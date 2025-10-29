"""Multi-agent movie assistant with LangGraph and LangSmith integration"""
import os
import json
import boto3
from dotenv import load_dotenv
import gradio as gr
from langgraph_agents import create_langgraph_workflow
from langsmith import Client
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Initialize LangSmith client (optional)
langsmith_enabled = os.getenv('LANGCHAIN_TRACING_V2', 'false').lower() == 'true'
if langsmith_enabled:
    try:
        langsmith_client = Client()
        print("✅ LangSmith tracing enabled")
        print(f"   Project: {os.getenv('LANGCHAIN_PROJECT', 'default')}")
    except Exception as e:
        print(f"⚠️  LangSmith not configured: {e}")
        langsmith_enabled = False
else:
    print("ℹ️  LangSmith tracing disabled")

# Initialize Bedrock client
# Boto3 will automatically use AWS_BEARER_TOKEN_BEDROCK if set in environment
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv('AWS_REGION', 'us-west-2')
)

bearer_token = os.getenv('AWS_BEARER_TOKEN_BEDROCK')
if bearer_token:
    print("✅ Using Bedrock bearer token authentication")
else:
    print("✅ Using standard AWS credentials")

# Load movie data
def load_json_data(filepath: str) -> str:
    """Load and format JSON data as text"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return json.dumps(data, indent=2)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return "{}"

print("🎬 Loading movie data...")
movie_details_data = load_json_data("data/movie_details.json")
movie_reviews_data = load_json_data("data/movie_reviews.json")

# Create LangGraph workflow
print("🔧 Building LangGraph workflow...")
workflow_app = create_langgraph_workflow(bedrock_runtime, movie_details_data, movie_reviews_data)

print("✅ LangGraph workflow compiled!")
print("\n" + "="*60)
print("Multi-Agent Movie Assistant with LangGraph Ready!")
print("="*60 + "\n")

# Track conversation for analytics
conversation_history = []


def chat_interface(message, history):
    """Gradio chat interface with LangGraph"""
    if message.lower() in ['quit', 'exit']:
        return "Goodbye! Thanks for using the Movie Assistant."
    
    try:
        # Build conversation context from Gradio history
        conversation_messages = []
        
        # Add previous exchanges to context
        for user_msg, assistant_msg in history:
            conversation_messages.append(HumanMessage(content=user_msg))
            if assistant_msg:
                conversation_messages.append(AIMessage(content=assistant_msg))
        
        # Add current user message
        conversation_messages.append(HumanMessage(content=message))
        
        # Initialize state with conversation context
        initial_state = {
            "messages": conversation_messages,
            "query": message,
            "routing_decision": {},
            "agent_responses": {},
            "final_response": "",
            "next_agent": ""
        }
        
        # Run workflow
        print(f"\n🔄 Processing: {message}")
        result = workflow_app.invoke(initial_state)
        
        # Extract response
        response = result.get("final_response", "I couldn't process that query.")
        
        # Log routing decision
        routing = result.get("routing_decision", {})
        print(f"   ✓ Routed to: {routing.get('primary_agent', 'Unknown')}")
        print(f"   ✓ Agents used: {list(result.get('agent_responses', {}).keys())}")
        
        # Track conversation
        conversation_history.append({
            "query": message,
            "routing": routing,
            "agents_used": list(result.get('agent_responses', {}).keys()),
            "response": response
        })
        
        return response
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return f"I encountered an error: {str(e)}"


def get_workflow_visualization():
    """Get workflow graph visualization"""
    try:
        # Get the graph as mermaid
        mermaid = workflow_app.get_graph().draw_mermaid()
        return f"```mermaid\n{mermaid}\n```"
    except:
        return "Workflow visualization not available"


def get_conversation_stats():
    """Get conversation statistics"""
    if not conversation_history:
        return "No conversations yet"
    
    total = len(conversation_history)
    agent_usage = {}
    
    for conv in conversation_history:
        for agent in conv.get('agents_used', []):
            agent_usage[agent] = agent_usage.get(agent, 0) + 1
    
    stats = f"### Conversation Statistics\n\n"
    stats += f"**Total Queries**: {total}\n\n"
    stats += f"**Agent Usage**:\n"
    for agent, count in sorted(agent_usage.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total) * 100
        stats += f"- {agent}: {count} ({percentage:.1f}%)\n"
    
    return stats


def get_langsmith_info():
    """Get LangSmith project information"""
    if not langsmith_enabled:
        return """
