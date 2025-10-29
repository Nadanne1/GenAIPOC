# Quick Start Guide

Get started with the Financial Market Analyst Agent in 5 minutes.

## Prerequisites

- AWS Account with Bedrock access
- Python 3.11+
- AWS CLI configured

## Local Development (Fastest)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your AWS credentials and Bedrock KB ID
```

### 3. Run the Agent

**Option A: Jupyter Notebook**
```bash
jupyter notebook financial_analyst_agent.ipynb
```

**Option B: Python Script**
```bash
python run_agent.py
```

## Deploy to AgentCore (Production)

### Option A: Automatic Deployment (Recommended)

Using the AWS Bedrock AgentCore starter toolkit:

```bash
# Install toolkit
pip install bedrock-agentcore-starter-toolkit

# Configure
cd agentcore
cp .env.example .env
# Edit .env with your BEDROCK_KB_ID

# Deploy (creates everything automatically)
agentcore configure -e agent.py
agentcore launch

# Test
agentcore invoke '{"input": {"prompt": "What is the average interest rate?"}}'
```

### Option B: Manual Deployment (Advanced)

For full control over the deployment:

```bash
cd agentcore
cp .env.example .env
# Edit .env with your AWS_ACCOUNT_ID and BEDROCK_KB_ID

# Create IAM role
python3 create_correct_role.py

# Setup ECR and build
./setup_ecr.sh
./build_and_push.sh

# Deploy to AgentCore
./deploy_cli.sh

# Test
python3 invoke_agent.py
```

## Example Query

```python
"What is the average credit card interest rate mentioned in the Federal Reserve report?"
```

**Expected Response**: The agent will search the Knowledge Base and provide a detailed answer with data from the report.

## Next Steps

- Read the full [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- Customize the agent in `agentcore/agent.py`
- Add more documents to your Knowledge Base
- Set up monitoring in CloudWatch

## Need Help?

Check the [Troubleshooting](DEPLOYMENT_GUIDE.md#troubleshooting) section in the deployment guide.
