#!/bin/bash

# MCP Gateway Setup Script for Amazon Bedrock AgentCore
# This script sets up a gateway to connect to an existing MCP server

set -e

echo "🌉 Setting up MCP Gateway for AgentCore..."

# Configuration
GATEWAY_NAME="mcp-gateway"
DEFAULT_TARGET_URL="http://localhost:8000/mcp"

# Get target MCP server URL
echo "📡 Target MCP Server Configuration"
echo "Enter the URL of your existing MCP server:"
echo "Examples:"
echo "  - http://localhost:8000/mcp (local server)"
echo "  - https://your-domain.com/mcp (remote server)"
echo "  - http://internal-server:8000/mcp (internal network)"
echo ""
read -p "Target MCP Server URL [$DEFAULT_TARGET_URL]: " TARGET_URL
TARGET_URL=${TARGET_URL:-$DEFAULT_TARGET_URL}

echo "🔍 Testing connection to target server..."

# Test if target server is reachable
if curl -s --connect-timeout 5 "${TARGET_URL%/mcp}/health" > /dev/null 2>&1; then
    echo "✅ Target server is reachable"
elif curl -s --connect-timeout 5 "$TARGET_URL" > /dev/null 2>&1; then
    echo "✅ Target server is reachable"
else
    echo "⚠️  Warning: Cannot reach target server at $TARGET_URL"
    echo "   This might be normal if the server is not running yet"
    echo "   or requires authentication."
    read -p "Continue anyway? (y/N): " CONTINUE
    if [[ ! "$CONTINUE" =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled"
        exit 1
    fi
fi

# Create gateway configuration
echo "📝 Creating gateway configuration..."

cat > gateway_config.json << EOF
{
  "gateway_name": "$GATEWAY_NAME",
  "target_url": "$TARGET_URL",
  "proxy_mode": true,
  "authentication": {
    "type": "oauth2",
    "provider": "cognito"
  },
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

echo "✅ Gateway configuration created: gateway_config.json"

# Set up authentication (reuse existing Cognito setup if available)
if [ -f "../../authorizer_config.json" ] && [ -s "../../authorizer_config.json" ]; then
    echo "🔐 Found existing authentication configuration"
    POOL_ID=$(jq -r '.customJWTAuthorizer.discoveryUrl' ../../authorizer_config.json | sed 's/.*\/\([^\/]*\)\/.*/\1/')
    CLIENT_ID=$(jq -r '.customJWTAuthorizer.allowedClients[0]' ../../authorizer_config.json)
    
    if [ "$POOL_ID" != "null" ] && [ "$CLIENT_ID" != "null" ]; then
        echo "✅ Using existing Cognito configuration"
        echo "   Pool ID: $POOL_ID"
        echo "   Client ID: $CLIENT_ID"
    else
        echo "⚠️  Existing auth config is invalid, setting up new authentication..."
        source ../direct-deployment/setup_cognito.sh
    fi
else
    echo "🔐 Setting up authentication for gateway..."
    source ../direct-deployment/setup_cognito.sh
fi

# Create gateway deployment script
echo "📦 Creating gateway deployment script..."

cat > deploy_gateway.sh << 'EOF'
#!/bin/bash

echo "🚀 Deploying MCP Gateway to AgentCore..."

# Load configuration
if [ ! -f "gateway_config.json" ]; then
    echo "❌ Gateway configuration not found. Run setup_gateway.sh first."
    exit 1
fi

GATEWAY_NAME=$(jq -r '.gateway_name' gateway_config.json)
TARGET_URL=$(jq -r '.target_url' gateway_config.json)

echo "Gateway Name: $GATEWAY_NAME"
echo "Target URL: $TARGET_URL"

# Configure AgentCore for gateway
echo "⚙️  Configuring AgentCore..."
agentcore configure \
    -e examples/mcp_gateway.py \
    --protocol MCP \
    --authorizer-config "$(cat ../../authorizer_config.json)" \
    --region us-east-1 \
    --env TARGET_URL="$TARGET_URL"

# Deploy the gateway
echo "🚀 Launching gateway..."
agentcore launch

echo "✅ Gateway deployment completed!"
echo ""
echo "🔧 Next steps:"
echo "1. Note the Agent ARN from the deployment output"
echo "2. Set environment variables:"
echo "   export AGENT_ARN=\"<your_gateway_agent_arn>\""
echo "   export BEARER_TOKEN=\"<your_bearer_token>\""
echo "3. Test the gateway:"
echo "   python3 examples/gateway-integration/gateway_client.py"
EOF

chmod +x deploy_gateway.sh

echo "✅ Gateway deployment script created: deploy_gateway.sh"

# Create gateway client for testing
echo "🧪 Creating gateway test client..."

cat > examples/gateway-integration/gateway_client.py << 'EOF'
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
EOF

chmod +x examples/gateway-integration/gateway_client.py

echo "✅ Gateway test client created: examples/gateway-integration/gateway_client.py"

echo ""
echo "🎉 MCP Gateway setup completed!"
echo "=" * 50
echo "📋 Configuration Summary:"
echo "Gateway Name: $GATEWAY_NAME"
echo "Target URL: $TARGET_URL"
echo "Auth Config: ../../authorizer_config.json"
echo ""
echo "🚀 Next Steps:"
echo "1. Deploy the gateway:"
echo "   ./deploy_gateway.sh"
echo ""
echo "2. Test the gateway:"
echo "   export AGENT_ARN=\"<from_deployment_output>\""
echo "   python3 examples/gateway-integration/gateway_client.py"
echo ""
echo "💡 The gateway will proxy requests to your target MCP server"
echo "   while providing AWS authentication and AgentCore integration."