### LangSmith Not Enabled

To enable LangSmith tracing:

1. Sign up at https://smith.langchain.com
2. Get your API key
3. Add to `.env`:
```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_PROJECT=movie-assistant-multiagent
```
4. Restart the application

**Benefits**:
- Trace all agent interactions
- Debug routing decisions
- Monitor performance
- Analyze conversation patterns
"""
    
    project = os.getenv('LANGCHAIN_PROJECT', 'default')
    return f"""
### LangSmith Enabled ✅

**Project**: {project}

View traces at: https://smith.langchain.com

**What's being tracked**:
- All agent invocations
- Routing decisions
- LLM calls and responses
- Execution time
- Error traces

Check the LangSmith dashboard for detailed analytics!
"""


# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="LangGraph Multi-Agent Movie Assistant") as demo:
    gr.Markdown("""
    # 🎬 Multi-Agent Movie Assistant
    ### Powered by LangGraph + AWS Bedrock Nova Lite + LangSmith
    
    A sophisticated multi-agent system using LangGraph's StateGraph for movie recommendations and information.
    """)
    
    with gr.Tab("💬 Chat"):
        chatbot = gr.ChatInterface(
            fn=chat_interface,
            examples=[
                "Who directed Inception?",
                "What do people think about Top Gun Maverick?",
                "Recommend a good sci-fi movie",
                "Where can I watch Last Action Hero?"
            ],
            title="",
            description="Ask about movies! The supervisor will route your query through the LangGraph workflow."
        )
    
    with gr.Tab("📊 Analytics"):
        gr.Markdown("### Real-time Analytics")
        stats_display = gr.Markdown(get_conversation_stats())
        refresh_stats_btn = gr.Button("🔄 Refresh Statistics")
        refresh_stats_btn.click(fn=get_conversation_stats, outputs=stats_display)
    
    with gr.Tab("🔍 LangSmith"):
        langsmith_info = gr.Markdown(get_langsmith_info())
        refresh_langsmith_btn = gr.Button("🔄 Refresh Info")
        refresh_langsmith_btn.click(fn=get_langsmith_info, outputs=langsmith_info)
    
    with gr.Tab("🗺️ Workflow Graph"):
        gr.Markdown("### LangGraph Workflow Visualization")
        workflow_viz = gr.Markdown(get_workflow_visualization())
    
    with gr.Tab("ℹ️ About"):
        gr.Markdown("""
        ## LangGraph Multi-Agent Architecture
        
        ### State Management
        Each query flows through a shared state containing:
        - Messages history
        - Query text
        - Routing decisions
        - Agent responses
        - Final response
        
        ### Workflow Nodes
        1. **Supervisor Route**: Analyzes query and determines routing
        2. **Specialist Agents**: Process query with domain expertise
        3. **Supervisor Finalize**: Combines and formats response
        
        ### Agent Nodes
        - **MovieDetailsAgent**: Movie specifications (cast, director, runtime)
        - **MovieReviewsAgent**: Review analysis and ratings
        - **MovieRecommendationAgent**: Personalized movie suggestions
        - **StreamingAgent**: Where to watch movies (Netflix, Prime, Hulu, etc.)
        - **MovieKnowledgeAgent**: Cinema and film industry knowledge
        
        ### LangSmith Integration
        When enabled, LangSmith traces:
        - Every node execution
        - State transitions
        - LLM calls
        - Execution time
        - Errors and debugging info
        
        ### Benefits
        ✓ Proper state management
        ✓ Traceable execution
        ✓ Easy to debug
        ✓ Scalable architecture
        ✓ Production-ready
        """)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Starting LangGraph Multi-Agent Movie Assistant...")
    print("="*60 + "\n")
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
