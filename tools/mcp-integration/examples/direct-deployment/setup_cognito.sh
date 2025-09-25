#!/bin/bash

# Cognito Setup Script for MCP Server Authentication
# Based on AWS AgentCore documentation

echo "🚀 Setting up Cognito authentication for MCP server..."

# Set secure passwords (you can change these)
TEMP_PASSWORD="TempPass123!"
PERMANENT_PASSWORD="SecurePass123!"

echo "📝 Creating Cognito User Pool..."

# Create User Pool and capture Pool ID directly
export POOL_ID=$(aws cognito-idp create-user-pool \
  --pool-name "MCPServerUserPool" \
  --policies '{"PasswordPolicy":{"MinimumLength":8}}' \
  --region us-east-1 | jq -r '.UserPool.Id')

if [ "$POOL_ID" = "null" ] || [ -z "$POOL_ID" ]; then
    echo "❌ Failed to create User Pool"
    exit 1
fi

echo "✅ User Pool created: $POOL_ID"

echo "📱 Creating App Client..."

# Create App Client and capture Client ID directly
export CLIENT_ID=$(aws cognito-idp create-user-pool-client \
  --user-pool-id $POOL_ID \
  --client-name "MCPServerClient" \
  --no-generate-secret \
  --explicit-auth-flows "ALLOW_USER_PASSWORD_AUTH" "ALLOW_REFRESH_TOKEN_AUTH" \
  --region us-east-1 | jq -r '.UserPoolClient.ClientId')

if [ "$CLIENT_ID" = "null" ] || [ -z "$CLIENT_ID" ]; then
    echo "❌ Failed to create App Client"
    exit 1
fi

echo "✅ App Client created: $CLIENT_ID"

echo "👤 Creating test user..."

# Create User
aws cognito-idp admin-create-user \
  --user-pool-id $POOL_ID \
  --username "mcpuser" \
  --temporary-password "$TEMP_PASSWORD" \
  --region us-east-1 \
  --message-action SUPPRESS > /dev/null

if [ $? -ne 0 ]; then
    echo "❌ Failed to create user"
    exit 1
fi

echo "✅ User created: mcpuser"

echo "🔐 Setting permanent password..."

# Set Permanent Password
aws cognito-idp admin-set-user-password \
  --user-pool-id $POOL_ID \
  --username "mcpuser" \
  --password "$PERMANENT_PASSWORD" \
  --region us-east-1 \
  --permanent > /dev/null

if [ $? -ne 0 ]; then
    echo "❌ Failed to set permanent password"
    exit 1
fi

echo "✅ Permanent password set"

echo "🎫 Authenticating user and getting bearer token..."

# Authenticate User and capture Access Token
export BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME='mcpuser',PASSWORD="$PERMANENT_PASSWORD" \
  --region us-east-1 | jq -r '.AuthenticationResult.AccessToken')

if [ "$BEARER_TOKEN" = "null" ] || [ -z "$BEARER_TOKEN" ]; then
    echo "❌ Failed to get bearer token"
    exit 1
fi

echo "✅ Bearer token obtained!"

echo ""
echo "🎉 Cognito setup completed successfully!"
echo "=" * 50
echo "📋 Configuration Details:"
echo "Pool ID: $POOL_ID"
echo "Discovery URL: https://cognito-idp.us-east-1.amazonaws.com/$POOL_ID/.well-known/openid-configuration"
echo "Client ID: $CLIENT_ID"
echo "Username: mcpuser"
echo "Password: $PERMANENT_PASSWORD"
echo ""
echo "🔑 Bearer Token (first 50 chars): ${BEARER_TOKEN:0:50}..."
echo ""
echo "🚀 Environment Variables Set:"
echo "export POOL_ID=\"$POOL_ID\""
echo "export CLIENT_ID=\"$CLIENT_ID\""
echo "export BEARER_TOKEN=\"$BEARER_TOKEN\""
echo ""
echo "💡 You can now test the MCP server with:"
echo "python3 examples/mcp_client.py"