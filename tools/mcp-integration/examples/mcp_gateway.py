#!/usr/bin/env python3
"""
MCP Gateway for Amazon Bedrock AgentCore

This gateway acts as a proxy between AgentCore and an existing MCP server.
It handles authentication, request routing, and protocol translation.

Usage:
    python3 mcp_gateway.py --target-url http://localhost:8000/mcp
"""

import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, Optional
import argparse
import httpx
from mcp.server.fastmcp import FastMCP
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MCPGateway:
    """Gateway that proxies MCP requests to an external MCP server"""
    
    def __init__(self, target_url: str, port: int = 8000, timeout: int = 30):
        self.target_url = target_url
        self.timeout = timeout
        self.port = port
        self.mcp = FastMCP(host="0.0.0.0", port=port, stateless_http=True)
        self._setup_tools()
    
    def _setup_tools(self):
        """Set up gateway tools that proxy to the target server"""
        
        @self.mcp.tool()
        async def proxy_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
            """Proxy a tool call to the target MCP server"""
            try:
                return await self._call_target_tool(tool_name, arguments)
            except Exception as e:
                logger.error(f"Error proxying tool call {tool_name}: {e}")
                return f"Error: Failed to call {tool_name} - {str(e)}"
        
        @self.mcp.tool()
        async def list_target_tools() -> str:
            """List all available tools from the target MCP server"""
            try:
                tools = await self._get_target_tools()
                return json.dumps({
                    "available_tools": tools,
                    "target_server": self.target_url,
                    "gateway_status": "connected"
                }, indent=2)
            except Exception as e:
                logger.error(f"Error listing target tools: {e}")
                return f"Error: Failed to list tools - {str(e)}"
        
        @self.mcp.tool()
        async def gateway_status() -> str:
            """Get gateway status and connection info"""
            try:
                # Test connection to target
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.get(f"{self.target_url.rstrip('/mcp')}/health", 
                                              timeout=5)
                    target_status = "healthy" if response.status_code == 200 else "unhealthy"
            except Exception:
                target_status = "unreachable"
            
            return json.dumps({
                "gateway_status": "running",
                "target_url": self.target_url,
                "target_status": target_status,
                "proxy_mode": "enabled"
            }, indent=2)
    
    async def _get_target_tools(self) -> list:
        """Get list of tools from target MCP server"""
        try:
            async with streamablehttp_client(self.target_url, {}, timeout=self.timeout) as (
                read_stream, write_stream, _
            ):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    tools_result = await session.list_tools()
                    return [{"name": tool.name, "description": tool.description} 
                           for tool in tools_result.tools]
        except Exception as e:
            logger.error(f"Failed to get target tools: {e}")
            return []
    
    async def _call_target_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Call a specific tool on the target MCP server"""
        try:
            async with streamablehttp_client(self.target_url, {}, timeout=self.timeout) as (
                read_stream, write_stream, _
            ):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    result = await session.call_tool(tool_name, arguments)
                    
                    # Extract text content from result
                    if hasattr(result, 'content') and result.content:
                        return result.content[0].text if result.content[0].text else str(result.content[0])
                    else:
                        return str(result)
                        
        except Exception as e:
            logger.error(f"Failed to call target tool {tool_name}: {e}")
            raise
    
    def run(self):
        """Run the gateway server"""
        logger.info(f"Starting MCP Gateway on port {self.port}")
        logger.info(f"Proxying to target: {self.target_url}")
        
        try:
            self.mcp.run(transport="streamable-http")
        except KeyboardInterrupt:
            logger.info("Gateway stopped by user")
        except Exception as e:
            logger.error(f"Gateway error: {e}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="MCP Gateway for AgentCore")
    parser.add_argument("--target-url", required=True, 
                       help="URL of the target MCP server (e.g., http://localhost:8000/mcp)")
    parser.add_argument("--port", type=int, default=8000,
                       help="Port to run the gateway on (default: 8000)")
    parser.add_argument("--timeout", type=int, default=30,
                       help="Timeout for target server requests (default: 30)")
    parser.add_argument("--verbose", action="store_true",
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate target URL
    if not args.target_url.startswith(('http://', 'https://')):
        logger.error("Target URL must start with http:// or https://")
        sys.exit(1)
    
    # Create and run gateway
    gateway = MCPGateway(args.target_url, args.port, args.timeout)
    gateway.run()


if __name__ == "__main__":
    main()