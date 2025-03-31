from mcp.server.fastmcp import FastMCP

mcp = FastMCP("echo server")

@mcp.tool()
def echo_message(message: str) -> str:
    return f"Response: {message}"

if __name__ == "__main__":
    mcp.run(transport='stdio')