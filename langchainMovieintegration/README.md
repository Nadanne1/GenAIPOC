# 🎬 Multi-Agent Movie Assistant

A production-ready AI assistant using **LangGraph**, **AWS Bedrock Nova Lite**, and **LangSmith** for intelligent movie queries with full observability.

## LangGraph Multi-Agent Implementation 
Full LangGraph StateGraph implementation with LangSmith integration:
- **Proper State Management**: TypedDict state across all nodes
- **Supervisor Node**: Intelligent routing with LLM
- **5 Specialist Agent Nodes**: MovieDetails, MovieReviews, MovieRecommendation, Streaming, MovieKnowledge
- **LangSmith Tracing**: Full observability and debugging
- **Visual Workflow**: See execution graph
- **Production Ready**: Scalable and maintainable

## Features
- 🎬 Query movie details and specifications (cast, director, runtime)
- ⭐ Get movie reviews and IMDb ratings
- 🎯 Personalized movie recommendations
- 📺 Find where to watch movies across streaming platforms
- 💡 Answer general questions about cinema and film industry
- 🗣️ Multi-turn conversations with context memory
- 🤖 Multi-agent coordination for complex queries
- 🔍 LangSmith tracing for debugging
- 📊 Real-time analytics dashboard
- 🗺️ Visual workflow graphs

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your AWS credentials and OMDB API key
# Add your OMDB_API_KEY (get free key from http://www.omdbapi.com/)
# Optionally add LangSmith API key for tracing
```

### 3. Scrape Movie Data
```bash
python3 scraper.py
```

### 4. Run the Assistant
```bash
python3 app_langgraph.py
```

See `QUICKSTART.md` for detailed instructions and `LANGSMITH_SETUP.md` for tracing setup.

## Data Collection
The scraper uses:
- **OMDB API** for movie details (title, director, cast, runtime, ratings, box office)
- **Smart streaming data generation** based on movie metadata (studio, year, genre, rating)
- **Mock reviews** generated based on IMDb ratings (real review APIs require authentication)

Run `python scraper.py` to collect data for 10 categories with 10 movies each, including streaming availability.

## Example Queries

- "Who directed Inception?"
- "What do people think about Top Gun Maverick?"
- "Recommend a good sci-fi movie"
- "Movies like Interstellar"
- "Is Dune available for free anywhere?"

## Agent Specializations

### MovieDetailsAgent
Handles technical movie information:
- Cast and crew details
- Runtime, release date, studio
- Box office performance
- Awards and nominations

### MovieReviewsAgent  
Analyzes audience opinions:
- IMDb ratings and vote counts
- Review sentiment analysis
- Content warnings
- Worth-watching recommendations

### MovieRecommendationAgent
Provides personalized suggestions:
- Similar movie recommendations
- Mood-based suggestions
- Genre-specific picks
- Comparative analysis

### StreamingAgent
Finds where to watch movies:
- Streaming availability (Netflix, Prime, Hulu, Disney+, HBO Max, Apple TV)
- Rental vs subscription options
- Platform recommendations
- Alternative viewing options

### MovieKnowledgeAgent
General cinema expertise:
- Film history and movements
- Director and actor filmographies
- Industry insights and trivia
- Box office trends

## LangSmith Integration

Enable tracing to debug and monitor your agents:

1. Sign up at https://smith.langchain.com
2. Get your API key
3. Add to `.env`:
```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_PROJECT=movie-assistant-multiagent
```

See `LANGSMITH_SETUP.md` for detailed instructions.

## Technology Stack

- **LangGraph**: Agent workflow orchestration
- **LangSmith**: Tracing and monitoring
- **AWS Bedrock Nova Lite**: LLM inference
- **Gradio**: Web interface
- **OMDB API**: Movie data source

