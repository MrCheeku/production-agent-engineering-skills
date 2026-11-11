from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agent_skills.validators import generate_skill_index  # noqa: E402

if __name__ == "__main__":
    output = generate_skill_index(ROOT)
    print(f"Updated {output.relative_to(ROOT)}")
