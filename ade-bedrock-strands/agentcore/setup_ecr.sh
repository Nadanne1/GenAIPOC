#!/bin/bash
set -e

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Validate required variables
if [ -z "$AWS_REGION" ]; then
    echo "❌ Error: AWS_REGION not set in .env file"
    exit 1
fi

if [ -z "$ECR_REPO_NAME" ]; then
    echo "❌ Error: ECR_REPO_NAME not set in .env file"
    exit 1
fi

echo "=========================================="
echo "Setting up ECR Repository"
echo "=========================================="
echo "Repository Name: $ECR_REPO_NAME"
echo "AWS Region: $AWS_REGION"
echo ""

# Check if repository exists
if aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $AWS_REGION > /dev/null 2>&1; then
    echo "✓ ECR repository '$ECR_REPO_NAME' already exists"
    REPO_URI=$(aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $AWS_REGION --query 'repositories[0].repositoryUri' --output text)
else
    echo "Creating ECR repository..."
    REPO_URI=$(aws ecr create-repository \
        --repository-name $ECR_REPO_NAME \
        --region $AWS_REGION \
        --image-scanning-configuration scanOnPush=true \
        --encryption-configuration encryptionType=AES256 \
        --query 'repository.repositoryUri' \
        --output text)
    
    echo "✓ ECR repository created successfully"
fi

echo ""
echo "=========================================="
echo "✓ ECR Setup Complete"
echo "=========================================="
echo "Repository URI: $REPO_URI"
echo ""
echo "Update your .env file with:"
echo "ECR_REPO_URI=$REPO_URI"
echo "ECR_IMAGE_URI=$REPO_URI:latest"
echo ""
echo "Next steps:"
echo "1. Update .env file with the URIs above"
echo "2. Run: ./build_and_push.sh"
