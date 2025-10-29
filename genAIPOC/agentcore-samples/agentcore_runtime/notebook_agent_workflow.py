#!/usr/bin/env python3
"""
LlamaIndex Workflow-Based Multi-Agent System
Uses LlamaIndex's Workflow framework for explicit multi-agent orchestration
This is the BEST approach - combines control with framework benefits!
"""
import os
import time
import textwrap
import pathlib
from typing import Any, Dict, List, Optional
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.core.workflow import (
    Workflow,
    StartEvent,
    StopEvent,
    step,
    Event,
    Context
)
from llama_index.embeddings.bedrock import BedrockEmbedding
from llama_index.llms.bedrock import Bedrock

# Configuration
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "us.anthropic.claude-sonnet-4-20250514-v1:0")
EMBEDDINGS_MODEL_ID = os.getenv("EMBEDDINGS_MODEL_ID", "amazon.titan-embed-text-v2:0")
RAG_TOP_K = int(os.getenv("RAG_TOP_K", "4"))
DATA_DIR = os.getenv("DATA_DIR", "./data")
PERSIST_DIR = "./storage"

# ============================================================================
# EVENTS: Define the data flow between agents
# ============================================================================

class PlanningCompleteEvent(Event):
    """Event fired when planning is complete"""
    subtasks: List[str]
    original_question: str

class ResearchCompleteEvent(Event):
    """Event fired when research is complete"""
    subtask: str
    answer: str
    citations: List[Dict[str, Any]]

class AllResearchCompleteEvent(Event):
    """Event fired when all research is complete"""
    original_question: str
    research_results: List[Dict[str, Any]]

class VerificationCompleteEvent(Event):
    """Event fired when verification is complete"""
    original_question: str
    research_results: List[Dict[str, Any]]
    verification: Dict[str, Any]

# ============================================================================
# SETUP: LlamaIndex Configuration
# ============================================================================

def _llm():
    """Get Bedrock LLM instance"""
    return Bedrock(
        model=BEDROCK_MODEL_ID,
        region_name=AWS_REGION,
        context_size=200000
    )

def _create_sample_data():
    """Create sample runbook data"""
    pathlib.Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    
    samples = {
        "incident_response_bruteforce.md": """# EC2 Brute Force Incident - First Hour Checklist
- Confirm the GuardDuty finding and source IP reputation.
- Isolate the EC2 instance from the network (quarantine security group).
- Rotate instance profile credentials if present.
- Capture volatile data; ensure detailed CloudTrail logs are enabled.
""",
        "network_isolation.md": """# Network Isolation Steps
- Apply a restrictive security group that allows only admin IPs.
- Optionally detach from load balancer and auto-scaling group.
- Snapshot EBS volumes for later forensics.
""",
        "iam_forensics.md": """# IAM Forensics Checklist
- Enumerate IAM role assumptions related to the instance profile.
- Review CloudTrail for unusual API calls.
- Rotate access keys for impacted principals.
"""
    }
    
    for name, content in samples.items():
        with open(os.path.join(DATA_DIR, name), "w") as f:
            f.write(textwrap.dedent(content).strip() + "\n")

def _ensure_index():
    """Ensure vector index exists"""
    Settings.embed_model = BedrockEmbedding(model=EMBEDDINGS_MODEL_ID, region_name=AWS_REGION)
    Settings.llm = _llm()
    
    if not os.path.exists(DATA_DIR):
        _create_sample_data()
    
    if not os.path.isdir(PERSIST_DIR):
        docs = SimpleDirectoryReader(DATA_DIR).load_data()
        idx = VectorStoreIndex.from_documents(docs)
        idx.storage_context.persist(persist_dir=PERSIST_DIR)
    
    storage = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    return load_index_from_storage(storage)

# Global index
INDEX = None

def _get_index():
    """Get or create the vector index"""
    global INDEX
    if INDEX is None:
        INDEX = _ensure_index()
    return INDEX

# ============================================================================
# WORKFLOW: Multi-Agent Orchestration
# ============================================================================

