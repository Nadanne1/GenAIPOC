#!/usr/bin/env python3
"""
Simple MCP Server Example
A basic MCP server implementation for testing with Amazon Bedrock AgentCore
"""

from mcp.server import Server
from mcp.types import Tool, TextContent, Resource
import asyncio
import json
from datetime import datetime

# Create server instance
server = Server("simple-mcp-server")

@server.list_tools()
async def list_tools():
    """List available tools"""
    return [
        Tool(
            name="echo",
            description="Echo back the provided message",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Message to echo back"
                    }
                },
                "required": ["message"]
            }
        ),
        Tool(
            name="timestamp",
            description="Get current timestamp",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="calculate",
            description="Perform basic arithmetic calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "Arithmetic operation to perform"
                    },
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    """Handle tool calls"""
    
    if name == "echo":
        message = arguments.get("message", "")
        return [TextContent(
            type="text",
            text=f"Echo: {message}"
        )]
    
    elif name == "timestamp":
        current_time = datetime.now().isoformat()
        return [TextContent(
            type="text",
            text=f"Current timestamp: {current_time}"
        )]
    
    elif name == "calculate":
        operation = arguments.get("operation")
        a = arguments.get("a")
        b = arguments.get("b")
        
        try:
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return [TextContent(
                        type="text",
                        text="Error: Division by zero"
                    )]
                result = a / b
            else:
                return [TextContent(
                    type="text",
                    text=f"Error: Unknown operation '{operation}'"
                )]
            
            return [TextContent(
                type="text",
                text=f"Result: {a} {operation} {b} = {result}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"Error: {str(e)}"
            )]
    
    else:
        return [TextContent(
            type="text",
            text=f"Error: Unknown tool '{name}'"
        )]

@server.list_resources()
async def list_resources():
    """List available resources"""
    return [
        Resource(
            uri="info://server",
            name="Server Information",
            description="Information about this MCP server"
        )
    ]

@server.read_resource()
async def read_resource(uri: str):
    """Read resource content"""
    if uri == "info://server":
        info = {
            "name": "Simple MCP Server",
            "version": "1.0.0",
            "description": "A basic MCP server for testing with Amazon Bedrock AgentCore",
            "tools": ["echo", "timestamp", "calculate"],
            "resources": ["info://server"]
        }
        return [TextContent(
            type="text",
            text=json.dumps(info, indent=2)
        )]
    else:
        return [TextContent(
            type="text",
            text=f"Error: Resource '{uri}' not found"
        )]

if __name__ == "__main__":
    print("Starting Simple MCP Server...")
    print("Available tools: echo, timestamp, calculate")
    print("Available resources: info://server")
    print("Press Ctrl+C to stop")
    
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("\nServer stopped")