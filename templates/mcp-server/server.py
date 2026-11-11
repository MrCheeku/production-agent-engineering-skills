from mcp.server import MCPServer

server = MCPServer("Example Template")


@server.tool()
def ping() -> str:
    """Return a simple health response."""
    return "pong"


if __name__ == "__main__":
    server.run()
