# Financial Market Analyst Agent - AgentCore Deployment

Deploy the Financial Market Analyst Agent to Amazon Bedrock AgentCore Runtime.

> **📖 For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md)**

## Prerequisites

- AWS Account with Bedrock AgentCore access
- Docker or Finch installed
- AWS CLI configured
- Python 3.11+
- ECR repository created

## Project Structure

```
agentcore/
├── agent.py              # FastAPI agent implementation
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container image definition
├── deploy_agent.py      # Deployment script
├── invoke_agent.py      # Invocation script
└── README.md           # This file
```

## Deployment Options

### Option 1: Automatic Deployment (Recommended)

Use the AWS Bedrock AgentCore starter toolkit for the easiest deployment experience.

#### Prerequisites

```bash
pip install bedrock-agentcore-starter-toolkit
```

#### Step 1: Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your configuration
# Required: BEDROCK_KB_ID, AWS_REGION (optional, defaults to us-west-2)
```

#### Step 2: Configure Agent

The toolkit automatically creates IAM roles, ECR repository, and builds the container.

```bash
# Configure with default settings (us-west-2)
agentcore configure -e agent.py

# Or specify a different region
agentcore configure -e agent.py -r us-east-1
```

#### Step 3: Deploy to AgentCore

```bash
# Deploy to AWS (creates all resources automatically)
agentcore launch
```

This command:
- Creates IAM execution role with correct permissions
- Builds ARM64 container image
- Creates and pushes to ECR repository
- Deploys to AgentCore Runtime
- Returns agent ARN and logs location

**Note the Agent ARN** from the output.

#### Step 4: Test the Agent

```bash
# Test using the toolkit
agentcore invoke '{"input": {"prompt": "What are the key findings?"}}'

# Or use the Python script
python invoke_agent.py
```

#### Step 5: Monitor and Debug

View logs in CloudWatch:
```
CloudWatch → Log groups → /aws/bedrock-agentcore/runtimes/{agent-id}-DEFAULT
```

#### Clean Up

```bash
# Remove all AWS resources
agentcore destroy
```

### Option 2: Manual Deployment (Advanced)

For users who want full control over the deployment process.

#### Step 1: Setup ECR Repository

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your AWS account details
# Update: AWS_ACCOUNT_ID, AWS_REGION, BEDROCK_KB_ID

# Create ECR repository
./setup_ecr.sh
```

#### Step 2: Create IAM Role

```bash
# Creates role with correct service principal and permissions
python3 create_correct_role.py
```

#### Step 3: Build and Push Docker Image

```bash
# Build and push to ECR (automated script)
./build_and_push.sh
```

This script will:
- Setup Docker buildx for ARM64
- Login to ECR
- Build the image for linux/arm64
- Push to ECR with latest tag

#### Step 4: Deploy to AgentCore

```bash
# Deploy using AWS CLI
./deploy_cli.sh
```

This will:
- Create the AgentCore Runtime
- Configure environment variables
- Save agent info to `agent_info.txt`

#### Step 5: Invoke the Agent

```bash
python invoke_agent.py
```

This will:
- Run sample queries
- Start interactive mode for custom questions

## Testing Locally (Optional)

Test the agent locally before deploying:

```bash
# Build local image
docker build -t financial-analyst-agent:local .

# Run locally
docker run -p 8080:8080 \
  -e AWS_REGION=us-west-2 \
  -e BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0 \
  -e BEDROCK_KB_ID=YOUR_KNOWLEDGE_BASE_ID \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
  financial-analyst-agent:local

# Test health endpoint
curl http://localhost:8080/ping

# Test invocation
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"input": {"prompt": "What are the key findings in the report?"}}'
```

## Observability

The agent includes AWS OpenTelemetry auto-instrumentation for:
- Distributed tracing
- Metrics collection
- CloudWatch integration

View metrics in:
- CloudWatch Console → GenAI Observability
- CloudWatch Application Signals → Transaction Search

## Troubleshooting

### Build Issues

```bash
# Check Docker buildx
docker buildx ls

# Verify ARM64 support
docker buildx inspect agentcore-builder
```

### Deployment Issues

```bash
# Check agent status
aws bedrock-agentcore-runtime describe-agent-runtime \
  --agent-runtime-id <AGENT_RUNTIME_ID> \
  --region us-west-2

# View logs
aws logs tail /aws/bedrock-agentcore/<AGENT_RUNTIME_ID> --follow
```

### Invocation Issues

- Verify agent status is ACTIVE
- Check AWS credentials are valid
- Ensure Knowledge Base ID is correct
- Review CloudWatch logs for errors

## Architecture

```
User Query
    ↓
AgentCore Runtime (Serverless)
    ↓
FastAPI Agent (Container)
    ↓
Strands Agent Framework
    ↓
Claude Sonnet 4 (Bedrock)
    ↓
Knowledge Base Search Tool
    ↓
Bedrock Knowledge Base
```

## Features

- **Serverless**: Auto-scaling, pay-per-use
- **Secure**: Session isolation, IAM integration
- **Observable**: Built-in tracing and metrics
- **Conversational**: Maintains context across queries
- **Specialized**: Financial analysis with KB search

## Next Steps

1. Enable CloudWatch Transaction Search for observability
2. Configure session management for multi-turn conversations
3. Add custom authentication/authorization
4. Integrate with your application via API
5. Monitor usage and optimize costs
