import asyncio
import json
from schemas.schema import NewsAnalysis
from agent.my_agent import news_agent

async def analyze(text: str):
    """Run agent and return parsed result."""
    result = await news_agent.run(text)

    raw_output = result.output

    # Clean possible markdown
    raw_output = raw_output.strip().strip("```json").strip("```")

    # Convert to dict
    data = json.loads(raw_output)

    # Convert to Pydantic model
    return NewsAnalysis(**data)

async def display(result):
    print("\n Analysis Result:")
    print(f" Category: {result.category}")
    print(f" Summary: {result.summary}")
    print(f" Importance Score: {result.importance_score}")
    print("-" * 50)

async def main():
    print("Welcome to the Smart News Analyzer!")

    while True:
        text=input("\nEnter news text (or 'exit' to quit): ").strip()
        if text.lower() == 'exit':
            print("Goodbye!")
            break

        if not text:
            print("Please enter some news text.")
            continue

        try:
            result = await analyze(text)
            await display(result)
        
        except Exception as e:
            print(f"Error analyzing news: {e}")

if __name__ == "__main__":
    asyncio.run(main())
