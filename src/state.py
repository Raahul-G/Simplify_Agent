from typing import TypedDict, Optional
from pydantic import BaseModel, Field

# --- Structured Output Schema ---
class TopicSummary(BaseModel):
    """
    Schema for the final, structured output of the agent.
    This ensures the LLM's response is easily parsable and high-quality.
    """
    topic: str = Field(description="The original topic provided by the user.")
    simplified_text: str = Field(
        description="A clear, simple explanation of the topic, suitable for a 10-year-old."
    )
    analogy: str = Field(
        description="A simple, relatable analogy to explain the core concept."
    )
    example: str = Field(
        description="A real-world or fictional example that illustrates the topic."
    )

# --- Graph State ---
class GraphState(TypedDict):
    """
    Represents the state of the graph's execution.
    Data flow across nodes is managed by updating this dictionary.
    """
    # The complex topic provided by the user
    user_topic: str
    # The final, structured output from the LLM
    final_summary: Optional[TopicSummary]
# src/state.py
from typing import TypedDict, Optional
from pydantic import BaseModel, Field

# --- Structured Output Schema ---
class TopicSummary(BaseModel):
    """
    Schema for the final, structured output of the agent.
    This ensures the LLM's response is easily parsable and high-quality.
    """
    topic: str = Field(description="The original topic provided by the user.")
    simplified_text: str = Field(
        description="A clear, simple explanation of the topic, suitable for a 10-year-old."
    )
    analogy: str = Field(
        description="A simple, relatable analogy to explain the core concept."
    )
    example: str = Field(
        description="A real-world or fictional example that illustrates the topic."
    )

# --- Graph State ---
class GraphState(TypedDict):
    """
    Represents the state of the graph's execution.
    Data flow across nodes is managed by updating this dictionary.
    """
    # The complex topic provided by the user
    user_topic: str
    # The final, structured output from the LLM
    final_summary: Optional[TopicSummary]