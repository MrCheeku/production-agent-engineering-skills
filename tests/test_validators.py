from pathlib import Path

from agent_skills.validators import check_local_markdown_links, validate_skill_text


def test_validator_rejects_missing_frontmatter() -> None:
    errors = validate_skill_text("# Not a skill", Path("SKILL.md"))
    assert "missing YAML frontmatter" in errors[0]


def test_validator_accepts_complete_skill() -> None:
    headings = (
        "Purpose", "Activation", "Required tools and inputs", "Recommended architecture",
        "Implementation workflow", "Coding standards", "Security requirements",
        "Error handling and observability", "Testing requirements", "Practical example",
        "Common mistakes and remedies", "Expected outputs", "Production-readiness checklist",
        "Quality-assurance checklist",
    )
    text = "---\nname: demo\ndescription: \"Demo skill\"\nversion: 1.0.0\n---\n"
    text += "".join(f"## {heading}\nContent.\n" for heading in headings)
    assert validate_skill_text(text) == []


def test_link_checker_detects_missing_target(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[missing](not-here.md)", encoding="utf-8")
    errors = check_local_markdown_links(tmp_path)
    assert errors and "not-here.md" in errors[0]
