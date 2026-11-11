from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agent_skills.validators import check_local_markdown_links  # noqa: E402

if __name__ == "__main__":
    errors = check_local_markdown_links(ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("Local Markdown link check passed.")
