# Project Structure

```
ade-bedrock-strands/
├── README.md                          # Main documentation
├── QUICKSTART.md                      # 5-minute getting started guide
├── DEPLOYMENT_GUIDE.md                # Comprehensive deployment guide
├── PROJECT_STRUCTURE.md               # This file
├── .gitignore                         # Git ignore rules
├── .env.example                       # Environment template
├── requirements.txt                   # Python dependencies
├── run_agent.py                       # Local Python runner
├── financial_analyst_agent.ipynb      # Jupyter notebook
│
├── Credit-Card-Banking-Federal-Reserve.pdf              # Source document
├── Credit-Card-Banking-Federal-Reserve.extraction.md    # Extracted content
├── Credit-Card-Banking-Federal-Reserve.extraction.json  # Extracted data
├── Consumer-Credit-Europe-Mastercard.pdf                # Additional document
│
└── agentcore/                         # AgentCore deployment
    ├── README.md                      # AgentCore-specific docs
    ├── .env.example                   # Environment template
    ├── agent.py                       # FastAPI agent implementation
    ├── Dockerfile                     # Container definition
    ├── requirements.txt               # Python dependencies
    ├── create_correct_role.py         # IAM role creation script
    ├── setup_ecr.sh                   # ECR repository setup
    ├── build_and_push.sh              # Docker build & push script
    ├── deploy_cli.sh                  # AgentCore deployment script
    └── invoke_agent.py                # Agent invocation script
```

## File Descriptions

### Root Directory

**Documentation**
- `README.md` - Project overview, features, and quick links
- `QUICKSTART.md` - Fast onboarding guide (5 minutes)
- `DEPLOYMENT_GUIDE.md` - Detailed deployment instructions
- `PROJECT_STRUCTURE.md` - This file

**Configuration**
- `.env.example` - Environment variable template (no credentials)
- `.gitignore` - Prevents committing sensitive files
- `requirements.txt` - Python package dependencies

**Local Development**
- `run_agent.py` - Run agent locally via Python script
- `financial_analyst_agent.ipynb` - Interactive Jupyter notebook

**Documents**
- PDF files - Source documents for Knowledge Base
- Extraction files - Pre-processed document content

### agentcore/ Directory

**Core Implementation**
- `agent.py` - FastAPI application with Strands agent
- `Dockerfile` - Container image definition for AgentCore

**Deployment Scripts**
- `create_correct_role.py` - Creates IAM role with correct permissions
- `setup_ecr.sh` - Creates ECR repository
- `build_and_push.sh` - Builds and pushes Docker image
- `deploy_cli.sh` - Deploys to AWS Bedrock AgentCore

**Usage**
- `invoke_agent.py` - Script to invoke deployed agent
- `requirements.txt` - Python dependencies for container

## What's NOT Included (By Design)

These files are excluded for security:
- `.env` - Real AWS credentials (use `.env.example` as template)
- `agent_info.txt` - Deployed agent ARN (generated during deployment)
- `agent_info.json` - Deployment details (generated during deployment)
- `venv/` - Python virtual environment (create locally)
- `__pycache__/` - Python cache files

## Getting Started

1. **Local Development**: See `QUICKSTART.md`
2. **Production Deployment**: See `DEPLOYMENT_GUIDE.md`
3. **AgentCore Deployment**: See `agentcore/README.md`
