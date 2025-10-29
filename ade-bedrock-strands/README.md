# Financial Market Analyst Agent

An AI agent that analyzes Federal Reserve credit card banking reports using AWS Bedrock, Claude Sonnet 4, and the Strands framework.

## Features

- 🤖 **Intelligent Analysis** - Uses Claude Sonnet 4 for reasoning and analysis
- 📚 **Knowledge Base Integration** - RAG with Bedrock Knowledge Base for accurate information retrieval
- 💬 **Conversational** - Maintains context and asks clarifying questions
- 🚀 **Serverless Deployment** - Deploy to AWS Bedrock AgentCore for auto-scaling
- 📊 **Observable** - Built-in CloudWatch logs, X-Ray tracing, and metrics
- 🔧 **Flexible** - Run locally in Jupyter or deploy to production

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your AWS credentials

# Run locally
jupyter notebook financial_analyst_agent.ipynb
```

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

## Deployment Options

### 1. Local Development
- Jupyter Notebook for interactive development
- Python script for command-line usage
- Perfect for testing and experimentation

### 2. AWS Bedrock AgentCore (Production)

**Option A: Automatic (Recommended)**
- Uses AWS Bedrock AgentCore starter toolkit
- One-command deployment
- Automatically creates IAM roles, ECR, and container

**Option B: Manual (Advanced)**
- Full control over deployment
- Custom IAM roles and configurations
- Step-by-step deployment scripts

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete deployment instructions.

## Project Structure

```
ade-bedrock-strands/
├── agentcore/                    # AgentCore deployment
│   ├── agent.py                  # FastAPI agent implementation
│   ├── Dockerfile                # Container definition
│   ├── deploy_cli.sh             # Deployment script
│   ├── invoke_agent.py           # Invocation script
│   ├── create_correct_role.py    # IAM role creation
│   └── build_and_push.sh         # Docker build script
├── financial_analyst_agent.ipynb # Jupyter notebook
├── run_agent.py                  # Local Python script
├── requirements.txt              # Python dependencies
├── DEPLOYMENT_GUIDE.md           # Detailed deployment guide
├── QUICKSTART.md                 # Quick start guide
└── README.md                     # This file
```

## Example Usage

```python
# Ask a question
"What is the average credit card interest rate in the Federal Reserve report?"

# Agent response (with KB search)
"Based on the Federal Reserve report, the average credit card interest 
rate is 23% APR in 2023. This represents an 18% spread over the Federal 
funds rate..."
```

## Architecture

```
User Query
    ↓
Strands Agent Framework
    ↓
Claude Sonnet 4 (Reasoning)
    ↓
Knowledge Base Search Tool
    ↓
Bedrock Knowledge Base (RAG)
    ↓
Federal Reserve Reports
```

## Requirements

- Python 3.11+
- AWS Account with Bedrock access
- AWS CLI configured
- Docker (for AgentCore deployment)

## Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Deployment Guide](DEPLOYMENT_GUIDE.md) - Complete deployment instructions
- [AgentCore README](agentcore/README.md) - AgentCore-specific documentation

## Key Technologies

- **AWS Bedrock** - Foundation model hosting
- **Claude Sonnet 4** - Advanced reasoning and analysis
- **Bedrock Knowledge Base** - RAG for document retrieval
- **Strands Framework** - Agent orchestration
- **AgentCore Runtime** - Serverless deployment platform
- **FastAPI** - Web framework for the agent API

## Cost Estimate

### Local Development
- Free (uses your AWS Bedrock quota)

### AgentCore Deployment
- **Compute**: ~$0.10 per hour of active use
- **Bedrock**: ~$3-15 per 1M tokens (depending on usage)
- **Knowledge Base**: ~$0.10 per 1K queries

See [Cost Considerations](DEPLOYMENT_GUIDE.md#cost-considerations) for details.

## Security

- Never commit credentials to version control
- Use IAM roles instead of access keys when possible
- Follow least privilege principle for permissions
- Enable CloudTrail for audit logging

See [Security Best Practices](DEPLOYMENT_GUIDE.md#security-best-practices) for more.

## Troubleshooting

Common issues and solutions are documented in the [Troubleshooting](DEPLOYMENT_GUIDE.md#troubleshooting) section.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Your License Here]

## Support

For questions or issues:
- Check the [Deployment Guide](DEPLOYMENT_GUIDE.md)
- Review [Troubleshooting](DEPLOYMENT_GUIDE.md#troubleshooting)
- Open an issue on GitHub

## Acknowledgments

- Built with [Strands](https://github.com/anthropics/strands) by Anthropic
- Powered by AWS Bedrock and Claude Sonnet 4
- Uses AWS Bedrock AgentCore for deployment
