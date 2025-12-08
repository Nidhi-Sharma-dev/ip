from crewai import Agent
from tools import forecast_tool, groq_llm

forecasting_agent = Agent(
    role='Demand Planner',
    goal='Predict future sales.',
    backstory="You use math to predict sales trends.",
    verbose=True,
    llm=groq_llm,
    tools=[forecast_tool]
)