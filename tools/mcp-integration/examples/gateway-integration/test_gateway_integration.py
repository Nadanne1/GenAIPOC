#!/usr/bin/env python3
"""
MCP Gateway Integration Test Suite

This script tests the complete gateway integration:
1. Starts an external MCP server
2. Tests the gateway locally
3. Validates proxy functionality
4. Provides deployment readiness check

Usage:
    python3 test_gateway_integration.py
"""

import asyncio
import json
import logging
import multiprocessing
import os
import sys
import time
import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class GatewayTester:
    """Test suite for MCP Gateway functionality"""
    
    def __init__(self):
        self.external_server_port = 8001
        self.gateway_port = 8002
        self.external_server_url = f"http://localhost:{self.external_server_port}/mcp"
        self.gateway_url = f"http://localhost:{self.gateway_port}/mcp"
        self.test_results = []
    
    def log_test(self, test_name: str, success: bool, message: str = ""):
        """Log test result"""
        status = "✅" if success else "❌"
        logger.info(f"{status} {test_name}")
        if message:
            logger.info(f"   {message}")
        self.test_results.append({"test": test_name, "success": success, "message": message})
    
    async def test_external_server_connection(self) -> bool:
        """Test connection to external MCP server"""
        try:
            # Test MCP endpoint (should return 406 for regular HTTP GET)
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://localhost:{self.external_server_port}/mcp", timeout=5)
                if response.status_code == 406:  # Expected for MCP endpoint
                    self.log_test("External Server Connection", True, 
                                "MCP endpoint responding (406 expected)")
                    return True
                else:
                    self.log_test("External Server Connection", False, 
                                f"Unexpected HTTP {response.status_code}")
                    return False
        except Exception as e:
            self.log_test("External Server Connection", False, str(e))
            return False
    
    async def test_external_server_mcp(self) -> bool:
        """Test MCP functionality of external server"""
        try:
            async with streamablehttp_client(self.external_server_url, {}, timeout=10) as (
                read_stream, write_stream, _
            ):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    
                    # List tools
                    tools = await session.list_tools()
                    tool_names = [tool.name for tool in tools.tools]
                    
                    if len(tool_names) > 0:
                        self.log_test("External Server MCP Tools", True, 
                                    f"Found {len(tool_names)} tools: {', '.join(tool_names)}")
                        
                        # Test a tool call
                        if "external_echo" in tool_names:
                            result = await session.call_tool("external_echo", {"message": "test"})
                            if "External Server Echo: test" in result.content[0].text:
                                self.log_test("External Server Tool Call", True, 
                                            "Echo tool working correctly")
                                return True
                            else:
                                self.log_test("External Server Tool Call", False, 
                                            f"Unexpected result: {result.content[0].text}")
                                return False
                        else:
                            self.log_test("External Server Tool Call", False, 
                                        "external_echo tool not found")
                            return False
                    else:
                        self.log_test("External Server MCP Tools", False, "No tools found")
                        return False
                        
        except Exception as e:
            self.log_test("External Server MCP Connection", False, str(e))
            return False
    
    async def test_gateway_connection(self) -> bool:
        """Test connection to gateway"""
        try:
            # Test MCP endpoint (should return 406 for regular HTTP GET)
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://localhost:{self.gateway_port}/mcp", timeout=5)
                if response.status_code == 406:  # Expected for MCP endpoint
                    self.log_test("Gateway Connection", True, 
                                "MCP endpoint responding (406 expected)")
                    return True
                else:
                    self.log_test("Gateway Connection", False, 
                                f"Unexpected HTTP {response.status_code}")
                    return False
        except Exception as e:
            self.log_test("Gateway Connection", False, str(e))
            return False
    
    async def test_gateway_mcp(self) -> bool:
        """Test MCP functionality of gateway"""
        try:
            async with streamablehttp_client(self.gateway_url, {}, timeout=10) as (
                read_stream, write_stream, _
            ):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    
                    # List gateway tools
                    tools = await session.list_tools()
                    tool_names = [tool.name for tool in tools.tools]
                    
                    expected_tools = ["proxy_tool_call", "list_target_tools", "gateway_status"]
                    if all(tool in tool_names for tool in expected_tools):
                        self.log_test("Gateway MCP Tools", True, 
                                    f"Found all expected tools: {', '.join(expected_tools)}")
                        return True
                    else:
                        missing = [tool for tool in expected_tools if tool not in tool_names]
                        self.log_test("Gateway MCP Tools", False, 
                                    f"Missing tools: {', '.join(missing)}")
                        return False
                        
        except Exception as e:
            self.log_test("Gateway MCP Connection", False, str(e))
            return False
    
    async def test_gateway_proxy(self) -> bool:
        """Test gateway proxy functionality"""
        try:
            async with streamablehttp_client(self.gateway_url, {}, timeout=15) as (
                read_stream, write_stream, _
            ):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    
                    # Test gateway status
                    status_result = await session.call_tool("gateway_status", {})
                    status_data = json.loads(status_result.content[0].text)
                    
                    if status_data.get("gateway_status") == "running":
                        self.log_test("Gateway Status Check", True, 
                                    f"Target: {status_data.get('target_status', 'unknown')}")
                    else:
                        self.log_test("Gateway Status Check", False, 
                                    f"Status: {status_data.get('gateway_status', 'unknown')}")
                        return False
                    
                    # Test listing target tools
                    tools_result = await session.call_tool("list_target_tools", {})
                    tools_data = json.loads(tools_result.content[0].text)
                    
                    if tools_data.get("available_tools"):
                        tool_count = len(tools_data["available_tools"])
                        self.log_test("Gateway Target Tools List", True, 
                                    f"Found {tool_count} target tools")
                        
                        # Test proxy call
                        proxy_result = await session.call_tool("proxy_tool_call", {
                            "tool_name": "external_echo",
                            "arguments": {"message": "Gateway proxy test"}
                        })
                        
                        if "External Server Echo: Gateway proxy test" in proxy_result.content[0].text:
                            self.log_test("Gateway Proxy Call", True, 
                                        "Successfully proxied tool call")
                            return True
                        else:
                            self.log_test("Gateway Proxy Call", False, 
                                        f"Unexpected proxy result: {proxy_result.content[0].text}")
                            return False
                    else:
                        self.log_test("Gateway Target Tools List", False, 
                                    "No target tools found")
                        return False
                        
        except Exception as e:
            self.log_test("Gateway Proxy Test", False, str(e))
            return False
    
    def print_summary(self):
        """Print test summary"""
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        logger.info("")
        logger.info("=" * 60)
        logger.info(f"🏁 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            logger.info("🎉 All tests passed! Gateway integration is working correctly.")
            logger.info("")
            logger.info("🚀 Ready for deployment:")
            logger.info("1. Run: ./setup_gateway.sh")
            logger.info("2. Configure target URL (or use the external server)")
            logger.info("3. Deploy: ./deploy_gateway.sh")
        else:
            logger.info("❌ Some tests failed. Check the issues above.")
            logger.info("")
            logger.info("🔧 Troubleshooting:")
            for result in self.test_results:
                if not result["success"]:
                    logger.info(f"   - {result['test']}: {result['message']}")
    
    async def run_tests(self):
        """Run all gateway tests"""
        logger.info("🚀 Starting MCP Gateway Integration Tests")
        logger.info("=" * 60)
        
        # Test external server
        logger.info("🧪 Testing External MCP Server...")
        await self.test_external_server_connection()
        await self.test_external_server_mcp()
        
        # Test gateway
        logger.info("")
        logger.info("🌉 Testing MCP Gateway...")
        await self.test_gateway_connection()
        await self.test_gateway_mcp()
        await self.test_gateway_proxy()
        
        self.print_summary()


def start_external_server():
    """Start external MCP server in a separate process"""
    import subprocess
    import sys
    
    cmd = [sys.executable, "external_mcp_server.py", "--port", "8001"]
    logger.info(f"Starting external server: {' '.join(cmd)}")
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def start_gateway():
    """Start MCP gateway in a separate process"""
    import subprocess
    import sys
    
    cmd = [sys.executable, "mcp_gateway.py", 
           "--target-url", "http://localhost:8001/mcp", 
           "--port", "8002"]
    logger.info(f"Starting gateway: {' '.join(cmd)}")
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


async def main():
    """Main test function"""
    logger.info("🔧 Setting up test environment...")
    
    # Start external server
    logger.info("🚀 Starting external MCP server...")
    external_process = start_external_server()
    
    # Wait for external server to start
    await asyncio.sleep(3)
    
    # Start gateway
    logger.info("🌉 Starting MCP gateway...")
    gateway_process = start_gateway()
    
    # Wait for gateway to start
    await asyncio.sleep(3)
    
    try:
        # Run tests
        tester = GatewayTester()
        await tester.run_tests()
        
    finally:
        # Clean up processes
        logger.info("")
        logger.info("🧹 Cleaning up test processes...")
        
        try:
            gateway_process.terminate()
            gateway_process.wait(timeout=5)
        except:
            gateway_process.kill()
        
        try:
            external_process.terminate()
            external_process.wait(timeout=5)
        except:
            external_process.kill()
        
        logger.info("✅ Test environment cleaned up")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Test suite error: {e}")
        sys.exit(1)