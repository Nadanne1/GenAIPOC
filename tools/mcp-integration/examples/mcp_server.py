# mcp_server.py
# Working MCP Server for Amazon Bedrock AgentCore
# This example demonstrates the correct implementation for AgentCore deployment

from mcp.server.fastmcp import FastMCP

# CRITICAL: AgentCore requires FastMCP with these specific settings
# - host="0.0.0.0": Listen on all interfaces
# - stateless_http=True: Required for AgentCore session isolation
mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def greet_user(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}! Nice to meet you."

@mcp.tool()
def echo_message(message: str) -> str:
    """Echo back the provided message"""
    return f"Echo: {message}"

@mcp.tool()
def get_timestamp() -> str:
    """Get current timestamp"""
    from datetime import datetime
    return f"Current timestamp: {datetime.now().isoformat()}"

@mcp.tool()
def calculate(operation: str, a: float, b: float) -> str:
    """Perform basic arithmetic calculations"""
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        result = a / b
    else:
        return f"Error: Unknown operation '{operation}'"
    
    return f"Result: {a} {operation} {b} = {result}"

if __name__ == "__main__":
    # CRITICAL: Must use "streamable-http" transport for AgentCore
    # This runs the server on 0.0.0.0:8000/mcp (AgentCore's expected endpoint)
    mcp.run(transport="streamable-http")