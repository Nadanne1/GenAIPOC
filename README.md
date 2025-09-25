# AWS Blog Writing AI Agent

An intelligent content generation system that analyzes existing AWS blogs, learns from their patterns and styles, and generates high-quality technical blog content using AWS Bedrock and Claude Sonnet 4.

## Features

- **GitHub Repository Analysis**: Automatically analyzes GitHub repositories to understand solutions and generate relevant blog content
- **AWS Bedrock Integration**: Leverages Claude Sonnet 4 for intelligent content generation and analysis
- **MCP Integration**: Connects with AWS MCP server for accurate technical information and architecture diagrams
- **Quality Control**: Comprehensive validation for technical accuracy, style compliance, and content quality
- **Multi-stage Review System**: Structured review workflow with feedback incorporation
- **Microservices Architecture**: Scalable, containerized services with Docker and Kubernetes support

## Architecture

The system follows a microservices architecture with the following components:

- **API Gateway**: Central entry point with authentication, rate limiting, and request routing
- **Blog Analyzer Service**: Analyzes existing AWS blogs to extract patterns and styles
- **Content Generator Service**: Generates blog content using Claude Sonnet 4 and learned patterns
- **MCP Connector Service**: Integrates with AWS MCP server for technical validation
- **Quality Control Service**: Validates content quality and technical accuracy
- **Review System Service**: Manages multi-stage review workflows
- **Bedrock Service**: Handles all AWS Bedrock and Claude Sonnet 4 interactions

## Prerequisites

- Node.js 18+
- Docker and Docker Compose
- AWS Account with Bedrock access
- PostgreSQL 15+
- Redis 7+
- ClickHouse (for analytics)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd aws-blog-writing-ai-agent
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS credentials and configuration
   ```

3. **Start the services with Docker Compose**
   ```bash
   npm run dev
   ```

4. **Access the API**
   - API Gateway: http://localhost:3000
   - Swagger Documentation: http://localhost:3000/api-docs
   - Health Check: http://localhost:3000/health

## Configuration

### AWS Bedrock Setup

1. Ensure you have access to Claude Sonnet 4 in AWS Bedrock
2. Configure your AWS credentials in the `.env` file
3. Set the appropriate AWS region where Bedrock is available

### Required Environment Variables

```bash
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# Database URLs
POSTGRES_URL=postgresql://postgres:password@localhost:5432/aws_blog_agent
REDIS_URL=redis://localhost:6379

# Bedrock Configuration
BEDROCK_MAX_TOKENS=4096
BEDROCK_TEMPERATURE=0.7
```

## API Endpoints

### Content Generation
- `POST /api/content/generate` - Generate blog content from requirements
- `POST /api/content/generate-from-repo` - Generate content from GitHub repository
- `GET /api/content/:id` - Retrieve generated content

### Blog Analysis
- `POST /api/analysis/analyze-blog` - Analyze existing blog
- `GET /api/analysis/patterns` - Get extracted content patterns
- `POST /api/analysis/analyze-repository` - Analyze GitHub repository

### Quality Control
- `POST /api/quality/validate` - Validate content quality
- `POST /api/quality/check-technical` - Check technical accuracy
- `POST /api/quality/check-style` - Validate writing style

### Review System
- `POST /api/review/initiate` - Start review process
- `POST /api/review/:id/feedback` - Submit review feedback
- `GET /api/review/:id/status` - Get review status

## Development

### Running Individual Services

Each service can be run independently for development:

```bash
# Bedrock Service
cd services/bedrock-service
npm install
npm run dev

# Content Generator
cd services/content-generator
npm install
npm run dev
```

### Running Tests

```bash
# Run all tests
npm test

# Run tests for specific service
cd services/bedrock-service
npm test
```

### Building for Production

```bash
# Build all services
npm run build

# Build specific service
cd services/bedrock-service
npm run build
```

## Deployment

### Docker Deployment

```bash
# Build and start all services
docker-compose up --build

# Scale specific services
docker-compose up --scale content-generator=3
```

### Kubernetes Deployment

Kubernetes manifests are available in the `k8s/` directory:

```bash
kubectl apply -f k8s/
```

## Monitoring and Observability

The system includes comprehensive monitoring:

- **Metrics**: Prometheus metrics for all services
- **Logging**: Structured logging with Winston
- **Tracing**: Distributed tracing with Jaeger
- **Health Checks**: Built-in health check endpoints
- **Analytics**: ClickHouse for performance analytics

## Usage Examples

### Generate Content from GitHub Repository

```bash
curl -X POST http://localhost:3000/api/content/generate-from-repo \
  -H "Content-Type: application/json" \
  -d '{
    "repositoryUrl": "https://github.com/aws-samples/serverless-webapp",
    "requirements": {
      "topic": "Building Serverless Web Applications",
      "targetAudience": "developer",
      "awsServices": ["Lambda", "API Gateway", "DynamoDB"],
      "contentType": "tutorial"
    }
  }'
```

### Validate Content Quality

```bash
curl -X POST http://localhost:3000/api/quality/validate \
  -H "Content-Type: application/json" \
  -d '{
    "contentId": "content-123"
  }'
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Security

- All services use JWT authentication
- Data encryption at rest and in transit
- AWS IAM integration for secure access
- Rate limiting and input validation
- Security headers with Helmet.js

## Performance

- Redis caching for frequently accessed data
- Connection pooling for databases
- Horizontal scaling support
- Optimized Bedrock token usage
- Async processing for long-running operations

## Troubleshooting

### Common Issues

1. **Bedrock Access Denied**
   - Ensure your AWS credentials have Bedrock permissions
   - Check if Claude Sonnet 4 is available in your region

2. **Database Connection Issues**
   - Verify PostgreSQL is running and accessible
   - Check connection string format

3. **Service Communication Errors**
   - Ensure all services are running
   - Check Docker network configuration

### Logs

View service logs:
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f bedrock-service
```

## Tools and Utilities

### MCP Integration Guide

For integrating Model Context Protocol (MCP) servers with Amazon Bedrock AgentCore, see the comprehensive guide in [`tools/mcp-integration/`](tools/mcp-integration/README.md).

The guide includes:
- Step-by-step integration instructions
- CLI and SDK-based approaches
- Complete code examples
- Deployment scripts
- Troubleshooting tips

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation at `/api-docs`