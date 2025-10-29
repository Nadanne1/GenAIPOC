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


class LangGraphMovieDetailsAgent:
    """Movie details agent as LangGraph node"""
    
    def __init__(self, bedrock_client, movie_data: str):
        self.bedrock_client = bedrock_client
        self.movie_data = movie_data
        self.name = "MovieDetailsAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        messages = state.get("messages", [])
        
        # Build conversation context
        conversation_context = ""
        if messages:
            recent_messages = messages[-6:]  # Last 3 exchanges (6 messages)
            for msg in recent_messages:
                if hasattr(msg, 'content'):
                    role = "User" if msg.__class__.__name__ == "HumanMessage" else "Assistant"
                    conversation_context += f"{role}: {msg.content}\n"
        
        prompt = f"""You are a Movie Details Expert. Provide accurate movie specifications and technical information.

Movie Database:
{self.movie_data[:3000]}

Conversation Context:
{conversation_context}

Current User Query: {query}

Provide detailed information about:
- Title and director
- Cast and main actors
- Runtime and release date
- Studio and production details
- Genres and language
- Box office performance and awards
- IMDb ID for reference

IMPORTANT: If the user refers to "it", "that movie", or similar pronouns, use the conversation context to understand which movie they're asking about. Be concise, accurate, and focus on factual movie specifications."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphMovieReviewsAgent:
    """Movie reviews agent as LangGraph node"""
    
    def __init__(self, bedrock_client, reviews_data: str):
        self.bedrock_client = bedrock_client
        self.reviews_data = reviews_data
        self.name = "MovieReviewsAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        prompt = f"""You are a Movie Reviews Analyst. Analyze and summarize audience opinions and ratings.

Movie Reviews Database:
{self.reviews_data[:3000]}

User Query: {query}

Provide analysis including:
- Overall audience sentiment
- IMDb rating and vote counts
- Common praise and criticism
- Whether it's worth watching
- Audience vs critic perspectives
- Content warnings if relevant

Be balanced, helpful, and cite specific points from reviews."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphMovieRecommendationAgent:
    """Movie recommendation agent as LangGraph node"""
    
    def __init__(self, bedrock_client, movie_data: str, reviews_data: str):
        self.bedrock_client = bedrock_client
        self.movie_data = movie_data
        self.reviews_data = reviews_data
        self.name = "MovieRecommendationAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        messages = state.get("messages", [])
        
        # Build conversation context
        conversation_context = ""
        if messages:
            recent_messages = messages[-6:]  # Last 3 exchanges (6 messages)
            for msg in recent_messages:
                if hasattr(msg, 'content'):
                    role = "User" if msg.__class__.__name__ == "HumanMessage" else "Assistant"
                    conversation_context += f"{role}: {msg.content}\n"
        
        # Get context from other agents if available
        agent_context = ""
        for agent_name, response in state["agent_responses"].items():
            if agent_name != self.name:
                agent_context += f"\n{agent_name}: {response[:200]}..."
        
        prompt = f"""You are a Movie Recommendation Specialist. Suggest movies based on preferences and mood.

Movie Database:
{self.movie_data[:2000]}

Reviews Summary:
{self.reviews_data[:2000]}

Conversation Context:
{conversation_context}

Context from other agents:
{agent_context}

Current User Query: {query}

Provide personalized recommendations including:
- Suggested movies with compelling reasons
- Why they match the user's preferences
- Genre, mood, and style considerations
- IMDb ratings and audience appeal
- Similar movies and alternatives
- Streaming availability if relevant

IMPORTANT: Use the conversation context to understand the user's preferences and any movies they've mentioned. Be enthusiastic, helpful, and consider the user's specific taste and mood."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=500)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphMovieKnowledgeAgent:
    """General movie knowledge agent as LangGraph node"""
    
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client
        self.name = "MovieKnowledgeAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        
        prompt = f"""You are a General Movie Knowledge Expert. Answer questions about cinema, film industry, and movie culture.

User Query: {query}

Provide informative answers about:
- Directors, actors, and their filmographies
- Film history and cinema movements
- Movie genres and storytelling techniques
- Film industry insights and trivia
- Box office trends and awards
- Behind-the-scenes information
- Movie culture and impact

