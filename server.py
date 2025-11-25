from fastmcp import FastMCP


app = FastMCP()


@app.tool
def greetings_tool(name: str) -> str:
  return f"Hello {name}, This is welcome from the MCP server of github"

if __name__ == "__main__":
    app.run()
