from mcp.server import MCPServer

from safety import safe_calculate

server = MCPServer("Production Agent Utilities")


@server.tool()
def calculate(expression: str) -> str:
    """Evaluate a bounded arithmetic expression; code execution is not supported."""
    try:
        return str(safe_calculate(expression))
    except (ValueError, ZeroDivisionError) as exc:
        return f"Rejected: {exc}"


@server.tool()
def text_statistics(text: str) -> dict[str, int]:
    """Return character, word, and line counts for supplied text."""
    if len(text) > 50_000:
        raise ValueError("Text exceeds the 50,000-character limit")
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()) or (1 if text else 0),
    }


if __name__ == "__main__":
    server.run()
