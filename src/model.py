from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from .config import LLM_MODEL, OPENAI_API_KEY
from .state import TopicSummary

def get_llm_with_schema():
    """
    Initializes the LLM and binds it to the TopicSummary Pydantic schema
    to ensure the output is structured JSON.
    """
    # Initialize the LLM client
    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.2 # Slight temperature for creative parts like analogy/example
    )

    # Bind the Pydantic schema to the LLM
    # This instructs the model to generate a JSON object matching the schema
    llm_with_schema = llm.with_structured_output(TopicSummary)
    return llm_with_schema

def get_summary_prompt():
    """
    Defines the system prompt to guide the LLM's persona and task.
    """
    system_prompt = (
        "You are an expert science communicator and educator. Your goal is to "
        "take a complex topic and explain it in a clear, highly structured, "
        "and engaging manner. You must output a JSON object that strictly "
        "adheres to the provided schema. Do not output any text other than the JSON."
    )
    
    # Placeholder for the user's input topic
    human_template = "Topic to explain: {user_topic}"

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_template)
    ])
# src/model.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.config import LLM_MODEL, OPENAI_API_KEY
from src.state import TopicSummary

def get_llm_with_schema():
    """
    Initializes the LLM and binds it to the TopicSummary Pydantic schema
    to ensure the output is structured JSON.
    """
    # Initialize the LLM client
    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.2 # Slight temperature for creative parts like analogy/example
    )

    # Bind the Pydantic schema to the LLM
    # This instructs the model to generate a JSON object matching the schema
    llm_with_schema = llm.with_structured_output(TopicSummary)
    return llm_with_schema

def get_summary_prompt():
    """
    Defines the system prompt to guide the LLM's persona and task.
    """
    system_prompt = (
        "You are an expert science communicator and educator. Your goal is to "
        "take a complex topic and explain it in a clear, highly structured, "
        "and engaging manner. You must output a JSON object that strictly "
        "adheres to the provided schema. Do not output any text other than the JSON."
    )
    
    # Placeholder for the user's input topic
    human_template = "Topic to explain: {user_topic}"

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_template)
    ])