class MultiAgentWorkflow(Workflow):
    """
    Multi-Agent Workflow for Incident Response
    
    Flow: Start → Planner → Researcher (parallel) → Verifier → Presenter → Stop
    
    This gives you:
    - Explicit control flow (like your original)
    - LlamaIndex framework benefits
    - Event-driven architecture
    - Async support for parallel operations
    """
    
    @step
    async def planner_agent(self, ctx: Context, ev: StartEvent) -> PlanningCompleteEvent:
        """
        Planner Agent: Decompose question into subtasks
        
        This is the first step - receives the user's question and breaks it down
        """
        question = ev.get("question", "")
        
        print(f"\n📋 PLANNER AGENT")
        print(f"{'─'*60}")
        print(f"Question: {question}")
        
        # Store original question in context
        await ctx.set("original_question", question)
        
        # Plan the subtasks
        prompt = f"""You are a planning expert for incident response.
Decompose this question into 2-4 specific, actionable subtasks.
Return ONLY a numbered list, nothing else.

Question: {question}

Format:
1. First subtask
2. Second subtask
3. Third subtask"""
        
        response = _llm().complete(prompt).text.strip()
        
        # Parse subtasks
        subtasks = []
        for line in response.splitlines():
            line = line.strip()
            if line and line[0].isdigit():
                subtasks.append(line.split('.', 1)[-1].strip())
        
        print(f"✅ Planned {len(subtasks)} subtasks:")
        for i, st in enumerate(subtasks, 1):
            print(f"   {i}. {st}")
        
        return PlanningCompleteEvent(
            subtasks=subtasks,
            original_question=question
        )
    
    @step
    async def researcher_agent(
        self, 
        ctx: Context, 
        ev: PlanningCompleteEvent
    ) -> AllResearchCompleteEvent:
        """
        Researcher Agent: Research each subtask using RAG
        
        This step receives the subtasks and researches each one
        """
        print(f"\n🔍 RESEARCHER AGENT")
        print(f"{'─'*60}")
        
        index = _get_index()
        query_engine = index.as_query_engine(
            similarity_top_k=RAG_TOP_K,
            llm=_llm()
        )
        
        research_results = []
        
        for i, subtask in enumerate(ev.subtasks, 1):
            print(f"Researching {i}/{len(ev.subtasks)}: {subtask}")
            
            # Query RAG
            response = query_engine.query(subtask)
            
            # Extract citations
            citations = []
            for node in getattr(response, "source_nodes", []):
                meta = node.node.metadata or {}
                citations.append({
                    "file_name": meta.get("file_name", ""),
                    "score": getattr(node, "score", None)
                })
            
            research_results.append({
                "subtask": subtask,
                "answer": str(response),
                "citations": citations
            })
            
            print(f"   ✅ Found {len(citations)} citations")
        
        print(f"✅ Research complete for all {len(ev.subtasks)} subtasks")
        
        return AllResearchCompleteEvent(
            original_question=ev.original_question,
            research_results=research_results
        )
    
    @step
    async def verifier_agent(
        self,
        ctx: Context,
        ev: AllResearchCompleteEvent
    ) -> VerificationCompleteEvent:
        """
        Verifier Agent: Check quality of research results
        
        This step validates the research before presentation
        """
        print(f"\n✓ VERIFIER AGENT")
        print(f"{'─'*60}")
        
        # Merge all results
        merged_answer = "\n\n".join([r["answer"] for r in ev.research_results])
        merged_citations = [c for r in ev.research_results for c in r["citations"]]
        
        # Quality checks
        flags = []
        
        if not merged_answer or len(merged_answer.strip()) < 50:
            flags.append("answer_too_short")
        
        if not merged_citations:
            flags.append("no_citations")
        
        # Check for structure
        if not any(marker in merged_answer for marker in ['•', '-', '1.', '2.', '\n']):
            flags.append("lacks_structure")
        
        verification = {
            "pass": len(flags) == 0,
            "flags": flags,
            "answer_length": len(merged_answer),
            "citations_count": len(merged_citations)
        }
        
        if verification["pass"]:
            print(f"✅ Quality verified:")
            print(f"   • Answer length: {verification['answer_length']} chars")
            print(f"   • Citations: {verification['citations_count']} sources")
        else:
            print(f"⚠️ Quality issues found: {', '.join(flags)}")
        
        return VerificationCompleteEvent(
            original_question=ev.original_question,
            research_results=ev.research_results,
            verification=verification
        )
    
    @step
    async def presenter_agent(
        self,
        ctx: Context,
        ev: VerificationCompleteEvent
    ) -> StopEvent:
        """
        Presenter Agent: Synthesize final answer
        
        This is the final step - creates the polished response
        """
        print(f"\n📊 PRESENTER AGENT")
        print(f"{'─'*60}")
        
        # Build context from research
        context_chunks = []
        for r in ev.research_results:
            context_chunks.append(
                f"Subtask: {r['subtask']}\nAnswer:\n{r['answer']}\n---"
            )
        merged_context = "\n".join(context_chunks)
        
        # Synthesize final answer
        prompt = f"""You are a presentation expert for incident response guidance.

Synthesize the research results below into a clear, actionable answer.

Requirements:
- Provide 6-8 bullet points maximum
- Each bullet should be specific and actionable
- Ground all information in the provided context
- End with a "Sources:" section listing all referenced documents
- Use professional security terminology

Original Question: {ev.original_question}

Research Context:
{merged_context}

Provide your synthesized answer now:"""
        
        final_answer = _llm().complete(prompt).text.strip()
        
        # Add sources
        sources = set()
        for r in ev.research_results:
            for c in r["citations"]:
                if c.get("file_name"):
                    sources.add(c["file_name"])
        
        if sources and "Sources:" not in final_answer:
            final_answer += "\n\nSources: " + ", ".join(sorted(sources))
        
        print(f"✅ Final answer synthesized ({len(final_answer)} chars)")
        
        # Collect all citations
        all_citations = [c for r in ev.research_results for c in r["citations"]]
        
        # Build trace
        trace = {
            "workflow_type": "LlamaIndex Workflow",
            "agents_used": ["Planner", "Researcher", "Verifier", "Presenter"],
            "subtasks": [r["subtask"] for r in ev.research_results],
            "verification": ev.verification,
            "citations_count": len(all_citations)
        }
        
        # Return final result
        return StopEvent(
            result={
                "answer": final_answer,
                "citations": all_citations,
                "trace": trace
            }
        )

