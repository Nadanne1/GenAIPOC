#!/usr/bin/env python3
"""
Test client for MCP Gateway deployed on AgentCore

This client connects to the gateway and tests the proxy functionality.
"""

import asyncio
import os
import sys
import json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def test_gateway():
    """Test the deployed MCP gateway"""
    
    agent_arn = os.getenv('AGENT_ARN')
    bearer_token = os.getenv('BEARER_TOKEN')
    
    if not agent_arn or not bearer_token:
        print("❌ Error: AGENT_ARN or BEARER_TOKEN environment variable is not set")
        print("Set them with:")
        print("  export AGENT_ARN=\"<your_gateway_agent_arn>\"")
        print("  export BEARER_TOKEN=\"<your_bearer_token>\"")
        sys.exit(1)
    
    # Construct AgentCore URL
    encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')
    gateway_url = f"https://bedrock-agentcore.us-east-1.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"
    
    headers = {
        "authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    print("🌉 Testing MCP Gateway...")
    print(f"Gateway ARN: {agent_arn}")
    print(f"URL: {gateway_url}")
    print()
    
    try:
        async with streamablehttp_client(gateway_url, headers, timeout=120, terminate_on_close=False) as (
            read_stream, write_stream, _
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                print("✅ Connected to gateway!")
                
                # Test gateway status
                print("\n🔍 Checking gateway status...")
                status_result = await session.call_tool("gateway_status", {})
                status_data = json.loads(status_result.content[0].text)
                print(f"Gateway Status: {status_data['gateway_status']}")
                print(f"Target URL: {status_data['target_url']}")
                print(f"Target Status: {status_data['target_status']}")
                
                # List available tools from target
                print("\n🔧 Listing target server tools...")
                tools_result = await session.call_tool("list_target_tools", {})
                tools_data = json.loads(tools_result.content[0].text)
                
                if tools_data['available_tools']:
                    print("Available tools from target server:")
                    for tool in tools_data['available_tools']:
                        print(f"  - {tool['name']}: {tool['description']}")
                    
                    # Test proxying a tool call
                    if tools_data['available_tools']:
                        first_tool = tools_data['available_tools'][0]
                        print(f"\n🧪 Testing proxy call to '{first_tool['name']}'...")
                        
                        # Example arguments - adjust based on your target server's tools
                        test_args = {}
                        if first_tool['name'] == 'echo_message':
                            test_args = {"message": "Hello from gateway!"}
                        elif first_tool['name'] == 'add_numbers':
                            test_args = {"a": 5, "b": 3}
                        
                        try:
                            proxy_result = await session.call_tool("proxy_tool_call", {
                                "tool_name": first_tool['name'],
                                "arguments": test_args
                            })
                            print(f"✅ Proxy result: {proxy_result.content[0].text}")
                        except Exception as e:
                            print(f"⚠️  Proxy test failed: {e}")
                else:
                    print("⚠️  No tools available from target server")
                
                print("\n🎉 Gateway testing completed!")
                
    except Exception as e:
        print(f"❌ Gateway test failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Verify AGENT_ARN is correct (from gateway deployment output)")
        print("2. Check BEARER_TOKEN is valid (tokens expire after 1 hour)")
        print("3. Ensure gateway is deployed and ready")
        print("4. Verify target MCP server is running and accessible")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test_gateway())
