from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import os

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "-c",
                    "from servers.math_server import mcp; mcp.run(transport='stdio')",
                ],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )

    # Initialize agent
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b", api_key=os.getenv("GROQ_API_KEY"))
    agent = create_react_agent(model, tools)

    # Run queries
    math_res = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Calculate (3 + 5) × 12"}]}
    )
    print("Math Result:", math_res["messages"][-1].content)

    weather_res = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's the weather in Paris?"}]}
    )
    print("Weather Result:", weather_res["messages"][-1].content)
