from crewai import Crew, Task, Process

# Import Agents from their specific files
from sub_agents.inventory import inventory_agent
from sub_agents.pricing import pricing_agent
from sub_agents.support import customer_service_agent
from sub_agents.supply import supply_chain_agent
from sub_agents.forecasting import forecasting_agent

# 1. Define Tasks
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

# 2. Assemble Crew
crew = Crew(
    agents=[inventory_agent, pricing_agent, forecasting_agent],
    tasks=[task_inv, task_price, task_fc],
    process=Process.sequential,
    verbose=True
)

# 3. Run
print("Starting Modular Agents...")
result = crew.kickoff()
print(result)