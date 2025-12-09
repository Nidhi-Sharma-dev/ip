import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from crewai import Crew, Task, Process, Agent
from tools import groq_llm


from sub_agents.inventory import inventory_agent
from sub_agents.pricing import pricing_agent
from sub_agents.support import customer_service_agent
from sub_agents.supply import supply_chain_agent
from sub_agents.forecasting import forecasting_agent


product_name = input("What product would you like to analyze? ")


task_inv = Task(
    description=f"Check stock levels for '{product_name}' and provide the current stock status with quantity and health indicators.",
    expected_output="A detailed stock status report including current quantity, stock health (CRITICAL LOW/HEALTHY), and any inventory alerts or recommendations.",
    agent=inventory_agent
)

task_price = Task(
    description=f"Analyze price history for '{product_name}' and provide comprehensive pricing information.",
    expected_output="A price analysis report with average price, maximum price, price trends, and pricing recommendations.",
    agent=pricing_agent
)

task_fc = Task(
    description=f"Forecast demand for '{product_name}' and predict future sales trends.",
    expected_output="A demand forecast report with predicted units for next month, trend analysis, and sales projections.",
    agent=forecasting_agent
)

#  Assemble Crew with explicit manager_llm
crew = Crew(
    agents=[inventory_agent, pricing_agent, forecasting_agent],
    tasks=[task_inv, task_price, task_fc],
    process=Process.sequential,
    verbose=True,
    manager_llm=groq_llm,  # Force Groq for crew manager
)

#  Run
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