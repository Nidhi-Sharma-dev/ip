from crewai import Agent
from tools import customer_tool, groq_llm

customer_service_agent = Agent(
    role='Customer Support Lead',
    goal='Resolve customer inquiries.',
    backstory="You are friendly and look up customer data to help them.",
    verbose=True,
    llm=groq_llm,
    tools=[customer_tool]
)