Be knowledgeable, engaging, and passionate about cinema."""

        response = invoke_bedrock_nova(self.bedrock_client, prompt, max_tokens=400)
        
        # Update state
        state["agent_responses"][self.name] = response
        state["messages"].append(AIMessage(content=response, name=self.name))
        
        return state


class LangGraphStreamingAgent:
    """Streaming availability agent as LangGraph node"""
    
    def __init__(self, bedrock_client, movie_data: str):
        self.bedrock_client = bedrock_client
        self.movie_data = movie_data
        self.name = "StreamingAgent"
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process state and return updated state"""
        query = state["query"]
        messages = state.get("messages", [])
        
        # Build conversation context
        conversation_context = ""
        if messages:
            recent_messages = messages[-6:]  # Last 3 exchanges (6 messages)
            for msg in recent_messages:
                if hasattr(msg, 'content'):
                    role = "User" if msg.__class__.__name__ == "HumanMessage" else "Assistant"
                    conversation_context += f"{role}: {msg.content}\n"
        
        prompt = f"""You are a Streaming Availability Expert. Help users find where to watch movies.

Movie Database with Streaming Info:
{self.movie_data[:3000]}

Conversation Context:
{conversation_context}

Current User Query: {query}

Provide helpful information about:
- Where specific movies are available to stream
- Which platforms have the movie (Netflix, Amazon Prime, Hulu, Disney+, HBO Max, Apple TV)
- Rental vs subscription availability
- Alternative viewing options if not on preferred platform
- Platform recommendations based on user preferences

IMPORTANT: If the user refers to "it", "that movie", or similar pronouns, use the conversation context to understand which movie they're asking about. Be helpful and specific about streaming availability."""

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
        
        prompt = f"""You are a Supervisor coordinating movie specialist agents.

Available Agents:
- MovieDetailsAgent: Movie specs, cast, director, runtime, box office
- MovieReviewsAgent: Audience reviews, ratings, and opinions
- MovieRecommendationAgent: Movie suggestions and recommendations
- StreamingAgent: Where to watch movies, streaming availability
- MovieKnowledgeAgent: General cinema and film industry knowledge

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
        
        if any(word in query_lower for word in ['runtime', 'director', 'cast', 'released', 'imdb', 'studio', 'box office']):
            return {"primary_agent": "MovieDetailsAgent", "needs_multiple": False}
        elif any(word in query_lower for word in ['review', 'rating', 'opinion', 'think', 'worth watching']):
            return {"primary_agent": "MovieReviewsAgent", "needs_multiple": False}
        elif any(word in query_lower for word in ['watch', 'streaming', 'netflix', 'prime', 'hulu', 'disney+', 'hbo', 'apple tv', 'available', 'stream']):
            return {"primary_agent": "StreamingAgent", "needs_multiple": False}
        elif any(word in query_lower for word in ['recommend', 'suggest', 'should i', 'compare', 'like', 'similar']):
            return {"primary_agent": "MovieRecommendationAgent", "needs_multiple": False}
        else:
            return {"primary_agent": "MovieKnowledgeAgent", "needs_multiple": False}
    
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


def create_langgraph_workflow(bedrock_client, movie_data: str, reviews_data: str):
    """Create the LangGraph workflow with all movie agents"""
    
    # Initialize agents
    supervisor = LangGraphSupervisor(bedrock_client)
    details_agent = LangGraphMovieDetailsAgent(bedrock_client, movie_data)
    reviews_agent = LangGraphMovieReviewsAgent(bedrock_client, reviews_data)
    recommendation_agent = LangGraphMovieRecommendationAgent(bedrock_client, movie_data, reviews_data)
    streaming_agent = LangGraphStreamingAgent(bedrock_client, movie_data)
    knowledge_agent = LangGraphMovieKnowledgeAgent(bedrock_client)
    
    # Create workflow
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("supervisor_route", supervisor.route_query)
    workflow.add_node("MovieDetailsAgent", details_agent)
    workflow.add_node("MovieReviewsAgent", reviews_agent)
    workflow.add_node("MovieRecommendationAgent", recommendation_agent)
    workflow.add_node("StreamingAgent", streaming_agent)
    workflow.add_node("MovieKnowledgeAgent", knowledge_agent)
    workflow.add_node("supervisor_finalize", supervisor.finalize_response)
    
    # Define routing function
    def route_to_agent(state: AgentState) -> Literal["MovieDetailsAgent", "MovieReviewsAgent", "MovieRecommendationAgent", "StreamingAgent", "MovieKnowledgeAgent"]:
        return state["next_agent"]
    
    # Add edges
    workflow.add_edge(START, "supervisor_route")
    workflow.add_conditional_edges(
        "supervisor_route",
        route_to_agent,
        {
            "MovieDetailsAgent": "MovieDetailsAgent",
            "MovieReviewsAgent": "MovieReviewsAgent",
            "MovieRecommendationAgent": "MovieRecommendationAgent",
            "StreamingAgent": "StreamingAgent",
            "MovieKnowledgeAgent": "MovieKnowledgeAgent"
        }
    )
    
    # All agents go to finalize
    workflow.add_edge("MovieDetailsAgent", "supervisor_finalize")
    workflow.add_edge("MovieReviewsAgent", "supervisor_finalize")
    workflow.add_edge("MovieRecommendationAgent", "supervisor_finalize")
    workflow.add_edge("StreamingAgent", "supervisor_finalize")
    workflow.add_edge("MovieKnowledgeAgent", "supervisor_finalize")
    workflow.add_edge("supervisor_finalize", END)
    
    # Compile
    app = workflow.compile()
    
    return app
