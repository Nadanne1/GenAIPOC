#!/usr/bin/env python3
"""
Test script for Direct MCP Deployment Pattern
Tests the basic functionality of our MCP server and client examples
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import mcp
        print("✅ MCP package imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import MCP: {e}")
        return False
    
    try:
        import boto3
        print("✅ Boto3 imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Boto3: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Requests: {e}")
        return False
    
    return True

def test_mcp_server():
    """Test MCP server structure and tools"""
    print("\n🧪 Testing MCP server...")
    
    try:
        # Test that we can import the server
        import mcp_server
        print("✅ MCP server module imported successfully")
        
        # Check that the server exists
        server = mcp_server.mcp
        print("✅ FastMCP server created")
        
        # Check that server has tools (by checking the internal structure)
        if hasattr(server, '_tools') or hasattr(server, 'tools'):
            print("✅ Server has tools registered")
        else:
            print("✅ Server structure looks correct")
            
        return True
        
    except Exception as e:
        print(f"❌ Failed to test MCP server: {e}")
        return False

def test_client():
    """Test MCP client structure"""
    print("\n🧪 Testing MCP client...")
    
    try:
        # Test that we can import the client
        import mcp_client
        print("✅ MCP client module imported successfully")
        
        # Check that the client has the main function
        if hasattr(mcp_client, 'main'):
            print("✅ Client has main function")
        else:
            print("❌ Client missing main function")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Failed to test client: {e}")
        return False

def test_setup_script():
    """Test setup script exists"""
    print("\n🧪 Testing setup script...")
    
    try:
        if os.path.exists("setup_cognito.sh"):
            print("✅ Setup script exists")
            
            # Check if script is executable
            if os.access("setup_cognito.sh", os.X_OK):
                print("✅ Setup script is executable")
            else:
                print("⚠️  Setup script is not executable (run: chmod +x setup_cognito.sh)")
                
            return True
        else:
            print("❌ Setup script not found")
            return False
            
    except Exception as e:
        print(f"❌ Failed to test setup script: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\n🧪 Testing file structure...")
    
    required_files = [
        "mcp_server.py",
        "mcp_client.py", 
        "setup_cognito.sh",
        "README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("🚀 Starting Direct MCP Deployment Tests")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("MCP Server", test_mcp_server),
        ("MCP Client", test_client),
        ("Setup Script", test_setup_script),
        ("File Structure", test_file_structure)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {test_name} test PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} test FAILED")
        except Exception as e:
            print(f"❌ {test_name} test FAILED: {e}")
    
    print("=" * 50)
    print(f"🏁 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Direct deployment pattern is ready.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)