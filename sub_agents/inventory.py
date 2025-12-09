from crewai import Agent
from tools import stock_tool, groq_llm

inventory_agent = Agent(
    role='Inventory Manager',
    goal='Ensure stock levels are healthy.',
    backstory="You are responsible for warehouse stocks.",
    verbose=True,
    llm=groq_llm,
    tools=[stock_tool],
    allow_delegation=False 
)