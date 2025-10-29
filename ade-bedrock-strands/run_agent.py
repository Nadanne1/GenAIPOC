#!/usr/bin/env python3
"""Financial Market Analyst Agent - Simple Script Version"""

import os
import json
import time
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load configuration
load_dotenv()

LANDINGAI_API_KEY = os.getenv('LANDINGAI_API_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
BEDROCK_MODEL_ID = os.getenv('BEDROCK_MODEL_ID', 'anthropic.claude-sonnet-4-20250514')
BEDROCK_KB_ID = os.getenv('BEDROCK_KB_ID')
PDF_PATH = 'Credit-Card-Banking-Federal-Reserve.pdf'

print("="*70)
print("Financial Market Analyst Agent")
print("="*70)
print(f"\n✓ Configuration loaded")
print(f"  - AWS Region: {AWS_REGION}")
print(f"  - S3 Bucket: {S3_BUCKET_NAME}")
print(f"  - Model: {BEDROCK_MODEL_ID}")

# Step 1: Load extracted document data
print(f"\n{'='*70}")
print(f"Step 1: Loading extracted document data")
print(f"{'='*70}")

# Check for markdown file or JSON file
markdown_file = 'extracted_content.md'
json_file = 'extraction_result.json'

if os.path.exists(markdown_file):
    print(f"Loading from: {markdown_file}")
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    extracted_data = {
        'result': {
            'markdown': markdown_content
        }
    }
    print(f"✓ Loaded {len(markdown_content)} characters of markdown content")
elif os.path.exists(json_file):
    print(f"Loading from: {json_file}")
    with open(json_file, 'r') as f:
        extracted_data = json.load(f)
    print(f"✓ Loaded extraction result")
else:
    raise FileNotFoundError(
        f"Please place either '{markdown_file}' or '{json_file}' in the current directory"
    )

# Step 2: Upload to S3
print(f"\n{'='*70}")
print(f"Step 2: Uploading to S3")
print(f"{'='*70}")

s3_client = boto3.client('s3', region_name=AWS_REGION)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
s3_key = f"financial-reports/fed-credit-card-banking_{timestamp}.json"

s3_client.put_object(
    Bucket=S3_BUCKET_NAME,
    Key=s3_key,
    Body=json.dumps(extracted_data, indent=2),
    ContentType='application/json'
)

s3_uri = f"s3://{S3_BUCKET_NAME}/{s3_key}"
print(f"✓ Data uploaded to: {s3_uri}")

# Step 3: Initialize Strands Agent
print(f"\n{'='*70}")
print(f"Step 3: Initializing Strands Agent")
print(f"{'='*70}")

from strands import Agent
import strands

@strands.tool
def query_financial_data(query: str, data_type: str = "all") -> dict:
    """Query structured financial data from the ADE extracted dataset."""
    return {
        'query': query,
        'data_type': data_type,
        'data': extracted_data
    }

@strands.tool
def search_knowledge_base(query: str, max_results: int = 5) -> dict:
    """Search the Bedrock Knowledge Base for relevant information."""
    if not BEDROCK_KB_ID:
        return {'error': 'Knowledge base not configured'}
    
    bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name=AWS_REGION)
    
    response = bedrock_agent_runtime.retrieve(
        knowledgeBaseId=BEDROCK_KB_ID,
        retrievalQuery={'text': query},
        retrievalConfiguration={
            'vectorSearchConfiguration': {
                'numberOfResults': max_results
            }
        }
    )
    
    return {
        'query': query,
        'results': response.get('retrievalResults', [])
    }

agent = Agent(
    model=BEDROCK_MODEL_ID,
    name="Financial Market Analyst",
    description="Expert agent for analyzing Federal Reserve credit card banking reports",
    system_prompt="""
You are a Financial Market Analyst specializing in credit card banking and Federal Reserve reports.

When responding:
- If a question is ambiguous or lacks necessary details, ask clarifying questions before providing analysis
- If you need specific parameters (time periods, metrics, segments), ask the user to specify
- Use your tools to gather data, then provide clear, data-driven insights
- Be conversational and interactive - this is a dialogue, not a one-way report

You have access to structured data extracted from Federal Reserve credit card banking reports.
Provide clear, data-driven insights backed by the available financial data.
""",
    tools=[query_financial_data, search_knowledge_base]
)

print(f"✓ Agent initialized")
print(f"  - Model: {BEDROCK_MODEL_ID}")
print(f"  - Tools: {len(agent.tool_names)}")

# Step 4: Interactive Chat Loop
print(f"\n{'='*70}")
print(f"Interactive Chat - Financial Market Analyst Agent")
print(f"{'='*70}")
print(f"\nAsk questions about the Federal Reserve credit card banking report.")
print(f"Type 'exit', 'quit', or 'bye' to end the conversation.")
print(f"{'='*70}\n")

while True:
    try:
        user_input = input("\n🧑 You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
            print("\n👋 Ending conversation. Goodbye!")
            break
        
        print("\n🤖 Agent: ", end="")
        result = agent(user_input)
        print(result)
        
    except KeyboardInterrupt:
        print("\n\n👋 Conversation interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please try again or type 'exit' to quit.")