# ============================================================================
# PUBLIC API: Run the workflow
# ============================================================================

async def run_multi_agent_async(user_question: str) -> Dict[str, Any]:
    """
    Run the multi-agent workflow (async version)
    
    Args:
        user_question: The user's question
        
    Returns:
        Dict with answer, citations, and trace
    """
    print(f"\n{'='*80}")
    print(f"🤖 Multi-Agent Workflow Processing")
    print(f"{'='*80}")
    print(f"Question: {user_question}")
    print(f"{'='*80}")
    
    start_time = time.time()
    
    # Create and run the workflow
    workflow = MultiAgentWorkflow(timeout=300, verbose=False)
    result = await workflow.run(question=user_question)
    
    duration = time.time() - start_time
    
    print(f"\n{'='*80}")
    print(f"✅ Workflow Complete ({duration:.2f}s)")
    print(f"{'='*80}\n")
    
    # Add duration to trace
    result["trace"]["duration_seconds"] = round(duration, 2)
    
    return result

def run_multi_agent(user_question: str) -> Dict[str, Any]:
    """
    Run the multi-agent workflow (sync wrapper)
    
    Args:
        user_question: The user's question
        
    Returns:
        Dict with answer, citations, and trace
    """
    import asyncio
    import nest_asyncio
    
    # Allow nested event loops (for AgentCore compatibility)
    try:
        nest_asyncio.apply()
    except:
        pass
    
    # Run the async workflow
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If loop is already running, use nest_asyncio
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, run_multi_agent_async(user_question))
                return future.result()
        else:
            return loop.run_until_complete(run_multi_agent_async(user_question))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(run_multi_agent_async(user_question))

# ============================================================================
# BACKWARD COMPATIBILITY
# ============================================================================

def plan(q: str) -> List[str]:
    """Legacy function for compatibility"""
    result = run_multi_agent(q)
    return result["trace"]["subtasks"]

def rag_query(q: str) -> Dict[str, Any]:
    """Legacy function for compatibility"""
    index = _get_index()
    query_engine = index.as_query_engine(similarity_top_k=RAG_TOP_K, llm=_llm())
    response = query_engine.query(q)
    
    citations = []
    for sn in getattr(response, "source_nodes", []):
        meta = sn.node.metadata or {}
        citations.append({
            "file_name": meta.get("file_name", ""),
            "score": getattr(sn, "score", None)
        })
    
    return {
        "answer": str(response),
        "citations": citations,
        "timings": {}
    }
