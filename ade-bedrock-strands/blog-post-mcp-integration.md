## Integrating MCP Servers with Amazon Bedrock AgentCore

## The Opportunity

Organizations building intelligent applications can integrate Model Context Protocol (MCP) servers with Amazon Bedrock AgentCore to create end-to-end agentic solutions. AgentCore enables seamless connection of MCP servers that provide specialized context and capabilities within agentic workflows.

Different integration scenarios exist based on current infrastructure:

- **New agentic solutions**: Building MCP servers as part of comprehensive agent workflows
- **Existing MCP capabilities**: Connecting current MCP servers to agentic applications
- **Enterprise agentic systems**: Scaling context-aware agents with authentication and monitoring
- **Flexible agent architecture**: Supporting different deployment patterns for agentic solutions

## Integration Approach

Two integration patterns enable incorporation of MCP servers into agentic solutions through Amazon Bedrock AgentCore. Each pattern supports different agentic application architectures and deployment requirements.

## Integration Patterns

Organizations can deploy MCP servers using two patterns:

### Pattern 1: Direct Deployment
Deploy MCP servers directly to AWS Lambda via AgentCore.

**Use cases:**

- New MCP server development
- Maximum performance requirements
- AWS-native deployments
- Auto-scaling workloads

### Pattern 2: Gateway Integration
Connect existing MCP servers through a proxy gateway.

**Use cases:**

- Existing MCP server infrastructure
- Gradual cloud migration
- Adding AWS authentication to current solutions
- Internal MCP services integration

## Implementation Examples

### Direct Deployment
Deploy a new MCP server to AWS Lambda:

```bash
cd examples/direct-deployment
chmod +x setup_cognito.sh && source setup_cognito.sh
agentcore configure -e mcp_server.py --protocol MCP --authorizer-config "$(cat ../../authorizer_config.json)" --region us-east-1
agentcore launch
```

Result: MCP server runs as AWS Lambda with auto-scaling and CloudWatch monitoring.

### Gateway Integration
Connect existing MCP server infrastructure:

```bash
cd examples/gateway-integration
./setup_gateway.sh  # Configure target MCP server URL
./deploy_gateway.sh
```

Result: Gateway proxy adds AWS authentication and monitoring to existing MCP servers.

## Technical Features

### Security
- OAuth2 authentication with AWS Cognito
- IAM role-based access control
- CloudWatch logging and monitoring
- No hardcoded credentials

### Architecture
- Pattern-based organization
- Automated deployment scripts
- Comprehensive test suites

### Validation
- Direct Deployment: 5/5 integration tests pass
- Gateway Integration: 8/8 proxy tests pass
- AWS deployment verified
- Authentication and monitoring confirmed

## Quick Start

### Direct Deployment
```bash
git clone https://github.com/Nadanne1/GenAIPOC.git
cd GenAIPOC/tools/mcp-integration/examples/direct-deployment
pip install -r ../../requirements.txt
chmod +x setup_cognito.sh && source setup_cognito.sh
agentcore configure -e mcp_server.py --protocol MCP --authorizer-config "$(cat ../../authorizer_config.json)" --region us-east-1
agentcore launch
```

### Gateway Integration
```bash
cd GenAIPOC/tools/mcp-integration/examples/gateway-integration
./setup_gateway.sh  # Configure target MCP server URL
./deploy_gateway.sh
```

## Benefits

### Development
- Reduces AWS integration development time
- Proven deployment patterns
- Focus on core MCP functionality

### Operations
- Enterprise security configurations
- AWS infrastructure integration
- CloudWatch monitoring and logging

### Deployment
- Support for new and existing MCP servers
- Flexible integration options

## Architecture

### Direct Deployment
```
Application → Bedrock AgentCore → MCP Server (Lambda)
```

### Gateway Integration
```
Application → Bedrock AgentCore → Gateway (Lambda) → Existing MCP Server
```

### Components

- **FastMCP:** AWS Lambda-optimized MCP implementation
- **Cognito:** OAuth2 authentication and token management
- **CloudWatch:** Logging and monitoring integration
- **Lambda:** Auto-scaling execution environment

## Repository Contents

### Integration Patterns
- Two working integration patterns with examples
- Automated setup and deployment scripts
- Test suites for validation
- Pattern-specific documentation

### Tools
- Structure verification scripts
- Automated testing frameworks
- Troubleshooting documentation
- Security and operational guidance

## Implementation Steps

1. **Evaluate** integration requirements and choose pattern
2. **Clone** repository and run verification scripts
3. **Test** using comprehensive test suites (end-to-end, Lambda, demo)
4. **Customize** examples for specific MCP functionality
5. **Deploy** using automated scripts
6. **Validate** with production test scenarios
7. **Monitor** and scale with AWS native tools

## Testing Your Implementation

The repository includes comprehensive test suites to validate your MCP integration at multiple levels:

### End-to-End Testing
```bash
# Test complete agent workflow with both RAG and MCP
python test_agentcore_runtime_end_to_end.py
```

**Tests include:**
- RAG queries using local knowledge base
- AWS documentation queries via MCP Gateway
- Multi-agent coordination scenarios
- Performance and response quality validation

### Lambda MCP Server Testing
```bash
# Test Lambda MCP server directly
python test_mcp_lambda.py

# Test agent integration with Lambda MCP
python test_agent_with_lambda_mcp.py
```

**Validates:**
- MCP protocol compliance (initialize, tools/list, tools/call)
- AWS documentation search functionality
- Error handling and authentication
- Response quality for incident response scenarios

### Quick Demo Testing
```bash
# Run interactive demo tests
python test_demo.py
```

**Features:**
- Real-time agent invocation testing
- Response time measurement
- Structured output validation
- Interactive prompt testing

### Test Results Validation

The test suites provide detailed metrics:
- **Direct Deployment**: 5/5 integration tests passing
- **Gateway Integration**: 8/8 proxy tests passing
- **End-to-End Scenarios**: Multi-agent coordination verified
- **Performance**: Sub-60 second response times
- **Security**: Authentication and authorization confirmed

### Troubleshooting

Common test scenarios and solutions:
- **401 Authentication**: Confirms gateway security is working
- **Connection timeouts**: Validates auto-scaling behavior
- **Tool availability**: Verifies MCP server deployment
- **Response quality**: Ensures knowledge integration

## Repository

**Location:** [GenAIPOC/tools/mcp-integration](https://github.com/Nadanne1/GenAIPOC/tree/main/tools/mcp-integration)