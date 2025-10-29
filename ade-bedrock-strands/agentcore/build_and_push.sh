#!/bin/bash
# Build and push Financial Market Analyst Agent to ECR using Finch

set -e

# Load environment variables
source .env

# Validate required variables
if [ -z "$ECR_IMAGE_URI" ]; then
    echo "❌ ECR_IMAGE_URI not set in .env file"
    exit 1
fi

if [ -z "$AWS_REGION" ]; then
    echo "❌ AWS_REGION not set in .env file"
    exit 1
fi

# Extract ECR repository details
ECR_REGISTRY=$(echo $ECR_IMAGE_URI | cut -d'/' -f1)
ECR_REPO=$(echo $ECR_IMAGE_URI | cut -d'/' -f2 | cut -d':' -f1)

echo "Building and pushing Financial Market Analyst Agent"
echo "Registry: $ECR_REGISTRY"
echo "Repository: $ECR_REPO"
echo "Region: $AWS_REGION"

# Login to ECR
echo ""
echo "Logging in to ECR..."
aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin $ECR_REGISTRY

# Build image for ARM64 (AgentCore requirement)
echo ""
echo "Building ARM64 image..."
finch build --platform linux/arm64 -t $ECR_IMAGE_URI .

# Push to ECR
echo ""
echo "Pushing image to ECR..."
finch push $ECR_IMAGE_URI

echo ""
echo "✓ Image successfully pushed to ECR!"
echo "  Image URI: $ECR_IMAGE_URI"
echo ""
echo "Next step: python deploy_agent.py"
