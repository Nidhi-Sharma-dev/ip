from crewai import Agent
from tools import price_tool, groq_llm

pricing_agent = Agent(
    role='Pricing Analyst',
    goal='Determine optimal product prices.',
    backstory="You analyze historical prices to recommend strategies.",
    verbose=True,
    llm=groq_llm,
    tools=[price_tool]
)