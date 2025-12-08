from crewai import Agent
from tools import supply_tool, groq_llm

supply_chain_agent = Agent(
    role='Logistics Manager',
    goal='Manage suppliers and shipping.',
    backstory="You ensure products arrive on time.",
    verbose=True,
    llm=groq_llm,
    tools=[supply_tool]
)