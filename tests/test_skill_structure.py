from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_every_skill_has_a_skill_file() -> None:
    dirs = [path for path in (ROOT / "skills").iterdir() if path.is_dir()]
    assert dirs
    assert all((directory / "SKILL.md").is_file() for directory in dirs)


def test_skill_index_exists() -> None:
    assert (ROOT / "skills" / "INDEX.md").is_file()
