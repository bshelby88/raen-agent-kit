# RAEN Agent Kit

Plug RAEN's paid x402 MCP tools into your AI agent in minutes.
RAEN runs 12 live services on Base Mainnet (USDC micropayments, $0.01–$5.00/call).
Gateway: `https://raen-mcp-gateway.fly.dev/mcp` · Registry: `io.github.bshelby88/raen-mcp`

## Tools on the gateway
- law_lookup — query 36 RAEN statutes
- dispute_letter — generate dispute letters
- image_generate — image generation
- contract_analyze — contract analysis
- tool_finder — discover every RAEN x402 endpoint

## 1. Get a gateway key
Email `ops@royalruby.io` with subject "AGENT KIT KEY" — free dev keys for integration testing.

## 2. LangChain / LangGraph
```bash
pip install langchain-mcp-adapters langgraph
export RAEN_MCP_KEY=your-key
python langchain_agent.py
```

## 3. CrewAI
```bash
pip install crewai crewai-tools mcp
export RAEN_MCP_KEY=your-key
python crewai_agent.py
```

## Payments
Each call returns an x402 402 challenge; your agent wallet pays USDC on Base (eip155:8453).
payTo: `0x9b8a27e03ceba490953cda8ab1291c0e13baf72f`.
First-call-free rebate rail available — see https://raen.royalruby.io

## Links
- Statute pages: https://raen-law-pages.vercel.app
- MCP Registry: https://registry.modelcontextprotocol.io (search "raen")
