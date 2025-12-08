import os
from dotenv import load_dotenv
from crewai_tools import tool
from langchain_groq import ChatGroq
from data_manager import data_loader


load_dotenv()


groq_llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")



@tool("Check Inventory")
def stock_tool(query: str):
    """Checks stock levels for a product name."""
    return data_loader.check_stock_level(query)

@tool("Check Pricing")
def price_tool(query: str):
    """Checks historical pricing for a product."""
    return data_loader.get_price_history(query)

@tool("Customer Lookup")
def customer_tool(query: str):
    """Looks up customer details by ID."""
    return data_loader.get_customer_history(query)

@tool("Supply Chain Info")
def supply_tool(query: str):
    """Gets supplier details for a product."""
    return data_loader.get_supplier_info(query)

@tool("Demand Forecast")
def forecast_tool(query: str):
    """Predicts future sales for a product."""
    return data_loader.predict_demand(query)