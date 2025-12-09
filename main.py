import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

from crewai import Crew, Task, Process, Agent
from tools import groq_llm

# Import Agents from their specific files
from sub_agents.inventory import inventory_agent
from sub_agents.pricing import pricing_agent
from sub_agents.support import customer_service_agent
from sub_agents.supply import supply_chain_agent
from sub_agents.forecasting import forecasting_agent

# 1. Define Tasks with explicit agent assignment
task_inv = Task(
    description="Check stock for 'WHITE METAL LANTERN'.",
    expected_output="Stock status.",
    agent=inventory_agent
)

task_price = Task(
    description="Check price history for 'WHITE METAL LANTERN'.",
    expected_output="Price summary.",
    agent=pricing_agent
)

task_fc = Task(
    description="Forecast demand for 'WHITE METAL LANTERN'.",
    expected_output="Prediction.",
    agent=forecasting_agent
)

# 2. Assemble Crew with explicit manager_llm
crew = Crew(
    agents=[inventory_agent, pricing_agent, forecasting_agent],
    tasks=[task_inv, task_price, task_fc],
    process=Process.sequential,
    verbose=True,
    manager_llm=groq_llm,  # Force Groq for crew manager
)

# 3. Run
if __name__ == "__main__":
    print("Starting Modular Agents with Groq...")
    try:
        result = crew.kickoff()
        print("\n" + "="*50)
        print("FINAL RESULT:")
        print("="*50)
        print(result)
    except Exception as e:
        print(f"Error occurred: {e}")