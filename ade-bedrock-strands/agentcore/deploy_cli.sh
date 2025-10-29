#!/bin/bash
# Deploy Financial Market Analyst Agent using AWS CLI

set -e

# Load environment variables
set -a
source .env
set +a

# Export AWS credentials
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export AWS_SESSION_TOKEN

echo "Deploying Financial Market Analyst Agent to AgentCore Runtime"
echo "Region: $AWS_REGION"
echo "Image: $ECR_IMAGE_URI"
echo "Role ARN: $AGENT_ROLE_ARN"
echo "Model: $BEDROCK_MODEL_ID"
echo "Knowledge Base: $BEDROCK_KB_ID"
echo ""

# Create agent runtime using AWS CLI
aws bedrock-agentcore-control create-agent-runtime \
  --agent-runtime-name financial_market_analyst_agent \
  --agent-runtime-artifact containerConfiguration={containerUri=$ECR_IMAGE_URI} \
  --role-arn $AGENT_ROLE_ARN \
  --network-configuration networkMode=PUBLIC \
  --environment-variables AWS_REGION=$AWS_REGION,BEDROCK_MODEL_ID=$BEDROCK_MODEL_ID,BEDROCK_KB_ID=$BEDROCK_KB_ID \
  --description "Financial Market Analyst Agent for Federal Reserve credit card banking analysis" \
  --region $AWS_REGION \
  --output json > agent_info.json

echo ""
echo "✓ Agent Runtime Created Successfully!"
echo ""

# Extract and display agent info
AGENT_RUNTIME_ARN=$(cat agent_info.json | grep -o '"agentRuntimeArn": "[^"]*"' | cut -d'"' -f4)
AGENT_RUNTIME_ID=$(cat agent_info.json | grep -o '"agentRuntimeId": "[^"]*"' | cut -d'"' -f4)
STATUS=$(cat agent_info.json | grep -o '"status": "[^"]*"' | cut -d'"' -f4)

echo "  - ARN: $AGENT_RUNTIME_ARN"
echo "  - ID: $AGENT_RUNTIME_ID"
echo "  - Status: $STATUS"
echo ""

# Save to simple text file
cat > agent_info.txt <<EOF
AGENT_RUNTIME_ARN=$AGENT_RUNTIME_ARN
AGENT_RUNTIME_ID=$AGENT_RUNTIME_ID
EOF

echo "✓ Agent info saved to agent_info.txt and agent_info.json"
echo ""
echo "Next steps:"
echo "1. Wait for agent status to become ACTIVE"
echo "2. Check status: aws bedrock-agentcore-control get-agent-runtime --agent-runtime-id $AGENT_RUNTIME_ID --region $AWS_REGION"
echo "3. Run: python invoke_agent.py"
