# MCPSERVERLangchain

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools and context to language models. LangGraph agents can use tools defined on MCP servers through the langchain-mcp-adapters library.

# Run command

python launcher.py

# UV package install

uv init
uv myenv
.venv\Scripts\activate

uv add -r requirements.txt --link-mode=copy

uv pip show fastapi
