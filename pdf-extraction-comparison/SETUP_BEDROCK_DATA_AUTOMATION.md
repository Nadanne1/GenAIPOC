# Bedrock Data Automation Setup Guide

## Overview

Amazon Bedrock Data Automation (BDA) is a managed service for document processing. This guide helps you set it up for the comparison demo.

## Prerequisites

- AWS Account with Bedrock access
- BDA enabled in your region (us-east-1 recommended)
- S3 bucket for temporary storage

## Setup Steps

### 1. Create BDA Project

**Option A: AWS Console**
1. Go to AWS Console → Bedrock → Data Automation
2. Create a new project
3. Configure for document processing
4. Note the project ARN

**Option B: AWS CLI**
```bash
aws bedrock-data-automation create-data-automation-project \
    --project-name pdf-comparison \
    --region us-east-1
```

### 2. Configure Environment

Add to your `.env` file:
```bash
BDA_PROJECT_ARN=arn:aws:bedrock:us-east-1:ACCOUNT_ID:data-automation-project/PROJECT_ID
BDA_TEMP_BUCKET=your-s3-bucket-name
```

### 3. Update IAM Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-data-automation-runtime:InvokeDataAutomationAsync",
                "bedrock-data-automation-runtime:GetDataAutomationStatus"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::your-bucket/*"
        }
    ]
}
```

### 4. Test

```bash
python3 main.py your_test.pdf
```

## Pricing

- **Fixed cost**: $10.00 per 1000 pages
- **Predictable**: Same cost regardless of content type
- **No token-based pricing**: Unlike Claude models

## Troubleshooting

### "Service not available"
BDA may not be available in your region. Check AWS Console for availability.

### "AccessDenied"
Verify IAM permissions include `bedrock-data-automation-runtime` actions.

### "ResourceNotFound"
Ensure your BDA project ARN is correct in `.env` file.

## Notes

- BDA processes documents asynchronously
- Results are stored in S3
- Processing time varies by document complexity
- Cost is static regardless of optimization

## Alternative

If BDA is not available, the demo will skip this scenario. You can still compare Textract vs Claude Smart Routing.
