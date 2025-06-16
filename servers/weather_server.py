from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for specified location"""
    return f"Weather in {location}: Sunny, 22°C"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
