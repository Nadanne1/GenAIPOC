# Gateway Integration Pattern

Connect existing MCP servers to AWS Bedrock AgentCore through a gateway proxy.

## Files

- `mcp_gateway.py` - Gateway proxy server that connects to external MCP servers
- `gateway_client.py` - Client for testing the deployed gateway
- `external_mcp_server.py` - Example external MCP server for testing

## Usage

1. Set up and deploy the gateway:
```bash
./setup_gateway.sh
./deploy_gateway.sh
```

2. Test the gateway:
```bash
export AGENT_ARN="<from_deployment_output>"
python3 gateway_client.py
```

3. Test with external server (for development):
```bash
# Start external server
python3 external_mcp_server.py --port 8001

# Test gateway integration
python3 test_gateway_integration.py
```

## When to Use

- Have existing MCP servers to integrate
- Want to add AWS authentication to external services
- Need to connect internal company MCP servers