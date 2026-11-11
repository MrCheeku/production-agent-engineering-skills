from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

REQUIRED_HEADINGS = (
    "## Purpose", "## Activation", "## Required tools and inputs",
    "## Recommended architecture", "## Implementation workflow", "## Coding standards",
    "## Security requirements", "## Error handling and observability", "## Testing requirements",
    "## Practical example", "## Common mistakes and remedies", "## Expected outputs",
    "## Production-readiness checklist", "## Quality-assurance checklist",
)
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
META_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)


def validate_skill_text(text: str, source: Path | str = Path("SKILL.md")) -> list[str]:
    errors: list[str] = []
    label = str(source)
    match = META_PATTERN.match(text)
    if not match:
        return [f"{label}: missing YAML frontmatter"]
    metadata = match.group(1)
    for key in ("name", "description", "version"):
        if not re.search(rf"^{key}:\s*.+$", metadata, re.MULTILINE):
            errors.append(f"{label}: missing frontmatter field '{key}'")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{label}: missing required section '{heading[3:]}'")
    return errors


def validate_repository(root: Path) -> list[str]:
    skill_root = root / "skills"
    if not skill_root.is_dir():
        return [f"Missing skills directory: {skill_root}"]
    paths = sorted(skill_root.glob("*/SKILL.md"))
    if not paths:
        return ["No skills/*/SKILL.md files found"]
    errors: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_skill_text(text, path.relative_to(root)))
        match = META_PATTERN.match(text)
        if match:
            name = re.search(r"^name:\s*(.+)$", match.group(1), re.MULTILINE)
            if name and name.group(1).strip().strip('"') != path.parent.name:
                errors.append(f"{path.relative_to(root)}: frontmatter name does not match directory")
    return errors


def check_local_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for markdown in root.rglob("*.md"):
        if any(part in {".git", ".venv", "node_modules"} for part in markdown.parts):
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK_PATTERN.findall(text):
            target = raw.strip().split()[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("#") or target.startswith("mailto:"):
                continue
            path_part = unquote(parsed.path)
            if not path_part:
                continue
            candidate = (markdown.parent / path_part).resolve()
            if not candidate.exists():
                errors.append(f"{markdown.relative_to(root)}: broken local link '{target}'")
    return errors


def generate_skill_index(root: Path) -> Path:
    rows: list[tuple[str, str]] = []
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        match = META_PATTERN.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        metadata = match.group(1)
        name = re.search(r"^name:\s*(.+)$", metadata, re.MULTILINE)
        description = re.search(r'^description:\s*"?(.*?)"?$', metadata, re.MULTILINE)
        if name and description:
            rows.append((name.group(1).strip().strip('"'), description.group(1).strip()))
    output = root / "skills" / "INDEX.md"
    body = "# Skill index\n\nThese skills use portable Markdown and YAML frontmatter.\n\n"
    body += "| Skill | Description |\n|---|---|\n"
    body += "".join(f"| [{slug}](./{slug}/SKILL.md) | {description} |\n" for slug, description in rows)
    output.write_text(body, encoding="utf-8")
    return output
