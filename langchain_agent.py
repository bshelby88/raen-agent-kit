"""RAEN x402 tools in a LangGraph agent, via MCP."""
import os
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

RAEN_MCP_URL = "https://raen-mcp-gateway.fly.dev/mcp"

async def main():
    headers = {"Authorization": f"Bearer {os.environ['RAEN_MCP_KEY']}"}
    async with streamablehttp_client(RAEN_MCP_URL, headers=headers) as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent("openai:gpt-4o-mini", tools)
            result = await agent.ainvoke(
                {"messages": [{"role": "user",
                               "content": "Find RAEN tools for contract analysis and use one."}]})
            print(result["messages"][-1].content)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
