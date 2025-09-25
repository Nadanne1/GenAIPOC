#!/usr/bin/env python3
"""
MCP Client Example
Example client for invoking MCP servers through Amazon Bedrock AgentCore
"""

import os
import requests
import json
import boto3
from botocore.exceptions import ClientError
from typing import Optional, Dict, Any

class MCPAgentCoreClient:
    """Client for invoking MCP servers through Amazon Bedrock AgentCore"""
    
    def __init__(self, agent_arn: str, bearer_token: str, base_url: str = None):
        self.agent_arn = agent_arn
        self.bearer_token = bearer_token
        self.base_url = base_url or "https://agentcore.bedrock.aws.com"
        
    def invoke_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Invoke a tool on the MCP server"""
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        url = f"{self.base_url}/agents/{self.agent_arn}/invoke"
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def list_tools(self) -> Dict[str, Any]:
        """List available tools"""
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "method": "tools/list",
            "params": {}
        }
        
        url = f"{self.base_url}/agents/{self.agent_arn}/invoke"
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def list_resources(self) -> Dict[str, Any]:
        """List available resources"""
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "method": "resources/list",
            "params": {}
        }
        
        url = f"{self.base_url}/agents/{self.agent_arn}/invoke"
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

def get_cognito_token(user_pool_id: str, client_id: str, username: str, password: str) -> Optional[str]:
    """Get bearer token from AWS Cognito"""
    client = boto3.client('cognito-idp')
    
    try:
        response = client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        
        return response['AuthenticationResult']['AccessToken']
    except ClientError as e:
        print(f"Error getting token: {e}")
        return None

def main():
    """Example usage of the MCP AgentCore client"""
    
    # Configuration - replace with your actual values
    agent_arn = os.getenv("AGENT_ARN", "your_agent_runtime_arn")
    bearer_token = os.getenv("BEARER_TOKEN", "your_bearer_token")
    
    # Alternative: Get token from Cognito
    # user_pool_id = "us-east-1_xxxxxxxxx"
    # client_id = "your_client_id"
    # username = "your_username"
    # password = "your_password"
    # bearer_token = get_cognito_token(user_pool_id, client_id, username, password)
    
    if not bearer_token:
        print("Error: No bearer token available")
        return
    
    # Create client
    client = MCPAgentCoreClient(agent_arn, bearer_token)
    
    print("=== MCP AgentCore Client Example ===\n")
    
    # List available tools
    print("1. Listing available tools...")
    tools_response = client.list_tools()
    print(f"Tools: {json.dumps(tools_response, indent=2)}\n")
    
    # List available resources
    print("2. Listing available resources...")
    resources_response = client.list_resources()
    print(f"Resources: {json.dumps(resources_response, indent=2)}\n")
    
    # Example tool calls
    print("3. Testing tool calls...")
    
    # Test echo tool
    print("Testing 'echo' tool:")
    echo_result = client.invoke_tool("echo", {"message": "Hello from AgentCore!"})
    print(f"Result: {json.dumps(echo_result, indent=2)}\n")
    
    # Test timestamp tool
    print("Testing 'timestamp' tool:")
    timestamp_result = client.invoke_tool("timestamp", {})
    print(f"Result: {json.dumps(timestamp_result, indent=2)}\n")
    
    # Test calculate tool
    print("Testing 'calculate' tool:")
    calc_result = client.invoke_tool("calculate", {
        "operation": "add",
        "a": 15,
        "b": 27
    })
    print(f"Result: {json.dumps(calc_result, indent=2)}\n")
    
    # Test error handling
    print("Testing error handling (division by zero):")
    error_result = client.invoke_tool("calculate", {
        "operation": "divide",
        "a": 10,
        "b": 0
    })
    print(f"Result: {json.dumps(error_result, indent=2)}\n")

if __name__ == "__main__":
    main()