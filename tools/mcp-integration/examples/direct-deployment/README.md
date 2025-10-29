# Direct MCP Server Deployment

Deploy your MCP server directly to AWS Bedrock AgentCore.

## Files

- `mcp_server.py` - MCP server implementation using FastMCP
- `mcp_client.py` - Client for testing the deployed server

## Usage

1. Set up authentication:
```bash
chmod +x setup_cognito.sh
source setup_cognito.sh
```

2. Deploy the server:
```bash
agentcore configure -e examples/direct-deployment/mcp_server.py --protocol MCP --authorizer-config "$(cat ../../authorizer_config.json)" --region us-east-1
agentcore launch
```

3. Test the deployment:
```bash
export AGENT_ARN="<from_deployment_output>"
python3 mcp_client.py
```

## When to Use

- Building a new MCP server
- Want full AWS integration
- Need maximum performance