from pathlib import Path

from agent_skills.validators import (
    check_local_markdown_links,
    generate_skill_index,
    validate_repository,
    validate_skill_text,
)

REQUIRED_HEADINGS = (
    "Purpose", "Activation", "Required tools and inputs", "Recommended architecture",
    "Implementation workflow", "Coding standards", "Security requirements",
    "Error handling and observability", "Testing requirements", "Practical example",
    "Common mistakes and remedies", "Expected outputs", "Production-readiness checklist",
    "Quality-assurance checklist",
)


def complete_skill(name: str = "demo", description: str = "Demo skill") -> str:
    frontmatter = (
        "---\n"
        f"name: {name}\n"
        f'description: "{description}"\n'
        "version: 1.0.0\n"
        "---\n"
    )
    return frontmatter + "".join(
        f"## {heading}\nContent.\n" for heading in REQUIRED_HEADINGS
    )


def test_validator_rejects_missing_frontmatter() -> None:
    errors = validate_skill_text("# Not a skill", Path("SKILL.md"))
    assert errors == ["SKILL.md: missing YAML frontmatter"]


def test_validator_accepts_complete_skill() -> None:
    assert validate_skill_text(complete_skill()) == []


def test_validator_reports_missing_metadata_and_sections() -> None:
    errors = validate_skill_text("---\nname: demo\n---\n# Demo\n")
    assert any("missing frontmatter field 'description'" in error for error in errors)
    assert any("missing frontmatter field 'version'" in error for error in errors)
    assert any("missing required section 'Purpose'" in error for error in errors)


def test_repository_validation_handles_missing_and_empty_skill_directories(
    tmp_path: Path,
) -> None:
    assert "Missing skills directory" in validate_repository(tmp_path)[0]
    (tmp_path / "skills").mkdir()
    assert validate_repository(tmp_path) == ["No skills/*/SKILL.md files found"]


def test_repository_validation_checks_frontmatter_directory_name(tmp_path: Path) -> None:
    skill_dir = tmp_path / "skills" / "expected-name"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        complete_skill(name="different-name"), encoding="utf-8"
    )
    errors = validate_repository(tmp_path)
    assert any("frontmatter name does not match directory" in error for error in errors)


def test_link_checker_detects_missing_target(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "[missing](not-here.md)", encoding="utf-8"
    )
    errors = check_local_markdown_links(tmp_path)
    assert errors and "not-here.md" in errors[0]


def test_link_checker_accepts_existing_and_external_links(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (tmp_path / "README.md").write_text(
        "[guide](docs/guide.md) [web](https://example.com) [anchor](#top) "
        "[email](mailto:test@example.com)",
        encoding="utf-8",
    )
    assert check_local_markdown_links(tmp_path) == []


def test_link_checker_ignores_generated_dependency_directories(tmp_path: Path) -> None:
    for directory in (".git", ".venv", "node_modules"):
        ignored = tmp_path / directory
        ignored.mkdir()
        (ignored / "generated.md").write_text(
            "[missing](missing.md)", encoding="utf-8"
        )
    assert check_local_markdown_links(tmp_path) == []


def test_skill_index_is_sorted_and_skips_invalid_metadata(tmp_path: Path) -> None:
    skills = tmp_path / "skills"
    for slug, content in (
        ("zeta", complete_skill("zeta", "Last skill")),
        ("alpha", complete_skill("alpha", "First skill")),
        ("invalid", "# No frontmatter"),
        ("missing-description", "---\nname: missing-description\n---\n"),
    ):
        directory = skills / slug
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(content, encoding="utf-8")

    output = generate_skill_index(tmp_path)
    result = output.read_text(encoding="utf-8")
    assert result.index("[alpha]") < result.index("[zeta]")
    assert "First skill" in result
    assert "Last skill" in result
    assert "invalid" not in result
