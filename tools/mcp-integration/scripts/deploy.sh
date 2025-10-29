#!/bin/bash

# MCP Server Deployment Script for Amazon Bedrock AgentCore
# This script automates the deployment process using the AgentCore CLI

set -e  # Exit on any error

# Configuration
MCP_SERVER_FILE="examples/simple_mcp_server.py"
GATEWAY_NAME="mcp-integration-gateway"
REGION="us-east-1"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        log_error "Python 3 is not installed"
        exit 1
    fi
    
    # Check Python version
    python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if [[ $(echo "$python_version 3.10" | awk '{print ($1 < $2)}') == 1 ]]; then
        log_warning "Python version $python_version detected. Python 3.10+ is recommended."
    else
        log_success "Python version $python_version is compatible"
    fi
    
    # Check if AWS CLI is configured
    if ! aws sts get-caller-identity &> /dev/null; then
        log_error "AWS credentials not configured. Run 'aws configure' first."
        exit 1
    fi
    
    log_success "AWS credentials configured"
    
    # Check if AgentCore CLI is installed
    if ! command -v agentcore &> /dev/null; then
        log_warning "AgentCore CLI not found. Installing..."
        pip install bedrock-agentcore-starter-toolkit
        log_success "AgentCore CLI installed"
    else
        log_success "AgentCore CLI is available"
    fi
}

# Install dependencies
install_dependencies() {
    log_info "Installing dependencies..."
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        log_info "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install required packages
    pip install --upgrade pip
    pip install mcp
    pip install bedrock-agentcore-starter-toolkit
    pip install boto3
    pip install requests
    
    log_success "Dependencies installed"
}

# Test MCP server locally
test_local_server() {
    log_info "Testing MCP server locally..."
    
    if [ ! -f "$MCP_SERVER_FILE" ]; then
        log_error "MCP server file not found: $MCP_SERVER_FILE"
        exit 1
    fi
    
    # Test server syntax
    python3 -m py_compile "$MCP_SERVER_FILE"
    log_success "MCP server syntax is valid"
    
    # TODO: Add more comprehensive local testing
    log_info "Local testing completed (basic syntax check)"
}

# Deploy MCP server
deploy_server() {
    log_info "Deploying MCP server to Amazon Bedrock AgentCore..."
    
    # Configure deployment
    log_info "Configuring deployment..."
    agentcore configure -e "$MCP_SERVER_FILE" --protocol MCP --region "$REGION"
    
    # Launch deployment
    log_info "Launching deployment..."
    deployment_output=$(agentcore launch)
    
    # Extract ARN from output
    agent_arn=$(echo "$deployment_output" | grep -o 'arn:aws:bedrock-agent:[^"]*' | head -1)
    
    if [ -n "$agent_arn" ]; then
        log_success "Deployment successful!"
        log_info "Agent ARN: $agent_arn"
        
        # Save ARN to file
        echo "$agent_arn" > .agent_arn
        log_info "Agent ARN saved to .agent_arn file"
    else
        log_error "Failed to extract Agent ARN from deployment output"
        log_error "Deployment output: $deployment_output"
        exit 1
    fi
}

# Deploy gateway (for existing MCP server)
deploy_gateway() {
    local mcp_endpoint="$1"
    
    if [ -z "$mcp_endpoint" ]; then
        log_error "MCP endpoint URL is required for gateway deployment"
        exit 1
    fi
    
    log_info "Deploying AgentCore Gateway for existing MCP server..."
    
    # Configure gateway
    log_info "Configuring gateway..."
    agentcore configure --protocol MCP --endpoint "$mcp_endpoint" --region "$REGION"
    
    # Launch gateway
    log_info "Launching gateway..."
    gateway_output=$(agentcore launch)
    
    # Extract ARN from output
    gateway_arn=$(echo "$gateway_output" | grep -o 'arn:aws:bedrock-agent:[^"]*' | head -1)
    
    if [ -n "$gateway_arn" ]; then
        log_success "Gateway deployment successful!"
        log_info "Gateway ARN: $gateway_arn"
        
        # Save ARN to file
        echo "$gateway_arn" > .gateway_arn
        log_info "Gateway ARN saved to .gateway_arn file"
    else
        log_error "Failed to extract Gateway ARN from deployment output"
        log_error "Gateway output: $gateway_output"
        exit 1
    fi
}

# Get authentication token
get_auth_token() {
    log_info "Getting authentication token..."
    
    # Try to get token using AgentCore CLI
    if command -v agentcore &> /dev/null; then
        log_info "Use 'agentcore auth login' to authenticate and 'agentcore auth token' to get token"
        log_info "Or set BEARER_TOKEN environment variable manually"
    else
        log_warning "AgentCore CLI not available for token management"
        log_info "Please set BEARER_TOKEN environment variable manually"
    fi
}

# Test deployment
test_deployment() {
    log_info "Testing deployment..."
    
    if [ -f ".agent_arn" ]; then
        agent_arn=$(cat .agent_arn)
        log_info "Testing with Agent ARN: $agent_arn"
        
        # Set environment variables for testing
        export AGENT_ARN="$agent_arn"
        
        if [ -n "$BEARER_TOKEN" ]; then
            log_info "Running client test..."
            python3 examples/client_example.py
            log_success "Deployment test completed"
        else
            log_warning "BEARER_TOKEN not set. Skipping client test."
            log_info "Set BEARER_TOKEN environment variable and run: python3 examples/client_example.py"
        fi
    else
        log_error "No agent ARN found. Deploy first."
        exit 1
    fi
}

# Cleanup deployment
cleanup() {
    log_info "Cleaning up deployment..."
    
    # TODO: Add cleanup commands when available in AgentCore CLI
    log_warning "Manual cleanup may be required through AWS Console"
    log_info "Check CloudFormation stacks, Lambda functions, and Cognito user pools"
}

# Show usage
show_usage() {
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  deploy              Deploy MCP server to AgentCore"
    echo "  gateway <endpoint>  Deploy gateway for existing MCP server"
    echo "  test                Test the deployment"
    echo "  cleanup             Clean up deployment resources"
    echo "  help                Show this help message"
    echo ""
    echo "Environment Variables:"
    echo "  BEARER_TOKEN        Authentication token for API calls"
    echo "  AWS_REGION          AWS region (default: us-east-1)"
    echo ""
    echo "Examples:"
    echo "  $0 deploy"
    echo "  $0 gateway http://localhost:8000"
    echo "  $0 test"
}

# Main script logic
main() {
    case "${1:-}" in
        "deploy")
            check_prerequisites
            install_dependencies
            test_local_server
            deploy_server
            get_auth_token
            log_success "Deployment completed! Set BEARER_TOKEN and run '$0 test' to verify."
            ;;
        "gateway")
            if [ -z "${2:-}" ]; then
                log_error "Gateway endpoint URL is required"
                show_usage
                exit 1
            fi
            check_prerequisites
            install_dependencies
            deploy_gateway "$2"
            get_auth_token
            log_success "Gateway deployment completed! Set BEARER_TOKEN and run '$0 test' to verify."
            ;;
        "test")
            test_deployment
            ;;
        "cleanup")
            cleanup
            ;;
        "help"|"-h"|"--help")
            show_usage
            ;;
        "")
            log_error "No command specified"
            show_usage
            exit 1
            ;;
        *)
            log_error "Unknown command: $1"
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"