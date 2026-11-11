from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agent_skills.validators import validate_repository  # noqa: E402

if __name__ == "__main__":
    errors = validate_repository(ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("Skill validation passed.")
