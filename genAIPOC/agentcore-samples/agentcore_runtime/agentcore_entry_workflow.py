#!/usr/bin/env python3
"""
AgentCore Entry Point - Using LlamaIndex Workflow
Event-driven multi-agent orchestration with LlamaIndex Workflow framework
"""
import sys
import os
from typing import Any, Dict

# Add paths for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Try to import AgentCore SDK with fallback
agentcore_app = None
try:
    from bedrock_agentcore.runtime import BedrockAgentCoreApp
    agentcore_app = BedrockAgentCoreApp()
    print("✅ AgentCore SDK loaded successfully")
except ImportError as e:
    print(f"❌ bedrock_agentcore import failed: {e}")
    # Create fallback HTTP server
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import json
    import asyncio
    
    class AgentHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                # Run main asynchronously
                response = asyncio.run(main(payload))
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"result": response}).encode('utf-8'))
            except Exception as e:
                import traceback
                error_detail = traceback.format_exc()
                print(f"Error processing request: {error_detail}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e), "detail": error_detail}).encode('utf-8'))
        
        def do_GET(self):
            # Handle ping requests
            if self.path == '/ping':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'pong')
            else:
                self.send_response(404)
                self.end_headers()
    
    class FallbackApp:
        def entrypoint(self, fn):
            return fn
        def run(self):
            print("🚀 Starting fallback HTTP server on port 8080...")
            server = HTTPServer(('0.0.0.0', 8080), AgentHandler)
            server.serve_forever()
    
    agentcore_app = FallbackApp()
    print("⚠️ Using fallback HTTP server")

# Create AgentCore app instance
app = agentcore_app

@app.entrypoint
async def main(payload: Dict[str, Any]) -> str:
    """
    AgentCore entrypoint using LlamaIndex Workflow
    
    The workflow explicitly orchestrates:
    1. Planner Agent - Breaks down the question
    2. Researcher Agent - Queries RAG for each subtask
    3. Verifier Agent - Validates quality
    4. Presenter Agent - Synthesizes final answer
    
    This approach combines:
    - Explicit control (like custom orchestration)
    - Framework benefits (LlamaIndex Workflow)
    - Event-driven architecture
    - Async support for performance
    
    Args:
        payload: Input from user/system with 'prompt' field
        context: AgentCore context with session_id, metadata, etc.
    
    Returns:
        Structured response with answer, citations, and trace
    """
    # Extract the user's question
    question = payload.get("prompt", "Ask me about incident runbooks.")
    
    # Optional: Log the request
    session_id = "workflow-session"
    print(f"\n{'='*80}")
    print(f"[AgentCore] New Request - Workflow-Based Agent")
    print(f"{'='*80}")
    print(f"Session ID: {session_id}")
    print(f"Question: {question}")
    print(f"{'='*80}\n")
    
    # Run the LlamaIndex Workflow multi-agent system (async)
    from agentcore_runtime.notebook_agent_workflow import run_multi_agent_async
    result = await run_multi_agent_async(question)
    
    # Format response for AgentCore
    response = {
        "result": result["answer"],           # Main answer text
        "citations": result["citations"],     # Source citations
        "trace": result["trace"],             # Workflow trace
        "session_id": session_id,             # Session tracking
        "metadata": {
            "agent_type": "llamaindex_workflow",
            "agent_framework": "LlamaIndex Workflow (Event-Driven)",
            "agents_used": result["trace"].get("agents_used", []),
            "subtasks_count": len(result["trace"].get("subtasks", [])),
            "duration_seconds": result["trace"].get("duration_seconds", 0),
            "citations_count": len(result["citations"]),
            "verification_passed": result["trace"].get("verification", {}).get("pass", False)
        }
    }
    
    print(f"\n{'='*80}")
    print(f"[AgentCore] Response Ready")
    print(f"{'='*80}")
    print(f"Answer length: {len(result['answer'])} characters")
    print(f"Citations: {len(result['citations'])} sources")
    print(f"Duration: {result['trace'].get('duration_seconds', 0):.2f}s")
    print(f"Agents used: {', '.join(result['trace'].get('agents_used', []))}")
    print(f"{'='*80}\n")
    
    # Return just the answer string (like the official sample)
    return result["answer"]

if __name__ == "__main__":
    print("🚀 Starting AgentCore Workflow Agent...")
    app.run()
