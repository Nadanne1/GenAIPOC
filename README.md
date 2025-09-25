# MCP Server Integration Toolkit

A comprehensive toolkit for integrating Model Context Protocol (MCP) servers with Amazon Bedrock AgentCore. This repository provides step-by-step guides, working examples, and automation scripts to help developers quickly deploy and connect MCP servers.

## What's Included

### 📚 Complete Integration Guide
- **CLI-based Deployment**: Quick setup using the AgentCore CLI
- **SDK-based Integration**: Advanced programmatic integration using Python SDKs
- **Authentication Methods**: Cognito OAuth2 and API key authentication
- **Best Practices**: Security, monitoring, and production deployment guidelines

### 🛠️ Working Examples
- **Simple MCP Server**: Example server with echo, timestamp, and calculator tools
- **Client Implementation**: Complete client with error handling and authentication
- **Resource Management**: Examples of MCP resource handling

### 🚀 Automation Scripts
- **Deployment Script**: Automated deployment with prerequisites checking
- **Testing Tools**: Built-in validation and testing capabilities
- **Environment Setup**: Streamlined development environment configuration

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nadanne1/GenAIPOC.git
   cd GenAIPOC
   ```

2. **Navigate to the MCP integration toolkit**
   ```bash
   cd tools/mcp-integration
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Follow the integration guide**
   - Read the [complete guide](tools/mcp-integration/README.md)
   - Try the [example server](tools/mcp-integration/examples/simple_mcp_server.py)
   - Use the [deployment script](tools/mcp-integration/scripts/deploy.sh)

## Repository Structure

```
tools/mcp-integration/
├── README.md                    # Complete integration guide
├── examples/
│   ├── simple_mcp_server.py    # Example MCP server implementation
│   └── client_example.py       # Example client for testing
├── scripts/
│   └── deploy.sh               # Automated deployment script
└── requirements.txt            # Python dependencies
```

## Features

- ✅ **Two Integration Approaches**: Choose between CLI simplicity or SDK flexibility
- ✅ **Complete Documentation**: Step-by-step instructions with troubleshooting
- ✅ **Working Code Examples**: Ready-to-run Python implementations
- ✅ **Automated Deployment**: One-command deployment with error handling
- ✅ **Authentication Support**: Multiple authentication methods supported
- ✅ **Production Ready**: Best practices for security and monitoring

## Prerequisites

- **AWS Account**: With appropriate permissions for IAM roles, Lambda functions, and Cognito resources
- **AWS Credentials**: Configured on your development environment
- **Python**: Version 3.10 or higher (3.6+ for SDK approach)
- **Required Packages**: Listed in requirements.txt

## Integration Options

### Option 1: CLI-based Deployment (Recommended for Quick Setup)
Perfect for rapid prototyping and simple deployments using the AgentCore CLI.

### Option 2: SDK-based Integration (Advanced)
Provides full control and customization options using Python SDKs for production systems.

## Getting Started

1. **Read the Guide**: Start with the [comprehensive integration guide](tools/mcp-integration/README.md)
2. **Try Examples**: Run the example MCP server and client
3. **Deploy**: Use the automated deployment script
4. **Customize**: Adapt the examples for your specific use case

## Example Usage

### Deploy an MCP Server
```bash
cd tools/mcp-integration
./scripts/deploy.sh deploy
```

### Connect to Existing MCP Server
```bash
cd tools/mcp-integration
./scripts/deploy.sh gateway http://your-mcp-server-url
```

### Test Your Deployment
```bash
export BEARER_TOKEN="your_token_here"
./scripts/deploy.sh test
```

## Documentation

- **[Complete Integration Guide](tools/mcp-integration/README.md)**: Detailed instructions for both approaches
- **[Example Server](tools/mcp-integration/examples/simple_mcp_server.py)**: Working MCP server implementation
- **[Client Example](tools/mcp-integration/examples/client_example.py)**: Complete client with authentication
- **[Deployment Script](tools/mcp-integration/scripts/deploy.sh)**: Automated deployment tool

## Support

For help with MCP integration:

- **Integration Issues**: Check the [troubleshooting section](tools/mcp-integration/README.md#troubleshooting)
- **AWS Bedrock**: Review AWS Bedrock documentation
- **MCP Protocol**: Join the MCP community for protocol-related questions
- **Repository Issues**: Create an issue in this repository

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see the LICENSE file for details.

## Additional Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Amazon Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)