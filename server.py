"""
from fastmcp import FastMCP


app = FastMCP()


@app.tool
def greetings_tool(name: str) -> str:
  return f"Hello {name}, This is welcome from the MCP server of github"

if __name__ == "__main__":
    app.run()
"""

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool
def process(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health
