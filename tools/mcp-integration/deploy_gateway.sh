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
    --authorizer-config "$(cat authorizer_config.json)" \
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
echo "   python3 examples/gateway_client.py"
