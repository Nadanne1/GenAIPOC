#!/usr/bin/env python3
"""
Test script for MCP Integration Toolkit
Tests the basic functionality of our MCP server and client examples
"""

import asyncio
import sys
import os
from datetime import datetime

# Add examples directory to path
sys.path.append('examples')

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import mcp
        print("✅ MCP package imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import MCP: {e}")
        return False
    
    try:
        import boto3
        print("✅ Boto3 imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Boto3: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Requests: {e}")
        return False
    
    return True

def test_mcp_server():
    """Test MCP server structure and tools"""
    print("\n🧪 Testing MCP server...")
    
    try:
        import simple_mcp_server
        server = simple_mcp_server.server
        
        print(f"✅ Server created: {server.name}")
        
        # Test that server has the expected structure
        if hasattr(server, 'name'):
            print("✅ Server has name attribute")
        else:
            print("❌ Server missing name attribute")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Failed to test MCP server: {e}")
        return False

def test_client():
    """Test MCP client structure"""
    print("\n🧪 Testing MCP client...")
    
    try:
        from client_example import MCPAgentCoreClient
        
        # Create client with mock values
        client = MCPAgentCoreClient("mock-arn", "mock-token")
        print("✅ Client created successfully")
        
        # Test client methods exist
        if hasattr(client, 'invoke_tool'):
            print("✅ Client has invoke_tool method")
        else:
            print("❌ Client missing invoke_tool method")
            return False
            
        if hasattr(client, 'list_tools'):
            print("✅ Client has list_tools method")
        else:
            print("❌ Client missing list_tools method")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Failed to test client: {e}")
        return False

async def test_server_tools():
    """Test MCP server tools functionality"""
    print("\n🧪 Testing MCP server tools...")
    
    try:
        import simple_mcp_server
        server = simple_mcp_server.server
        
        # Test list_tools
        tools = await simple_mcp_server.list_tools()
        print(f"✅ Server has {len(tools)} tools")
        
        tool_names = [tool.name for tool in tools]
        expected_tools = ["echo", "timestamp", "calculate"]
        
        for expected_tool in expected_tools:
            if expected_tool in tool_names:
                print(f"✅ Tool '{expected_tool}' found")
            else:
                print(f"❌ Tool '{expected_tool}' missing")
                return False
        
        # Test echo tool
        echo_result = await simple_mcp_server.call_tool("echo", {"message": "test"})
        if echo_result and len(echo_result) > 0:
            print(f"✅ Echo tool works: {echo_result[0].text}")
        else:
            print("❌ Echo tool failed")
            return False
        
        # Test timestamp tool
        timestamp_result = await simple_mcp_server.call_tool("timestamp", {})
        if timestamp_result and len(timestamp_result) > 0:
            print(f"✅ Timestamp tool works: {timestamp_result[0].text}")
        else:
            print("❌ Timestamp tool failed")
            return False
        
        # Test calculate tool
        calc_result = await simple_mcp_server.call_tool("calculate", {
            "operation": "add",
            "a": 5,
            "b": 3
        })
        if calc_result and len(calc_result) > 0:
            print(f"✅ Calculate tool works: {calc_result[0].text}")
        else:
            print("❌ Calculate tool failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to test server tools: {e}")
        return False

def test_deployment_script():
    """Test deployment script structure"""
    print("\n🧪 Testing deployment script...")
    
    script_path = "scripts/deploy.sh"
    if os.path.exists(script_path):
        print("✅ Deployment script exists")
        
        # Check if script is executable
        if os.access(script_path, os.X_OK):
            print("✅ Deployment script is executable")
        else:
            print("❌ Deployment script is not executable")
            return False
            
        return True
    else:
        print("❌ Deployment script not found")
        return False

async def main():
    """Run all tests"""
    print("🚀 Starting MCP Integration Toolkit Tests")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("MCP Server", test_mcp_server),
        ("Client", test_client),
        ("Deployment Script", test_deployment_script),
    ]
    
    async_tests = [
        ("Server Tools", test_server_tools),
    ]
    
    passed = 0
    total = len(tests) + len(async_tests)
    
    # Run synchronous tests
    for test_name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {test_name} test PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} test FAILED")
        except Exception as e:
            print(f"❌ {test_name} test ERROR: {e}")
    
    # Run asynchronous tests
    for test_name, test_func in async_tests:
        try:
            if await test_func():
                print(f"✅ {test_name} test PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} test FAILED")
        except Exception as e:
            print(f"❌ {test_name} test ERROR: {e}")
    
    print("\n" + "=" * 50)
    print(f"🏁 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MCP Integration Toolkit is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)