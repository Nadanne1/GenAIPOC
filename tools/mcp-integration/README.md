# MCP Server Integration with Amazon Bedrock AgentCore

Model Context Protocol (MCP) server integration with Amazon Bedrock AgentCore.

## 📁 Pattern-Based Organization

This toolkit is organized into two clear implementation patterns:

- **[Direct Deployment](examples/direct-deployment/)** - Deploy MCP servers directly to AgentCore
- **[Gateway Integration](examples/gateway-integration/)** - Connect existing MCP servers through a gateway

Each pattern has its own folder with complete examples, scripts, and documentation.

## Quick Start

Choose your integration pattern:

**Direct Deployment:**
```bash
cd tools/mcp-integration
pip install -r requirements.txt
cd examples/direct-deployment
chmod +x setup_cognito.sh && source setup_cognito.sh
agentcore configure -e examples/direct-deployment/mcp_server.py --protocol MCP --authorizer-config "$(cat ../../authorizer_config.json)" --region us-east-1
agentcore launch
export AGENT_ARN="<from_deployment_output>"
python3 mcp_client.py
```

**Gateway Integration:**
```bash
cd tools/mcp-integration/examples/gateway-integration
chmod +x setup_gateway.sh && ./setup_gateway.sh
./deploy_gateway.sh
export AGENT_ARN="<from_deployment_output>"
python3 gateway_client.py
```

## Prerequisites

- **AWS Account**: With appropriate permissions for Bedrock AgentCore, IAM, and Cognito
- **AWS CLI**: Configured with valid credentials
- **Python**: Version 3.10 or higher
- **jq**: For JSON processing in setup scripts

## Two Integration Patterns

### Pattern 1: Direct MCP Server Deployment
Deploy your MCP server directly to AWS Bedrock AgentCore.

### Pattern 2: AgentCore Gateway
Connect to existing MCP servers through a gateway.

---

## Pattern 1: Direct MCP Server Deployment

### Step 1: Local Testing and Setup

```bash
pip install -r requirements.txt
source test_env/bin/activate
python3 examples/direct-deployment/test_mcp_integration.py
```

### Step 2: MCP Server Implementation

```python
from mcp.server.fastmcp import FastMCP

# Must use FastMCP with these settings
mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def echo_message(message: str) -> str:
    """Echo back the provided message"""
    return f"Echo: {message}"

if __name__ == "__main__":
    # Must use streamable-http transport
    mcp.run(transport="streamable-http")
```

**Requirements:**
- Use `FastMCP` (not `Server`)
- Set `host="0.0.0.0"` and `stateless_http=True`
- Use `transport="streamable-http"`
- Server runs on port 8000

### Step 3: Authentication Setup

AgentCore requires OAuth2 authentication:

```bash
chmod +x examples/direct-deployment/setup_cognito.sh
source examples/direct-deployment/setup_cognito.sh
```

Creates:
- Cognito User Pool and App Client
- Test user: `mcpuser` with password `SecurePass123!`
- Bearer token for authentication
- Updates `authorizer_config.json`

### Step 4: Deploy to AWS AgentCore

```bash
agentcore configure -e examples/direct-deployment/mcp_server.py --protocol MCP --authorizer-config "$(cat authorizer_config.json)" --region us-east-1
agentcore launch
```

Configuration notes:
- Use `Authorization` for request headers
- Choose CodeBuild deployment
- Save the Agent ARN from output

### Step 5: Test Your Deployment

```bash
export AGENT_ARN="arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/mcp_server-XXXXXXXX"
python3 examples/direct-deployment/mcp_client.py
agentcore status
```

---

## Pattern 2: AgentCore Gateway Integration

Connect existing MCP servers to AWS Bedrock AgentCore through a gateway proxy.

### Step 1: Test Gateway Integration

```bash
source test_env/bin/activate
python3 examples/gateway-integration/test_gateway_integration.py
```

### Step 2: Gateway Setup and Configuration

```bash
./examples/gateway-integration/setup_gateway.sh
```

Prompts for target MCP server URL and creates configuration files.

### Step 3: Deploy Gateway to AgentCore

```bash
./examples/gateway-integration/deploy_gateway.sh
```

### Step 4: Test Gateway Deployment

```bash
export AGENT_ARN="<your_gateway_agent_arn>"
export BEARER_TOKEN="<your_bearer_token>"
python3 examples/gateway-integration/gateway_client.py
```

### Gateway Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   MCP Client    │───▶│  AgentCore       │───▶│  MCP Gateway    │
│                 │    │  Gateway         │    │  (AWS Lambda)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
                                               ┌─────────────────┐
                                               │  Target MCP     │
                                               │  Server         │
                                               │  (External)     │
                                               └─────────────────┘
```

**Gateway Features:**
- Authentication with AWS Cognito OAuth2
- MCP protocol proxying
- Tool discovery and proxying
- Status monitoring

### Gateway Use Cases

- Connect existing MCP servers to AWS
- Add authentication to MCP servers
- Proxy multiple MCP servers



## Repository Structure

```
tools/mcp-integration/
├── README.md
├── DEPLOYMENT_GUIDE.md
├── examples/
│   ├── direct-deployment/
│   │   ├── mcp_server.py
│   │   ├── mcp_client.py
│   │   ├── setup_cognito.sh
│   │   ├── test_mcp_integration.py
│   │   └── README.md
│   └── gateway-integration/
│       ├── mcp_gateway.py
│       ├── gateway_client.py
│       ├── external_mcp_server.py
│       ├── setup_gateway.sh
│       ├── deploy_gateway.sh
│       ├── test_gateway_integration.py
│       └── README.md
├── authorizer_config.json
├── gateway_config.json
├── requirements.txt
└── .bedrock_agentcore.yaml
```

## Troubleshooting

**403 Forbidden Error:**
- Ensure bearer token is valid and not expired
- Check agent is deployed and status shows "Ready"

**Connection Timeout:**
- Verify Agent ARN is correct from deployment output
- Use `agentcore status` to confirm deployment

**Tool Not Found:**
- Check server logs with `aws logs tail` command
- Verify tool names match exactly in client calls

**Token Expiration:**
- Re-run `source examples/direct-deployment/setup_cognito.sh` to get fresh token
- Tokens expire after 1 hour

### Debug Commands

```bash
# Check deployment status
agentcore status

# View server logs
aws logs tail /aws/bedrock-agentcore/runtimes/YOUR-AGENT-ID-DEFAULT --log-stream-name-prefix "2025/09/25/[runtime-logs]" --follow

# Test bearer token validity
aws cognito-idp get-user --access-token "$BEARER_TOKEN" --region us-east-1

# Refresh authentication
source examples/direct-deployment/setup_cognito.sh
```

## Which Pattern Should You Choose?

### Choose Direct Deployment when:
- Building a new MCP server
- Want full AWS integration
- Need maximum performance

### Choose Gateway Pattern when:
- Have existing MCP servers to integrate
- Want to add AWS authentication to external services
- Need to connect internal company MCP servers

## Success Criteria

Integration is successful when:
- Local tests pass
- Deployment succeeds
- Client connects and lists tools
- Tool calls return expected results



## Additional Resources

- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Complete Deployment Guide](DEPLOYMENT_GUIDE.md)
- [AWS AgentCore Examples](https://github.com/awslabs/amazon-bedrock-agentcore-samples)

