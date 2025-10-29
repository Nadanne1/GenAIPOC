"""
Financial Market Analyst Agent for Amazon Bedrock AgentCore Runtime
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime, timezone
from strands import Agent
import strands
import boto3
import os

app = FastAPI(title="Financial Market Analyst Agent", version="1.0.0")

# Configuration from environment variables
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
BEDROCK_MODEL_ID = os.getenv('BEDROCK_MODEL_ID', 'us.anthropic.claude-sonnet-4-20250514-v1:0')
BEDROCK_KB_ID = os.getenv('BEDROCK_KB_ID')

# Define the Knowledge Base search tool
@strands.tool
def search_knowledge_base(query: str, max_results: int = 5) -> dict:
    """
    Search the Bedrock Knowledge Base for relevant information about Federal Reserve credit card banking.
    
    Use this tool to find:
    - Interest rate trends and data
    - Market conditions and analysis
    - Policy impacts and regulatory information
    - Financial metrics and statistics
    - Historical comparisons and trends
    
    Args:
        query: Natural language question or search query
        max_results: Maximum number of results to return (default: 5)
    
    Returns:
        Relevant passages from the Federal Reserve report with context
    """
    if not BEDROCK_KB_ID:
        return {'error': 'Knowledge base not configured. Please set BEDROCK_KB_ID environment variable.'}
    
    try:
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
        
        results = []
        for item in response.get('retrievalResults', []):
            results.append({
                'content': item.get('content', {}).get('text', ''),
                'score': item.get('score', 0),
                'location': item.get('location', {})
            })
        
        return {
            'query': query,
            'results_count': len(results),
            'results': results
        }
    
    except Exception as e:
        return {
            'error': f'Knowledge base search failed: {str(e)}',
            'query': query
        }

# Initialize Strands agent
strands_agent = Agent(
    model=BEDROCK_MODEL_ID,
    name="Financial Market Analyst",
    description="Expert agent for analyzing Federal Reserve credit card banking reports",
    system_prompt="""
You are a Financial Market Analyst specializing in credit card banking and Federal Reserve reports.

When responding:
- If a question is ambiguous, ask clarifying questions before providing analysis
- If you need specific parameters (time periods, metrics, segments), ask the user to specify
- Use your tools to gather data, then provide clear, data-driven insights
- Be conversational and interactive

You have access to a knowledge base with Federal Reserve credit card banking reports.
Provide clear, data-driven insights backed by the available financial data.
""",
    tools=[search_knowledge_base]
)

class InvocationRequest(BaseModel):
    input: Dict[str, Any]

class InvocationResponse(BaseModel):
    output: Dict[str, Any]

@app.post("/invocations", response_model=InvocationResponse)
async def invoke_agent(request: InvocationRequest):
    """
    Main invocation endpoint for the Financial Market Analyst Agent.
    
    Expected input format:
    {
        "input": {
            "prompt": "Your question about Federal Reserve credit card banking"
        }
    }
    """
    try:
        user_message = request.input.get("prompt", "")
        if not user_message:
            raise HTTPException(
                status_code=400,
                detail="No prompt found in input. Please provide a 'prompt' key in the input."
            )

        # Invoke the Strands agent
        result = strands_agent(user_message)
        
        response = {
            "message": result.message,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "model": BEDROCK_MODEL_ID,
            "agent": "Financial Market Analyst"
        }

        return InvocationResponse(output=response)

    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Agent processing failed: {str(e)}"
        )

@app.get("/ping")
async def ping():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "agent": "Financial Market Analyst",
        "model": BEDROCK_MODEL_ID,
        "kb_configured": bool(BEDROCK_KB_ID)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
