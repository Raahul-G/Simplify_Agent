# main.py
import os
from typing import TypedDict, Optional
from .config import LLM_MODEL, OPENAI_API_KEY

# Check for API key before importing modules that initialize the LLM
if not os.getenv("OPENAI_API_KEY"):
    print("FATAL ERROR: Please set the OPENAI_API_KEY environment variable.")
    exit(1)

from src.agent import agent_app
from src.state import GraphState, TopicSummary

def run_agent(topic: str):
    """
    Runs the compiled LangGraph agent with a specific topic.
    """
    print(f"\n--- Starting Agent for Topic: '{topic}' ---")

    # The initial state contains only the user's topic
    initial_state: GraphState = {"user_topic": topic, "final_summary": None}

    # Invoke the agent
    final_state: GraphState = agent_app.invoke(initial_state)

    # --- Print Final Output ---
    print("\n" + "="*50)
    print("--- FINAL RESULT ---")
    
    summary: Optional[TopicSummary] = final_state.get("final_summary")
    
    if summary:
        print(f"Topic: {summary.topic}")
        print("\n--- Simplified Text ---")
        print(summary.simplified_text)
        print("\n--- Analogy ---")
        print(summary.analogy)
        print("\n--- Example ---")
        print(summary.example)
    else:
        print("Agent failed to produce a structured summary. Check logs for errors.")

    print("="*50)


if __name__ == "__main__":
    # Example complex topic (Quantum Entanglement used in the original notebook)
    # You can change this to any topic you want!
    COMPLEX_TOPIC = input("Enter a complex topic to simplify: ")
    
    # Run the agent 
    run_agent(COMPLEX_TOPIC)