# GenAI POC Repository

This repository contains multiple Proof of Concept (POC) projects demonstrating various AI and AWS integrations.

## Projects

### 🤖 MCP Server Integration Toolkit
**Location**: `tools/mcp-integration/`

A comprehensive toolkit for integrating Model Context Protocol (MCP) servers with Amazon Bedrock AgentCore.

**Features:**
- CLI-based and SDK-based deployment approaches
- Working examples with authentication
- Automated deployment scripts
- Complete documentation and troubleshooting guides

**Quick Start:**
```bash
cd tools/mcp-integration
pip install -r requirements.txt
./scripts/deploy.sh deploy
```

[📖 Full Documentation](tools/mcp-integration/README.md)

### 📄 PDF to Markdown Converter
**Location**: `pdf-to-markdown-poc/`

An intelligent PDF to Markdown converter using AWS Bedrock and Claude Sonnet for high-quality document conversion.

**Features:**
- AWS S3 integration for file storage
- Claude Sonnet 4 for intelligent text extraction
- Image extraction and cloud storage
- Structured markdown output with tables
- Batch processing capabilities

**Quick Start:**
```bash
cd pdf-to-markdown-poc
# Follow the setup instructions in the README
```

[📖 Full Documentation](pdf-to-markdown-poc/README.md)

## Repository Structure

```
GenAIPOC/
├── tools/
│   └── mcp-integration/          # MCP Server Integration Toolkit
│       ├── README.md
│       ├── examples/
│       ├── scripts/
│       └── requirements.txt
├── pdf-to-markdown-poc/          # PDF to Markdown Converter
│   ├── README.md
│   ├── pdftomarkdown.ipynb
│   └── LICENSE
├── pdftomarkdown.ipynb           # Legacy PDF converter (deprecated)
└── README.md                     # This file
```

## Getting Started

1. **Choose your project**: Navigate to the specific POC folder
2. **Follow the documentation**: Each project has its own detailed README
3. **Install dependencies**: Each project lists its specific requirements
4. **Run examples**: Try the provided examples and scripts

## Prerequisites

### General Requirements
- AWS Account with appropriate permissions
- AWS CLI configured with credentials
- Python 3.8+ (specific versions noted in each project)

### Project-Specific Requirements
- **MCP Integration**: Python 3.10+, AWS Bedrock access
- **PDF to Markdown**: Python 3.8+, AWS S3 and Bedrock access

## Contributing

1. Fork the repository
2. Create a feature branch for your POC or enhancement
3. Follow the existing project structure
4. Add comprehensive documentation
5. Test thoroughly
6. Submit a pull request

## Project Guidelines

When adding new POCs to this repository:

1. **Create a dedicated folder** with a descriptive name
2. **Include a comprehensive README** with setup instructions
3. **Provide working examples** that can be run immediately
4. **Document prerequisites** and dependencies clearly
5. **Include error handling** and troubleshooting guides
6. **Follow security best practices** for AWS integrations

## License

Each project may have its own license. Check individual project folders for specific licensing information.

- **PDF to Markdown POC**: MIT License
- **MCP Integration Toolkit**: MIT License

## Support

For project-specific issues:
- Check the individual project's README and troubleshooting section
- Create an issue in this repository with the project name in the title
- Review AWS documentation for service-specific questions

## Additional Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude AI Documentation](https://docs.anthropic.com/)