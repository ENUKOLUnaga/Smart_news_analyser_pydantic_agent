from pydantic_ai import Agent
from schemas.schema import NewsAnalysis
from configuration.config import MODEL

# Create agent
news_agent = Agent(
    MODEL,
    system_prompt="""
    You are a smart AI news analyzer.

    STRICT RULES:
    - DO NOT call any tools or functions
    - ONLY return valid JSON
    - NO explanations

    Format:
    {
      "category": "AI | Tech | Business | Science | Other",
      "summary": "one short sentence",
      "importance_score": number (1-10)
    }
    """
)