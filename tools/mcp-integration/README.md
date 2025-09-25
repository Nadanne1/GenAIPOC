# MCP Server Integration with Amazon Bedrock AgentCore

This guide provides step-by-step instructions for integrating Model Context Protocol (MCP) servers with Amazon Bedrock AgentCore. You can choose between two approaches:

1. **CLI-based Deployment**: Quick setup using the AgentCore CLI
2. **SDK-based Integration**: Programmatic integration using Python SDKs

## Prerequisites

Before starting the integration, ensure you have:

- **AWS Account**: With appropriate permissions for IAM roles, Lambda functions, and Cognito resources
- **AWS Credentials**: Configured on your development environment
- **Python**: Version 3.10 or higher (3.6+ for SDK approach)
- **Required Packages**: Listed in the installation sections below

## Approach 1: CLI-based Deployment (Recommended for Quick Setup)

This approach uses the AgentCore CLI for streamlined deployment and management.

### Option 1A: Deploy Your MCP Server on Bedrock AgentCore

#### Step 1: Create Your MCP Server

Install the MCP package:

```bash
pip install mcp
```

Create your MCP server (e.g., `my_mcp_server.py`):

```python
from mcp.server import Server
from mcp.types import Tool, TextContent
import asyncio

# Create server instance
server = Server("my-mcp-server")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="example_tool",
            description="An example tool",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {"type": "string"}
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "example_tool":
        return [TextContent(
            type="text",
            text=f"Hello, {arguments.get('message', 'World')}!"
        )]

if __name__ == "__main__":
    asyncio.run(server.run())
```

Test your MCP server locally:

```bash
python my_mcp_server.py
```

#### Step 2: Configure Your Deployment

Install the Amazon Bedrock AgentCore CLI:

```bash
pip install bedrock-agentcore-starter-toolkit
```

Configure your deployment:

```bash
agentcore configure -e my_mcp_server.py --protocol MCP
```

Follow the guided prompts to:
- Set up Cognito user pool for authentication
- Configure deployment parameters
- Specify resource requirements

#### Step 3: Deploy to AWS

Deploy your agent:

```bash
agentcore launch
```

Save the agent runtime ARN from the deployment output.

#### Step 4: Invoke Your Deployed MCP Server

Set environment variables:

```bash
export AGENT_ARN="<your_agent_runtime_arn>"
export BEARER_TOKEN="<your_bearer_token>"
```

Create a client script (`client.py`):

```python
import os
import requests
import json

def invoke_mcp_server(tool_name: str, arguments: dict):
    agent_arn = os.getenv("AGENT_ARN")
    bearer_token = os.getenv("BEARER_TOKEN")
    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    
    # Replace with actual AgentCore endpoint
    url = f"https://agentcore.bedrock.aws.com/agents/{agent_arn}/invoke"
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Usage
if __name__ == "__main__":
    result = invoke_mcp_server("example_tool", {"message": "AgentCore"})
    print(json.dumps(result, indent=2))
```

### Option 1B: Connect to Existing MCP Server Using AgentCore Gateway

#### Step 1: Configure the AgentCore Gateway

Ensure your existing MCP server is running and accessible.

Install the AgentCore CLI:

```bash
pip install bedrock-agentcore-starter-toolkit
```

Configure the gateway:

```bash
agentcore configure --protocol MCP --endpoint "<your_mcp_server_url>"
```

Provide configuration details:
- MCP server endpoint URL
- Authentication method
- Cognito user pool settings

#### Step 2: Deploy the AgentCore Gateway

Deploy the gateway:

```bash
agentcore launch
```

Note the gateway runtime ARN from the deployment output.

#### Step 3: Invoke Through the Gateway

Set environment variables:

```bash
export AGENT_ARN="<your_gateway_runtime_arn>"
export BEARER_TOKEN="<your_bearer_token>"
```

Use the same client script as above to invoke your MCP server through the gateway.

## Approach 2: SDK-based Integration (Advanced)

This approach provides more control and customization options using Python SDKs.

### Installation

Install the required Python packages:

```bash
pip install boto3
pip install bedrock-agentcore-starter-toolkit
pip install bedrock-agentcore
pip install strands-agents
```

### Integration Steps

#### Step 1: Initialize Gateway Client

Set up the gateway client with proper logging configuration:

```python
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import logging

# Setup client
client = GatewayClient(region_name="us-east-1")
client.logger.setLevel(logging.DEBUG)
```

#### Step 2: Create Authorization

Create a Cognito authorizer for secure access:

```python
# Create Cognito authorizer
cognito_response = client.create_oauth_authorizer_with_cognito("TestGateway")
```

#### Step 3: Create MCP Gateway

Initialize the gateway with the authorization configuration:

```python
# Create gateway
gateway = client.create_mcp_gateway(
    authorizer_config=cognito_response["authorizer_config"]
)
```

#### Step 4: Add Target to Gateway

Create a Lambda target for the gateway:

