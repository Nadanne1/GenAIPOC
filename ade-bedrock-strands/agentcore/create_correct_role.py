#!/usr/bin/env python3
"""
Create IAM role with the CORRECT trust policy for AgentCore
Based on the working roles in us-east-1
"""

import boto3
import json
import os
from dotenv import load_dotenv
import time

load_dotenv(override=True)

AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
BEDROCK_KB_ID = os.getenv('BEDROCK_KB_ID')
ROLE_NAME = "FinancialAnalystAgentCoreRole"

iam = boto3.client('iam')
sts = boto3.client('sts')

account_id = sts.get_caller_identity()['Account']

# CORRECT trust policy - using bedrock-agentcore.amazonaws.com
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AssumeRolePolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "bedrock-agentcore.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": account_id
                },
                "ArnLike": {
                    "aws:SourceArn": f"arn:aws:bedrock-agentcore:{AWS_REGION}:{account_id}:*"
                }
            }
        }
    ]
}

# Comprehensive permissions based on working roles
permissions_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ECRImageAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": [
                f"arn:aws:ecr:{AWS_REGION}:{account_id}:repository/*"
            ]
        },
        {
            "Sid": "ECRTokenAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                f"arn:aws:logs:{AWS_REGION}:{account_id}:log-group:/aws/bedrock-agentcore/runtimes/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                f"arn:aws:logs:{AWS_REGION}:{account_id}:log-group:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords",
                "xray:GetSamplingRules",
                "xray:GetSamplingTargets"
            ],
            "Resource": ["*"]
        },
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "bedrock-agentcore"
                }
            }
        },
        {
            "Sid": "BedrockModelInvocation",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:ApplyGuardrail"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/*",
                f"arn:aws:bedrock:{AWS_REGION}:{account_id}:*"
            ]
        },
        {
            "Sid": "BedrockKnowledgeBaseAccess",
            "Effect": "Allow",
            "Action": [
                "bedrock:Retrieve",
                "bedrock:RetrieveAndGenerate"
            ],
            "Resource": [
                f"arn:aws:bedrock:{AWS_REGION}:{account_id}:knowledge-base/{BEDROCK_KB_ID}"
            ]
        }
    ]
}

try:
    print(f"Creating IAM role: {ROLE_NAME}")
    print(f"Region: {AWS_REGION}")
    print(f"Account: {account_id}")
    
    # Create the role
    try:
        role_response = iam.create_role(
            RoleName=ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Execution role for Bedrock AgentCore - Financial Analyst Agent",
            Tags=[
                {'Key': 'Service', 'Value': 'BedrockAgentCore'},
                {'Key': 'Project', 'Value': 'FinancialAnalyst'}
            ]
        )
        role_arn = role_response['Role']['Arn']
        print(f"✓ Role created: {role_arn}")
    except iam.exceptions.EntityAlreadyExistsException:
        # Update existing role
        print(f"✓ Role already exists, updating trust policy...")
        iam.update_assume_role_policy(
            RoleName=ROLE_NAME,
            PolicyDocument=json.dumps(trust_policy)
        )
        role = iam.get_role(RoleName=ROLE_NAME)
        role_arn = role['Role']['Arn']
        print(f"✓ Role updated: {role_arn}")
    
    # Attach inline policy
    iam.put_role_policy(
        RoleName=ROLE_NAME,
        PolicyName="FinancialAnalystAgentCorePermissions",
        PolicyDocument=json.dumps(permissions_policy)
    )
    
    print(f"✓ Permissions policy attached")
    
    # Wait for IAM propagation
    print(f"\n⏳ Waiting 10 seconds for IAM propagation...")
    time.sleep(10)
    
    # Update .env file
    env_file = '.env'
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    # Update or add AGENT_ROLE_ARN
    found = False
    for i, line in enumerate(lines):
        if line.startswith('AGENT_ROLE_ARN='):
            lines[i] = f'AGENT_ROLE_ARN={role_arn}\n'
            found = True
            break
    
    if not found:
        lines.append(f'\nAGENT_ROLE_ARN={role_arn}\n')
    
    with open(env_file, 'w') as f:
        f.writelines(lines)
    
    print(f"✓ Role ARN saved to {env_file}")
    print(f"\nRole ARN: {role_arn}")
    print(f"\n✓✓✓ Role is ready! You can now run: ./deploy_cli.sh")
    
except Exception as e:
    print(f"❌ Error: {e}")
    raise
