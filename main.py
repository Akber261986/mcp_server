from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="My MCP Server",
    stateless_http= True
)

mcp_app = mcp.streamable_http_app()

# Greeting tool
@mcp.tool()
def greet(name: str):
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str):
    return f"The weather in {city} is sunny with a high of 25°C."

