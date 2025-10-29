#!/usr/bin/env python3
"""
External MCP Server for Gateway Testing

This is a simple MCP server that can run independently and be accessed
through the MCP Gateway. It simulates an existing MCP server that you
want to make accessible through AWS Bedrock AgentCore.

Usage:
    python3 external_mcp_server.py --port 8001
"""

import argparse
import logging
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_external_server(port: int = 8001) -> FastMCP:
    """Create an external MCP server with sample tools"""
    
    # Create server that listens on all interfaces with specified port
    mcp = FastMCP(host="0.0.0.0", port=port, stateless_http=True)
    
    @mcp.tool()
    def external_echo(message: str) -> str:
        """Echo a message from the external server"""
        return f"External Server Echo: {message}"
    
    @mcp.tool()
    def external_calculate(operation: str, a: float, b: float) -> str:
        """Perform calculations on the external server"""
        try:
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
            
            return f"External Server: {a} {operation} {b} = {result}"
        except Exception as e:
            return f"External Server Error: {str(e)}"
    
    @mcp.tool()
    def external_server_info() -> str:
        """Get information about this external server"""
        return f"""External MCP Server Info:
- Server Type: Independent MCP Server
- Port: {port}
- Status: Running
- Timestamp: {datetime.now().isoformat()}
- Purpose: Gateway target for testing
- Tools: external_echo, external_calculate, external_server_info, external_health_check
"""
    
    @mcp.tool()
    def external_health_check() -> str:
        """Health check endpoint for the external server"""
        return f"External Server Health: OK - {datetime.now().isoformat()}"
    
    # Note: FastMCP doesn't support HTTP routes, only MCP tools
    # Health check will be done via MCP tool calls
    
    return mcp


def main():
    parser = argparse.ArgumentParser(description="External MCP Server for Gateway Testing")
    parser.add_argument("--port", type=int, default=8001,
                       help="Port to run the server on (default: 8001)")
    parser.add_argument("--verbose", action="store_true",
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Create and run the external server
    server = create_external_server(args.port)
    
    logger.info(f"🚀 Starting External MCP Server on port {args.port}")
    logger.info(f"📡 Server will be accessible at: http://localhost:{args.port}/mcp")
    logger.info(f"🏥 Health check available at: http://localhost:{args.port}/health")
    logger.info("🌉 This server can be used as a target for the MCP Gateway")
    logger.info("💡 Use Ctrl+C to stop the server")
    
    try:
        server.run(transport="streamable-http")
    except KeyboardInterrupt:
        logger.info("🛑 External server stopped by user")
    except Exception as e:
        logger.error(f"❌ Server error: {e}")


if __name__ == "__main__":
    main()