```python
# Create a lambda target
lambda_target = client.create_mcp_gateway_target(
    gateway=gateway, 
    target_type="lambda"
)
```

#### Step 5: Obtain Access Token

Get the access token for authentication:

```python
# Get access token
access_token = client.get_access_token_for_cognito(
    cognito_response["client_info"]
)
```

#### Step 6: Connect to Gateway

Establish connection to the MCP gateway:

```python
def create_streamable_http_transport(mcp_url: str, access_token: str):
    return streamablehttp_client(
        mcp_url, 
        headers={"Authorization": f"Bearer {access_token}"}
    )

# Create MCP client
mcp_client = MCPClient(
    lambda: create_streamable_http_transport(
        gateway["gatewayUrl"], 
        access_token
    )
)
```

## Getting Bearer Tokens

For both approaches, you'll need to obtain bearer tokens for authentication:

### Using AWS Cognito

```python
import boto3
from botocore.exceptions import ClientError

def get_bearer_token(user_pool_id: str, client_id: str, username: str, password: str):
    client = boto3.client('cognito-idp')
    
    try:
        response = client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        
        return response['AuthenticationResult']['AccessToken']
    except ClientError as e:
        print(f"Error getting token: {e}")
        return None

# Usage
token = get_bearer_token(
    user_pool_id="us-east-1_xxxxxxxxx",
    client_id="your_client_id",
    username="your_username",
    password="your_password"
)
```

### Using AgentCore CLI

```bash
# Get token using CLI
agentcore auth login --username your_username --password your_password
agentcore auth token
```

## Configuration Options

### Custom Gateway Configuration

You can customize the gateway and targets using:

- **Custom IAM Roles**: Define specific permissions for your use case
- **Custom Lambda Functions**: Use existing Lambda functions as targets
- **API Specifications**: Support for both Smithy and OpenAPI specifications

### Authentication Methods

The gateway supports multiple authentication methods:

- **API Keys**: Simple key-based authentication
- **OAuth2**: Token-based authentication with Cognito
- **Custom Authorization**: Implement your own authorization logic

## Best Practices

1. **Security**: Always use least-privilege IAM roles
2. **Logging**: Enable debug logging during development
3. **Error Handling**: Implement proper error handling for network issues
4. **Token Management**: Refresh access tokens before expiration
5. **Monitoring**: Set up CloudWatch monitoring for your gateway

## Troubleshooting

### Common Issues

#### CLI Approach Issues
- **Configuration Errors**: Run `agentcore configure --help` for parameter details
- **Deployment Failures**: Check AWS permissions and resource limits
- **Connection Issues**: Verify MCP server endpoint accessibility

#### SDK Approach Issues
- **Authentication Errors**: Verify AWS credentials and IAM permissions
- **Network Issues**: Check VPC configuration and security groups
- **Token Expiration**: Implement token refresh logic
- **Lambda Timeouts**: Adjust Lambda timeout settings for long-running operations

### Debug Tips

#### For CLI Approach
- Use `agentcore logs` to view deployment logs
- Check `agentcore status` for deployment health
- Use `--verbose` flag with CLI commands for detailed output

#### For SDK Approach
- Enable debug logging to see detailed request/response information
- Use AWS CloudTrail to track API calls
- Monitor CloudWatch logs for Lambda function errors
- Test connectivity with simple HTTP requests first

## Example Implementation

Here's a complete example combining all steps:

```python
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import logging

def setup_mcp_gateway():
    # Initialize client
    client = GatewayClient(region_name="us-east-1")
    client.logger.setLevel(logging.DEBUG)
    
    # Create authorization
    cognito_response = client.create_oauth_authorizer_with_cognito("MyMCPGateway")
    
    # Create gateway
    gateway = client.create_mcp_gateway(
        authorizer_config=cognito_response["authorizer_config"]
    )
    
    # Add target
    lambda_target = client.create_mcp_gateway_target(
        gateway=gateway, 
        target_type="lambda"
    )
    
    # Get access token
    access_token = client.get_access_token_for_cognito(
        cognito_response["client_info"]
    )
    
    # Create transport function
    def create_transport():
        return streamablehttp_client(
            gateway["gatewayUrl"],
            headers={"Authorization": f"Bearer {access_token}"}
        )
    
    # Create MCP client
    mcp_client = MCPClient(create_transport)
    
    return mcp_client, gateway

# Usage
if __name__ == "__main__":
    client, gateway = setup_mcp_gateway()
    print(f"Gateway URL: {gateway['gatewayUrl']}")
```

## Next Steps

After successful integration:

1. Test your MCP server functionality
2. Implement proper error handling and retry logic
3. Set up monitoring and alerting
4. Configure scaling policies for production use
5. Document your specific implementation details

## Support

For additional help:

- Review AWS Bedrock documentation
- Check the bedrock-agentcore-starter-toolkit GitHub repository
- Contact AWS support for account-specific issues
- Join the MCP community for protocol-related questions