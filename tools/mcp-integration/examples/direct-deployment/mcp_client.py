# mcp_client.py
# Working MCP Client for Amazon Bedrock AgentCore
# This example demonstrates how to properly connect to and test an AgentCore MCP server

import asyncio
import os
import sys

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    """
    Test an MCP server deployed on Amazon Bedrock AgentCore
    
    Required environment variables:
    - AGENT_ARN: The AgentCore runtime ARN (from deployment output)
    - BEARER_TOKEN: OAuth2 bearer token from Cognito authentication
    """
    agent_arn = os.getenv('AGENT_ARN')
    bearer_token = os.getenv('BEARER_TOKEN')
    
    if not agent_arn or not bearer_token:
        print("❌ Error: Required environment variables not set")
        print("\nPlease set these environment variables:")
        print("export AGENT_ARN='arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/SERVER-ID'")
        print("export BEARER_TOKEN='your_cognito_bearer_token'")
        print("\nTo get a bearer token, run the Cognito setup script:")
        print("source setup_cognito.sh")
        sys.exit(1)
    
    # CRITICAL: Proper URL encoding and format for AgentCore
    encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')
    mcp_url = f"https://bedrock-agentcore.us-east-1.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"
    
    # CRITICAL: Required headers for AgentCore authentication
    headers = {
        "authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    print("🚀 Connecting to AgentCore MCP server...")
    print(f"Agent ARN: {agent_arn}")
    print(f"URL: {mcp_url}")
    print()

    try:
        # Connect using MCP streamable HTTP client
        async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
            read_stream,
            write_stream,
            _,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                print("✅ Connected to MCP server!")
                
                # Initialize the MCP session
                await session.initialize()
                print("✅ Session initialized!")
                
                # List all available tools
                print("\n🔧 Listing available tools...")
                tool_result = await session.list_tools()
                tool_names = [tool.name for tool in tool_result.tools]
                print(f"Available tools: {tool_names}")
                
                # Test echo tool
                print("\n🧪 Testing echo_message tool...")
                echo_result = await session.call_tool("echo_message", {"message": "Hello from AgentCore!"})
                print(f"Echo result: {echo_result.content[0].text}")
                
                # Test calculation tool
                print("\n🧮 Testing calculate tool...")
                calc_result = await session.call_tool("calculate", {"operation": "add", "a": 15, "b": 27})
                print(f"Calculate result: {calc_result.content[0].text}")
                
                # Test timestamp tool
                print("\n⏰ Testing get_timestamp tool...")
                time_result = await session.call_tool("get_timestamp", {})
                print(f"Timestamp result: {time_result.content[0].text}")
                
                print("\n🎉 All tests completed successfully!")
                print("✅ MCP server integration with AgentCore is working!")
                
    except Exception as e:
        print(f"❌ Error connecting to MCP server: {e}")
        print("\nTroubleshooting tips:")
        print("1. Verify AGENT_ARN is correct (from agentcore launch output)")
        print("2. Check BEARER_TOKEN is valid (tokens expire after 1 hour)")
        print("3. Ensure AgentCore server is deployed and ready")
        print("4. Verify AWS credentials and region settings")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())