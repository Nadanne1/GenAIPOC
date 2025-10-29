"""LangGraph-based multi-agent system with proper state management"""
import json
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from utils import invoke_bedrock_nova


class AgentState(TypedDict):
    """State shared across all agents"""
    messages: Annotated[list, add_messages]
    query: str
    routing_decision: dict
    agent_responses: dict
    final_response: str
    next_agent: str


class LangGraphBookDetailsAgent:
    """Book details agent as LangGraph node"""
    
    def __init__(self, bedrock_client, book_data: str):
        self.bedrock_client = bedrock_client
        self.book_data = book_data
        self.name = "BookDetailsAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        prompt = f"""You are a Book Details Expert. Provide accurate book specifications.

Book Database:
{self.book_data[:3000]}

User Query: {query}

Provide detailed information about:
- Title and author
- Page count and ISBN
- Publisher and publication date
- Categories and language

Be concise and accurate."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphReviewsAgent:
    """Reviews agent as LangGraph node"""
    
    def __init__(self, bedrock_client, reviews_data: str):
        self.bedrock_client = bedrock_client
        self.reviews_data = reviews_data
        self.name = "ReviewsAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        prompt = f"""You are a Book Reviews Analyst. Analyze and summarize reader opinions.

Reviews Database:
{self.reviews_data[:3000]}

User Query: {query}

Provide analysis including:
- Overall sentiment
- Rating information
- Common themes
- Key praise or criticism

Be balanced and cite specific points."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphRecommendationAgent:
    """Recommendation agent as LangGraph node"""
    
    def __init__(self, bedrock_client, book_data: str, reviews_data: str):
        self.bedrock_client = bedrock_client
        self.book_data = book_data
        self.reviews_data = reviews_data
        self.name = "RecommendationAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        # Get context from other agents if available
        context = ""
        for agent_name, response in state["agent_responses"].items():
            if agent_name != self.name:
                context += f"\n{agent_name}: {response[:200]}..."
        
        prompt = f"""You are a Book Recommendation Specialist. Suggest books based on preferences.

Book Database:
{self.book_data[:2000]}

Reviews Summary:
{self.reviews_data[:2000]}

Context from other agents:
{context}

User Query: {query}

Provide recommendations including:
- Suggested books with reasons
- Why they match the query
- Rating and popularity info
- Alternatives

Be enthusiastic and helpful."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=500)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphGeneralAgent:
    """General knowledge agent as LangGraph node"""
    
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client
        self.name = "GeneralKnowledgeAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        prompt = f"""You are a General Book Knowledge Expert. Answer questions about books and literature.

User Query: {query}

Provide informative answers about:
- Authors and their works
- Literary concepts
- Book history
- Reading culture

Be knowledgeable and engaging."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphSupervisor:
    """Supervisor node for routing and coordination"""
    
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client
        self.name = "Supervisor"
    
    def route_query(self, state: AgentState) -> AgentState:
        """Analyze query and determine routing"""
        query = state["query"]
        
        prompt = f"""You are a Supervisor coordinating book specialist agents.

Available Agents:
- BookDetailsAgent: Book specs, publication info
- ReviewsAgent: Reader reviews and ratings
- RecommendationAgent: Book suggestions
- GeneralKnowledgeAgent: General book knowledge

User Query: "{query}"

Respond in JSON format:
{{
    "primary_agent": "agent_name",
    "needs_multiple": false,
    "reasoning": "brief explanation"
}}

Choose the best agent for this query."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=150)
        
        # Parse routing decision
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                routing = json.loads(response[start:end])
            else:
                routing = self._fallback_routing(query)
        except:
            routing = self._fallback_routing(query)
        
        state["routing_decision"] = routing
        state["next_agent"] = routing.get("primary_agent", "GeneralKnowledgeAgent")
        
        return state
    
    def _fallback_routing(self, query: str) -> dict:
        """Keyword-based fallback routing"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['page', 'author', 'published', 'isbn', 'publisher']):
            return {"primary_agent": "BookDetailsAgent", "needs_multiple": False}
        elif any(word in query_lower for word in ['review', 'rating', 'opinion', 'think']):
            return {"primary_agent": "ReviewsAgent", "needs_multiple": False}
        elif any(word in query_lower for word in ['recommend', 'suggest', 'should i', 'compare']):
            return {"primary_agent": "RecommendationAgent", "needs_multiple": False}
        else:
            return {"primary_agent": "GeneralKnowledgeAgent", "needs_multiple": False}
    
    def finalize_response(self, state: AgentState) -> AgentState:
        """Finalize and format the response"""
        # If only one agent responded, use that response
        if len(state["agent_responses"]) == 1:
            state["final_response"] = list(state["agent_responses"].values())[0]
        else:
            # Combine multiple agent responses
            combined = self._combine_responses(state)
            state["final_response"] = combined
        
        return state
    
    def _combine_responses(self, state: AgentState) -> str:
        """Combine multiple agent responses"""
        query = state["query"]
        responses = state["agent_responses"]
        
        prompt = f"""Combine these specialist responses into one coherent answer.

User Query: {query}

Specialist Responses:
"""
        for agent_name, response in responses.items():
            prompt += f"\n{agent_name}:\n{response}\n"
        
        prompt += "\nCreate a unified response that integrates all insights naturally."
        
        combined = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=600)
        return combined


def create_langgraph_workflow(bedrock_client, book_data: str, reviews_data: str):
    """Create the LangGraph workflow with all agents"""
    
    # Initialize agents
    supervisor = LangGraphSupervisor(bedrock_client)
    details_agent = LangGraphBookDetailsAgent(bedrock_client, book_data)
    reviews_agent = LangGraphReviewsAgent(bedrock_client, reviews_data)
    recommendation_agent = LangGraphRecommendationAgent(bedrock_client, book_data, reviews_data)
    general_agent = LangGraphGeneralAgent(bedrock_client)
    
    # Create workflow
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("supervisor_route", supervisor.route_query)
    workflow.add_node("BookDetailsAgent", details_agent)
    workflow.add_node("ReviewsAgent", reviews_agent)
    workflow.add_node("RecommendationAgent", recommendation_agent)
    workflow.add_node("GeneralKnowledgeAgent", general_agent)
    workflow.add_node("supervisor_finalize", supervisor.finalize_response)
    
    # Define routing function
    def route_to_agent(state: AgentState) -> Literal["BookDetailsAgent", "ReviewsAgent", "RecommendationAgent", "GeneralKnowledgeAgent"]:
        return state["next_agent"]
    
    # Add edges
    workflow.add_edge(START, "supervisor_route")
    workflow.add_conditional_edges(
        "supervisor_route",
        route_to_agent,
        {
            "BookDetailsAgent": "BookDetailsAgent",
            "ReviewsAgent": "ReviewsAgent",
            "RecommendationAgent": "RecommendationAgent",
            "GeneralKnowledgeAgent": "GeneralKnowledgeAgent"
        }
    )
    
    # All agents go to finalize
    workflow.add_edge("BookDetailsAgent", "supervisor_finalize")
    workflow.add_edge("ReviewsAgent", "supervisor_finalize")
    workflow.add_edge("RecommendationAgent", "supervisor_finalize")
    workflow.add_edge("GeneralKnowledgeAgent", "supervisor_finalize")
    workflow.add_edge("supervisor_finalize", END)
    
    # Compile
    app = workflow.compile()
    
    return app
