# Complete MCP Server Deployment Guide for Amazon Bedrock AgentCore

This guide provides step-by-step instructions for successfully deploying and testing MCP servers on Amazon Bedrock AgentCore, based on lessons learned from real implementation.

## 🎯 Quick Start (5 Minutes)

```bash
# 1. Clone and setup
git clone https://github.com/Nadanne1/GenAIPOC.git
cd GenAIPOC/tools/mcp-integration
pip install -r requirements.txt

# 2. Set up authentication
chmod +x setup_cognito.sh
source setup_cognito.sh

# 3. Deploy MCP server
agentcore configure -e examples/mcp_server.py --protocol MCP --authorizer-config "$(cat authorizer_config.json)" --region us-east-1
agentcore launch

# 4. Test the deployment
export AGENT_ARN="<from_deployment_output>"
python3 examples/mcp_client.py
```

## 🔧 Detailed Implementation

### Step 1: MCP Server Implementation

**CRITICAL REQUIREMENTS** for AgentCore compatibility:

```python
from mcp.server.fastmcp import FastMCP

# ✅ REQUIRED: Use FastMCP (not Server)
# ✅ REQUIRED: host="0.0.0.0" (listen on all interfaces)  
# ✅ REQUIRED: stateless_http=True (for session isolation)
mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def your_tool(param: str) -> str:
    """Your tool description"""
    return f"Result: {param}"

if __name__ == "__main__":
    # ✅ REQUIRED: Use "streamable-http" transport
    mcp.run(transport="streamable-http")
```

**Common Mistakes to Avoid:**
- ❌ Using `mcp.server.Server` (doesn't work with AgentCore)
- ❌ Using `stdio` transport (AgentCore needs HTTP)
- ❌ Missing `stateless_http=True` (causes session issues)
- ❌ Wrong host configuration (must be "0.0.0.0")

### Step 2: Authentication Setup

AgentCore **requires** OAuth2 authentication. Use the provided script:

```bash
# Run the Cognito setup script
source setup_cognito.sh
```

This creates:
- Cognito User Pool
- App Client
- Test user with credentials
- Bearer token for authentication

**Authorizer Configuration Format:**
```json
{
  "customJWTAuthorizer": {
    "discoveryUrl": "https://cognito-idp.us-east-1.amazonaws.com/POOL_ID/.well-known/openid-configuration",
    "allowedClients": ["CLIENT_ID"]
  }
}
```

### Step 3: Deployment

```bash
# Configure with authentication
agentcore configure -e examples/mcp_server.py \
  --protocol MCP \
  --authorizer-config "$(cat authorizer_config.json)" \
  --region us-east-1

# Deploy to AWS
agentcore launch
```

**Expected Output:**
```
✅ Agent created/updated: arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/SERVER-ID
```

### Step 4: Client Testing

**CRITICAL CLIENT REQUIREMENTS:**

```python
# ✅ REQUIRED: Proper URL encoding
encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')

# ✅ REQUIRED: Correct AgentCore endpoint format
mcp_url = f"https://bedrock-agentcore.us-east-1.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"

# ✅ REQUIRED: Bearer token in authorization header
headers = {
    "authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# ✅ REQUIRED: Use MCP streamable HTTP client
async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as streams:
    # ... MCP session code
```

## 🚨 Common Issues and Solutions

### Issue 1: 406 Not Acceptable Error
**Cause:** Wrong MCP server implementation or missing headers
**Solution:** Use FastMCP with streamable-http transport

### Issue 2: 403 Forbidden Error  
**Cause:** Authentication not configured or wrong bearer token
**Solution:** Set up Cognito authentication and use valid bearer token

### Issue 3: Connection Timeout
**Cause:** Server not deployed or wrong endpoint URL
**Solution:** Verify deployment success and use correct URL format

### Issue 4: Tool Not Found
**Cause:** Server not properly initialized or wrong tool names
**Solution:** Check server logs and verify tool registration

## 📊 Testing Your Deployment

Use the provided test client:

```bash
# Set environment variables
export AGENT_ARN="arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/SERVER-ID"
export BEARER_TOKEN="your_cognito_bearer_token"

# Run tests
python3 examples/mcp_client.py
```

**Expected Success Output:**
```
🚀 Connecting to AgentCore MCP server...
✅ Connected to MCP server!
✅ Session initialized!
🔧 Listing available tools...
Available tools: ['add_numbers', 'multiply_numbers', 'greet_user', 'echo_message', 'get_timestamp', 'calculate']
🧪 Testing echo_message tool...
Echo result: Echo: Hello from AgentCore!
🧮 Testing calculate tool...
Calculate result: Result: 15.0 add 27.0 = 42.0
🎉 All tests completed successfully!
```

## 🔍 Debugging

### Check Server Status
```bash
agentcore status
```

### View Logs
```bash
aws logs tail /aws/bedrock-agentcore/runtimes/SERVER-ID-DEFAULT \
  --log-stream-name-prefix "2025/09/25/[runtime-logs]" \
  --region us-east-1 --follow
```

### Verify Authentication
```bash
# Test bearer token validity
aws cognito-idp get-user --access-token "$BEARER_TOKEN" --region us-east-1
```

## 🎉 Success Criteria

Your MCP server integration is successful when:

- ✅ `agentcore status` shows "Ready"
- ✅ Client connects without errors
- ✅ Tools are listed correctly
- ✅ Tool calls return expected results
- ✅ Authentication works with bearer token

## 📚 Additional Resources

- [AWS AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Example Repository](https://github.com/awslabs/amazon-bedrock-agentcore-samples)

## 🤝 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Verify all requirements are met
3. Review the working examples in this repository
4. Check AWS CloudWatch logs for detailed error information