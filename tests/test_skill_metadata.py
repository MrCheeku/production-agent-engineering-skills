from pathlib import Path
from agent_skills.validators import validate_skill_text

ROOT = Path(__file__).resolve().parents[1]


def test_all_skills_have_required_metadata_and_sections() -> None:
    paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    assert paths
    for path in paths:
        errors = validate_skill_text(path.read_text(encoding="utf-8"), path)
        assert not errors, "\\n".join(errors)
