# Multi-Agent RAG System with AWS Bedrock AgentCore

| Information         | Details                                                                      |
|---------------------|------------------------------------------------------------------------------|
| Agent type          | Synchronous Workflow                                                        |
| Agentic Framework   | LlamaIndex Workflow                                                         |
| LLM model           | AWS Bedrock Claude Sonnet 4                                                 |
| Components          | 4 Specialized Agents (Planner, Researcher, Verifier, Presenter)            |
| Example complexity  | Advanced                                                                    |
| SDK used            | Amazon BedrockAgentCore Python SDK                                          |

This example demonstrates a production-ready multi-agent system using LlamaIndex Workflow, deployed on AWS Bedrock AgentCore. The system features 4 specialized agents that coordinate to answer complex questions using RAG (Retrieval-Augmented Generation) with local knowledge bases.

## Architecture

The system uses a multi-agent workflow with specialized roles:

```
User Question
    ↓
📋 Planner Agent (breaks down question into sub-tasks)
    ↓
🔍 Researcher Agent (retrieves information from knowledge base)
    ↓
✓ Verifier Agent (validates completeness and accuracy)
    ↓
📝 Presenter Agent (synthesizes final response)
    ↓
Structured Response
```

## Prerequisites

- Python 3.12+
- AWS CLI configured with credentials
- AWS account with Bedrock access (Claude Sonnet 4 and Titan Embeddings)
- [AgentCore CLI](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-core.html) installed

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure AWS Credentials

Ensure your AWS CLI is configured with credentials that have access to Bedrock:

```bash
aws configure
# Enter your AWS Access Key ID, Secret Access Key, and region
```

### 3. Update Configuration

Copy the template configuration and update with your AWS account ID:

```bash
cp .bedrock_agentcore.yaml.template .bedrock_agentcore.yaml
```

Edit `.bedrock_agentcore.yaml` and replace `YOUR_AWS_ACCOUNT_ID` with your actual AWS account ID.

### 4. Understanding the Agent Code

The system consists of two main files:

**`agentcore_runtime/agentcore_entry_workflow.py`** - AgentCore entry point that:
- Receives requests from AgentCore
- Initializes the multi-agent workflow
- Returns structured responses

**`agentcore_runtime/notebook_agent_workflow.py`** - Multi-agent workflow with:
- **Planner Agent**: Breaks down complex questions into sub-tasks
- **Researcher Agent**: Retrieves information from the RAG knowledge base
- **Verifier Agent**: Validates response completeness and accuracy
- **Presenter Agent**: Synthesizes the final structured response

The knowledge base is stored in the `data/` directory with security runbooks and incident response procedures.

## Deployment Steps

### 1. Deploy to AWS Bedrock AgentCore

```bash
agentcore launch
```

This command will:
- Build the Docker container with your agent code
- Push it to Amazon ECR
- Deploy to AWS Bedrock AgentCore
- Set up auto-scaling and monitoring
- Return the agent endpoint URL

### 2. Check Deployment Status

```bash
agentcore status
```

This shows:
- Deployment state (ACTIVE, UPDATING, etc.)
- Agent endpoint URL
- Resource utilization
- Recent invocations

### 3. Test the Deployed Agent

```bash
agentcore invoke '{"prompt": "What steps should I take if I detect a brute force attack on my AWS account?"}'
```

Expected response includes:
- Structured answer from all 4 agents
- Citations from the knowledge base
- Verification status
- Response time metrics

### 4. Monitor and Debug

View CloudWatch logs:

```bash
agentcore logs
```

Or access logs directly in AWS Console:
- CloudWatch Logs → `/aws/bedrock/agentcore/your-agent-name`

## Local Testing (Optional)

Before deploying to AWS, you can test locally:

```bash
# Run locally
python -m agentcore_runtime

# In another terminal, test with a sample query
curl -X POST http://localhost:8000/invoke \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What are the steps for incident response?"}'
```

## How It Works

### Multi-Agent Coordination

1. **Planner Agent** receives the user question and creates a structured plan with sub-tasks
2. **Researcher Agent** executes each sub-task by querying the RAG knowledge base
3. **Verifier Agent** checks if all sub-tasks are answered and validates accuracy
4. **Presenter Agent** synthesizes all information into a coherent final response

### RAG Knowledge Base

The system uses LlamaIndex to:
- Embed documents from the `data/` directory using AWS Titan Embeddings
- Store vectors in a local index
- Retrieve relevant context for each query
- Provide citations for all information

### AWS Bedrock Integration

The agent uses:
- **Claude Sonnet 4** for reasoning and response generation
- **Titan Embeddings** for document vectorization
- **AgentCore** for deployment, scaling, and monitoring
- **CloudWatch** for logging and observability

## Project Structure

```
agentcore-samples/
├── agentcore_runtime/
│   ├── __init__.py
│   ├── __main__.py
│   ├── agentcore_entry_workflow.py    # AgentCore entry point
│   └── notebook_agent_workflow.py     # Multi-agent workflow
├── data/                               # Knowledge base
│   ├── iam_forensics.md
│   ├── incident_response_bruteforce.md
│   └── network_isolation.md
├── .bedrock_agentcore.yaml            # AgentCore config (with credentials)
├── .bedrock_agentcore.yaml.template   # Config template
├── Dockerfile                         # Container definition
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Updating the Knowledge Base

To add new documents to the knowledge base:

1. Add markdown files to the `data/` directory
2. Redeploy the agent:
   ```bash
   agentcore launch
   ```

The system will automatically:
- Re-index all documents
- Update the vector store
- Make new information available to queries

## Troubleshooting

### Deployment Issues

**Error: AWS credentials not found**
```bash
aws configure
# Enter your credentials
```

**Error: Bedrock access denied**
- Ensure your IAM role has `bedrock:InvokeModel` permissions
- Check that Claude Sonnet 4 is enabled in your region

**Error: Docker build failed**
- Ensure Docker is running
- Check that all dependencies in `requirements.txt` are valid

### Runtime Issues

**Slow responses**
- First invocation may take longer (cold start)
- Subsequent requests should be faster (~10-20 seconds)

**Empty or incomplete responses**
- Check CloudWatch logs for errors
- Verify knowledge base documents are properly formatted
- Ensure sufficient context in the query

## Additional Resources

- [LlamaIndex Workflow Documentation](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-core.html)
- [Claude Sonnet 4 Model Card](https://docs.anthropic.com/claude/docs/models-overview)
- [AWS Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)