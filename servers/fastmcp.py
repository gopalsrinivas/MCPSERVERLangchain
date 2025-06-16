class FastMCP:
    def __init__(self, name):
        self.name = name
        self.tools = {}

    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func

        return decorator

    def run(self, transport="stdio"):
        print(f"Starting MCP server '{self.name}' with transport: {transport}")
