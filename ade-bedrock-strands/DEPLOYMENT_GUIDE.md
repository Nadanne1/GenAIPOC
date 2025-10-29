# Financial Market Analyst Agent - Deployment Guide

This guide shows you how to deploy a Financial Market Analyst Agent using AWS Bedrock AgentCore and the Strands framework.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Option 1: Local Development (Jupyter Notebook)](#option-1-local-development-jupyter-notebook)
- [Option 2: Deploy to AWS Bedrock AgentCore](#option-2-deploy-to-aws-bedrock-agentcore)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)

## Overview

This project demonstrates how to build an AI agent that analyzes Federal Reserve credit card banking reports using:
- **AWS Bedrock** - Claude Sonnet 4 for reasoning
- **Bedrock Knowledge Base** - RAG for document retrieval
- **Strands Framework** - Agent orchestration
- **AgentCore Runtime** - Serverless deployment

## Prerequisites

### Required
- Python 3.11+
- AWS Account with Bedrock access
- AWS CLI configured
- Docker or Finch (for AgentCore deployment)

### AWS Services Needed
- Amazon Bedrock (Claude Sonnet 4 model access)
- Bedrock Knowledge Base (with your documents)
- ECR (for container images)
- IAM (for role creation)

## Option 1: Local Development (Jupyter Notebook)

Perfect for testing and development before deploying to production.

### 1. Setup Environment

```bash
# Clone or navigate to the project
cd ade-bedrock-strands

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your values
nano .env
```

Required variables:
```bash
AWS_REGION=us-west-2
AWS_ACCOUNT_ID=YOUR_AWS_ACCOUNT_ID
BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
BEDROCK_KB_ID=YOUR_KNOWLEDGE_BASE_ID
```

### 3. Run the Notebook

```bash
# Start Jupyter
jupyter notebook financial_analyst_agent.ipynb
```

The notebook demonstrates:
- Setting up the Strands agent
- Defining the Knowledge Base search tool
- Running queries and analyzing results
- Interactive conversation with the agent

### 4. Run as Python Script (Alternative)

```bash
python run_agent.py
```

## Option 2: Deploy to AWS Bedrock AgentCore

Deploy your agent as a serverless, scalable service on AWS.

### Architecture

```
User Request
    ↓
AWS Bedrock AgentCore Runtime (Serverless)
    ↓
Your Agent Container (ARM64)
    ↓
Strands Agent Framework
    ↓
Claude Sonnet 4 + Knowledge Base
```

### Deployment Method 1: Automatic (Recommended - AWS Starter Toolkit)

The easiest way to deploy using the official AWS Bedrock AgentCore starter toolkit.

#### Prerequisites

```bash
# Install the starter toolkit
pip install bedrock-agentcore-starter-toolkit
```

#### Step 1: Configure Environment

```bash
cd agentcore

# Copy and configure environment
cp .env.example .env
nano .env  # Add your BEDROCK_KB_ID and AWS_REGION
```

#### Step 2: Configure Agent

The toolkit automatically creates IAM roles, ECR repository, and container image.

```bash
# Configure with default settings (us-west-2)
agentcore configure -e agent.py

# Or specify a different region
agentcore configure -e agent.py -r us-east-1
```

#### Step 3: Deploy to AgentCore

```bash
# Deploy to AWS
agentcore launch
```

This command:
- Creates IAM execution role automatically
- Builds ARM64 container image
- Creates ECR repository
- Pushes image to ECR
- Deploys to AgentCore Runtime
- Returns the agent ARN and logs location

**Note the Agent ARN** from the output - you'll need it to invoke the agent.

#### Step 4: Test Deployed Agent

```bash
# Test using the toolkit
agentcore invoke '{"input": {"prompt": "What is the average credit card interest rate?"}}'
```

#### Step 5: View Logs and Monitor

```bash
# View CloudWatch logs
# Location: CloudWatch → Log groups → /aws/bedrock-agentcore/runtimes/{agent-id}-DEFAULT
```

#### Step 6: Clean Up (Optional)

```bash
# Remove all AWS resources created by the toolkit
agentcore destroy
```

### Deployment Method 2: Manual (Advanced Users)

For users who want full control over the deployment process.

#### Step 1: Setup ECR Repository

```bash
cd agentcore

# Copy and configure environment
cp .env.example .env
nano .env  # Add your AWS_ACCOUNT_ID and BEDROCK_KB_ID

# Create ECR repository
./setup_ecr.sh
```

#### Step 2: Create IAM Role

The agent needs an IAM role with the correct permissions and trust policy.

```bash
# This creates a role with the correct service principal
python3 create_correct_role.py
```

This script creates a role with:
- **Trust Policy**: Allows `bedrock-agentcore.amazonaws.com` to assume the role
- **Permissions**: ECR access, Bedrock model invocation, Knowledge Base access, CloudWatch logs

#### Step 3: Build and Push Docker Image

```bash
# Build for ARM64 (required by AgentCore) and push to ECR
./build_and_push.sh
```

This will:
- Setup Docker buildx for ARM64
- Login to ECR
- Build the container image
- Push to ECR with `latest` tag

#### Step 4: Deploy to AgentCore

```bash
# Deploy using AWS CLI
./deploy_cli.sh
```

This creates the AgentCore Runtime with:
- Your container image from ECR
- Environment variables (model ID, KB ID, region)
- IAM role for permissions
- Public network mode

The deployment saves agent info to `agent_info.txt` and `agent_info.json`.

#### Step 5: Invoke the Agent

```bash
# Test the deployed agent
python3 invoke_agent.py
```

This will:
- Run sample queries
- Start interactive mode for custom questions

## Agent Implementation

### Core Components

**`agent.py`** - FastAPI application with:
```python
# Knowledge Base search tool
@strands.tool
def search_knowledge_base(query: str, max_results: int = 5) -> dict:
    """Search Bedrock Knowledge Base for relevant information"""
    # Retrieves documents from your KB
    
# Strands agent with the tool
strands_agent = Agent(
    model=BEDROCK_MODEL_ID,
    name="Financial Market Analyst",
    tools=[search_knowledge_base]
)

# FastAPI endpoint
@app.post("/invocations")
async def invoke_agent(request: InvocationRequest):
    result = strands_agent(user_message)
    return InvocationResponse(output=response)
```

### Key Features

- **Tool Use**: Agent automatically decides when to search the Knowledge Base
- **Conversational**: Maintains context and asks clarifying questions
- **Data-Driven**: Backs answers with citations from the KB
- **Observability**: Built-in CloudWatch logs, X-Ray tracing, and metrics

## Usage Examples

### Example 1: Basic Query

```python
import boto3
import json

client = boto3.client('bedrock-agentcore', region_name='us-west-2')

response = client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:us-west-2:ACCOUNT:runtime/AGENT_ID',
    payload=json.dumps({
        'input': {
            'prompt': 'What is the average credit card interest rate?'
        }
    }).encode(),
    contentType='application/json',
    accept='application/json'
)

result = json.loads(response['response'].read())
print(result['output']['content'][0]['text'])
```

### Example 2: Interactive Session

```bash
python3 invoke_agent.py

# Interactive mode starts
🧑 You: What are the key findings in the Federal Reserve report?
🤖 Agent: [Detailed analysis with data from Knowledge Base]

🧑 You: What about interest rate trends?
🤖 Agent: [Contextual response building on previous answer]
```

### Example 3: Programmatic Use

```python
from strands import Agent
import strands

# Define your tool
@strands.tool
def search_knowledge_base(query: str) -> dict:
    # Your KB search logic
    pass

# Create agent
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    name="Financial Analyst",
    tools=[search_knowledge_base]
)

# Use agent
result = agent("Analyze the credit card market trends")
print(result.message)
```

## Monitoring and Observability

### CloudWatch Logs

```bash
# View agent logs
aws logs tail "/aws/bedrock-agentcore/runtimes/YOUR_AGENT_ID" \
  --region us-west-2 \
  --follow
```

### Check Agent Status

```bash
aws bedrock-agentcore-control get-agent-runtime \
  --agent-runtime-id YOUR_AGENT_ID \
  --region us-west-2
```

### Metrics

View in AWS Console:
- CloudWatch → GenAI Observability
- CloudWatch Application Signals → Transaction Search

## Troubleshooting

### Issue: Role validation failed

**Problem**: `Role validation failed for 'arn:aws:iam::...'`

**Solution**: The IAM role must use the correct service principal:
```json
{
  "Principal": {
    "Service": "bedrock-agentcore.amazonaws.com"
  }
}
```

Use `create_correct_role.py` to create the role with the right configuration.

### Issue: Knowledge Base authentication errors

**Problem**: Agent can't access the Knowledge Base

**Solution**: Ensure the IAM role has these permissions:
```json
{
  "Action": [
    "bedrock:Retrieve",
    "bedrock:RetrieveAndGenerate"
  ],
  "Resource": "arn:aws:bedrock:REGION:ACCOUNT:knowledge-base/KB_ID"
}
```

### Issue: Container fails to start

**Problem**: Agent runtime shows error status

**Solution**: 
1. Check CloudWatch logs for errors
2. Verify environment variables are set correctly
3. Test the container locally first:
```bash
docker build -t test-agent .
docker run -p 8080:8080 \
  -e AWS_REGION=us-west-2 \
  -e BEDROCK_MODEL_ID=... \
  -e BEDROCK_KB_ID=... \
  test-agent
```

### Issue: 500 errors on invocation

**Problem**: Agent returns 500 errors

**Possible causes**:
- Cold start timeout (first request may be slow)
- Bedrock service unavailable
- Invalid model ID or KB ID

**Solution**: Check CloudWatch logs and verify configuration.

## Cost Considerations

### AgentCore Runtime
- Pay only for compute time used
- Auto-scales to zero when not in use
- Charged per GB-second

### Bedrock Costs
- Claude Sonnet 4: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- Knowledge Base: Retrieval charges per query
- Embeddings: One-time cost for indexing

### Optimization Tips
- Use smaller context windows when possible
- Cache frequently accessed KB results
- Monitor usage in AWS Cost Explorer

## Security Best Practices

1. **Never commit credentials** - Use `.env` files (in `.gitignore`)
2. **Use IAM roles** - Avoid long-term access keys
3. **Least privilege** - Grant only required permissions
4. **Enable CloudTrail** - Audit all API calls
5. **Use VPC endpoints** - For private network access (optional)

## Next Steps

1. **Customize the agent** - Modify `agent.py` to add more tools or change behavior
2. **Add more documents** - Upload additional files to your Knowledge Base
3. **Implement authentication** - Add API keys or OAuth for production
4. **Set up CI/CD** - Automate builds and deployments
5. **Monitor costs** - Set up billing alerts

## Additional Resources

- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/)
- [Strands Framework](https://github.com/anthropics/strands)
- [Claude Sonnet 4 Model Card](https://docs.anthropic.com/claude/docs/models-overview)
- [Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review CloudWatch logs for errors
3. Consult AWS Bedrock documentation
4. Check AWS Service Health Dashboard

## License

[Your License Here]
