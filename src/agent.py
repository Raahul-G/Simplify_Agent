import asyncio
from langgraph.graph import StateGraph, END
from langchain_core.exceptions import OutputParserException
from .state import GraphState, TopicSummary
from .model import get_llm_with_schema, get_summary_prompt

# --- Initialize LLM and Prompt ---
llm_with_schema = get_llm_with_schema()
summary_prompt = get_summary_prompt()

# --- Graph Nodes ---

def generate_summary_node(state: GraphState) -> dict:
    """
    Calls the LLM with the structured output schema to generate the summary.
    This node attempts to produce the final, structured output.
    """
    print(f"--- Running Node: Generate Summary for '{state['user_topic']}' ---")
    
    # The state is used as the input variables for the prompt
    chain = summary_prompt | llm_with_schema
    
    try:
        # Invoke the chain, which forces structured JSON output
        result: TopicSummary = chain.invoke(state)
        print("Summary generated successfully.")
        
        # Update the state with the final structured result
        return {"final_summary": result}
        
    except OutputParserException as e:
        # If the LLM fails to produce valid JSON, handle the error
        print(f"Error: OutputParserException encountered: {e}")
        # Optionally, you could add logic here to re-prompt the LLM
        # For this simple example, we will stop and report the error.
        return {"final_summary": None}


# --- Graph Edges (Router) ---

def decide_to_end(state: GraphState) -> str:
    """
    A router function that determines the next step.
    Since this is a simple, single-step agent, it always proceeds to END.
    """
    print("--- Running Router: Decide to End ---")
    
    if state.get("final_summary"):
        # If we have a summary, we are done
        return "end"
    else:
        # If the summary failed to generate (e.g., due to parsing error), we also stop
        return "end"


# --- Build the LangGraph Workflow ---

def build_agent_graph():
    """
    Assembles the LangGraph workflow. 
    """
    print("--- Building LangGraph Agent ---")
    
    # 1. Define the graph state
    workflow = StateGraph(GraphState)

    # 2. Add nodes
    # The main node is the only step that generates content
    workflow.add_node("summary_generator", generate_summary_node)

    # 3. Set the entry point (first node to run)
    workflow.set_entry_point("summary_generator")

    # 4. Add the edge to the router
    # After the summary is generated, we call the router to decide the next step
    workflow.add_conditional_edges(
        "summary_generator",
        decide_to_end,
        {
            "end": END,  # If the router returns "end", stop the graph
        }
    )

    # 5. Compile the graph into a runnable application
    app = workflow.compile()
    print("--- LangGraph Agent Compiled ---")
    return app

# Compile the final agent application
agent_app = build_agent_graph()
# src/agent.py
import asyncio
from langgraph.graph import StateGraph, END
from langchain_core.exceptions import OutputParserException
from src.state import GraphState, TopicSummary
from src.model import get_llm_with_schema, get_summary_prompt

# --- Initialize LLM and Prompt ---
llm_with_schema = get_llm_with_schema()
summary_prompt = get_summary_prompt()

# --- Graph Nodes ---

def generate_summary_node(state: GraphState) -> dict:
    """
    Calls the LLM with the structured output schema to generate the summary.
    This node attempts to produce the final, structured output.
    """
    print(f"--- Running Node: Generate Summary for '{state['user_topic']}' ---")
    
    # The state is used as the input variables for the prompt
    chain = summary_prompt | llm_with_schema
    
    try:
        # Invoke the chain, which forces structured JSON output
        result: TopicSummary = chain.invoke(state)
        print("Summary generated successfully.")
        
        # Update the state with the final structured result
        return {"final_summary": result}
        
    except OutputParserException as e:
        # If the LLM fails to produce valid JSON, handle the error
        print(f"Error: OutputParserException encountered: {e}")
        # Optionally, you could add logic here to re-prompt the LLM
        # For this simple example, we will stop and report the error.
        return {"final_summary": None}


# --- Graph Edges (Router) ---

def decide_to_end(state: GraphState) -> str:
    """
    A router function that determines the next step.
    Since this is a simple, single-step agent, it always proceeds to END.
    """
    print("--- Running Router: Decide to End ---")
    
    if state.get("final_summary"):
        # If we have a summary, we are done
        return "end"
    else:
        # If the summary failed to generate (e.g., due to parsing error), we also stop
        return "end"


# --- Build the LangGraph Workflow ---

def build_agent_graph():
    """
    Assembles the LangGraph workflow. 
    """
    print("--- Building LangGraph Agent ---")
    
    # 1. Define the graph state
    workflow = StateGraph(GraphState)

    # 2. Add nodes
    # The main node is the only step that generates content
    workflow.add_node("summary_generator", generate_summary_node)

    # 3. Set the entry point (first node to run)
    workflow.set_entry_point("summary_generator")

    # 4. Add the edge to the router
    # After the summary is generated, we call the router to decide the next step
    workflow.add_conditional_edges(
        "summary_generator",
        decide_to_end,
        {
            "end": END,  # If the router returns "end", stop the graph
        }
    )

    # 5. Compile the graph into a runnable application
    app = workflow.compile()
    print("--- LangGraph Agent Compiled ---")
    return app

# Compile the final agent application
agent_app = build_agent_graph()