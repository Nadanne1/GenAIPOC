# 📚 Multi-Agent Book Assistant

A production-ready AI assistant using **LangGraph**, **AWS Bedrock Nova Lite**, and **LangSmith** for intelligent book queries with full observability.

## Three Implementations

### 1. Single-Agent (app.py)
Simple routing with LangGraph workflows - good for learning basics

### 2. Multi-Agent Custom (app_multiagent.py)
Custom supervisor pattern with agent memory - good for understanding multi-agent concepts

### 3. LangGraph Multi-Agent (app_langgraph.py) ⭐ RECOMMENDED
Full LangGraph StateGraph implementation with LangSmith integration:
- **Proper State Management**: TypedDict state across all nodes
- **Supervisor Node**: Intelligent routing with LLM
- **Specialist Agent Nodes**: BookDetails, Reviews, Recommendation, General
- **LangSmith Tracing**: Full observability and debugging
- **Visual Workflow**: See execution graph
- **Production Ready**: Scalable and maintainable

## Features
- 📚 Query book details and specifications
- ⭐ Get book reviews and ratings
- 🎯 Personalized book recommendations
- 💡 Answer general questions about books
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
# Edit .env with your AWS credentials
# Optionally add LangSmith API key for tracing
```

### 3. Scrape Book Data
```bash
python3 scraper.py
```

### 4. Run the Assistant
```bash
# Recommended: LangGraph with LangSmith
python3 app_langgraph.py

# Or try other implementations:
python3 app.py                # Simple single-agent
python3 app_multiagent.py     # Custom multi-agent
```

See `QUICKSTART.md` for detailed instructions and `LANGSMITH_SETUP.md` for tracing setup.

## Data Collection
The scraper uses:
- **Google Books API** for book details (title, author, pages, description, ratings)
- **Mock reviews** generated based on ratings (real review APIs require authentication)

Run `python scraper.py` to collect data for 10 categories with 10 books each.

## Example Queries
- "What's the page count of Harry Potter?"
- "What do readers think about 1984?"
- "Recommend a good science fiction book"
- "Compare reviews of two fantasy books" (multi-agent)
- "Who wrote The Great Gatsby?"

## Documentation

- 📖 `QUICKSTART.md` - Step-by-step setup guide
- 🏗️ `ARCHITECTURE.md` - Multi-agent design details
- 🔍 `LANGSMITH_SETUP.md` - LangSmith tracing configuration
- 📊 `IMPLEMENTATIONS.md` - Compare all three implementations
- 🗂️ `PROJECT_STRUCTURE.md` - File organization

## LangSmith Integration

Enable tracing to debug and monitor your agents:

1. Sign up at https://smith.langchain.com
2. Get your API key
3. Add to `.env`:
```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_PROJECT=book-assistant-multiagent
```

See `LANGSMITH_SETUP.md` for detailed instructions.

## Technology Stack

- **LangGraph**: Agent workflow orchestration
- **LangSmith**: Tracing and monitoring
- **AWS Bedrock Nova Lite**: LLM inference
- **Gradio**: Web interface
- **Google Books API**: Book data source
