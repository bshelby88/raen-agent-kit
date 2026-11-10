"""RAEN x402 tools in a CrewAI crew, via MCP."""
import os
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

RAEN_MCP_URL = "https://raen-mcp-gateway.fly.dev/mcp"

with MCPServerAdapter(server_url=RAEN_MCP_URL,
                      headers={"Authorization": f"Bearer {os.environ['RAEN_MCP_KEY']}"}) as tools:
    researcher = Agent(role="RAEN Researcher",
                       goal="Use RAEN x402 tools to answer the task",
                       tools=tools, verbose=True)
    crew = Crew(agents=[researcher],
                tasks=[Task(description="Look up RAEN statute on settlements and summarize.",
                            expected_output="Short summary", agent=researcher)])
    print(crew.kickoff())
