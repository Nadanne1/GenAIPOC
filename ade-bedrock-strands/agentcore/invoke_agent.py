#!/usr/bin/env python3
"""
Invoke Financial Market Analyst Agent on Amazon Bedrock AgentCore Runtime
"""

import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')

# Load agent info
try:
    with open('agent_info.txt', 'r') as f:
        for line in f:
            if line.startswith('AGENT_RUNTIME_ARN='):
                AGENT_RUNTIME_ARN = line.split('=')[1].strip()
            elif line.startswith('AGENT_RUNTIME_ID='):
                AGENT_RUNTIME_ID = line.split('=')[1].strip()
except FileNotFoundError:
    print("❌ agent_info.txt not found. Please run deploy_agent.py first.")
    exit(1)

print(f"Invoking Financial Market Analyst Agent")
print(f"Region: {AWS_REGION}")
print(f"Agent Runtime ARN: {AGENT_RUNTIME_ARN}")
print(f"Agent Runtime ID: {AGENT_RUNTIME_ID}")

# Initialize Bedrock AgentCore client
bedrock_agentcore = boto3.client('bedrock-agentcore', region_name=AWS_REGION)

# Example queries
queries = [
    "What are the key findings in the Federal Reserve credit card banking report?",
    "What are the current interest rate trends?",
    "What policy implications are discussed in the report?"
]

print(f"\n{'='*70}")
print(f"Testing Agent with Sample Queries")
print(f"{'='*70}\n")

for i, query in enumerate(queries, 1):
    print(f"\nQuery {i}: {query}")
    print(f"-" * 70)
    
    try:
        # Prepare payload
        payload = json.dumps({
            "input": {
                "prompt": query
            }
        })
        
        response = bedrock_agentcore.invoke_agent_runtime(
            agentRuntimeArn=AGENT_RUNTIME_ARN,
            payload=payload.encode('utf-8'),
            contentType='application/json',
            accept='application/json'
        )
        
        # Parse response - the body is in 'response' field
        response_body = response['response'].read().decode('utf-8')
        result = json.loads(response_body)
        
        print(f"\nResponse:")
        if 'output' in result:
            output = result['output']
            if isinstance(output, dict):
                if 'message' in output:
                    print(f"  {output['message']}")
                elif 'content' in output:
                    # Handle Claude response format
                    for item in output['content']:
                        if 'text' in item:
                            print(f"  {item['text']}")
                else:
                    print(f"  {json.dumps(output, indent=2)}")
            else:
                print(f"  {output}")
        else:
            print(f"  {json.dumps(result, indent=2)}")
        
    except Exception as e:
        print(f"\n❌ Invocation failed: {e}")

print(f"\n{'='*70}")
print(f"Interactive Mode")
print(f"{'='*70}\n")
print(f"Type your questions (or 'exit' to quit):\n")

# Interactive mode
while True:
    try:
        user_query = input("\n🧑 You: ").strip()
        
        if not user_query or user_query.lower() in ['exit', 'quit', 'bye']:
            print("\n👋 Goodbye!")
            break
        
        payload = json.dumps({
            "input": {
                "prompt": user_query
            }
        })
        
        response = bedrock_agentcore.invoke_agent_runtime(
            agentRuntimeArn=AGENT_RUNTIME_ARN,
            payload=payload.encode('utf-8'),
            contentType='application/json',
            accept='application/json'
        )
        
        response_body = response['response'].read().decode('utf-8')
        result = json.loads(response_body)
        
        if 'output' in result:
            output = result['output']
            if isinstance(output, dict):
                if 'message' in output:
                    print(f"\n🤖 Agent: {output['message']}")
                elif 'content' in output:
                    # Handle Claude response format
                    for item in output['content']:
                        if 'text' in item:
                            print(f"\n🤖 Agent: {item['text']}")
                else:
                    print(f"\n🤖 Agent: {json.dumps(output, indent=2)}")
            else:
                print(f"\n🤖 Agent: {output}")
        else:
            print(f"\n🤖 Agent: {json.dumps(result, indent=2)}")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
