import os
from dotenv import load_dotenv
from crewai.tools import BaseTool
from crewai import LLM
from data_manager import data_loader
from typing import Type
from pydantic import BaseModel, Field


load_dotenv()

groq_llm = LLM(model="groq/llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))


# Define input schema
class ProductInput(BaseModel):
    query: str = Field(..., description="Product name or customer ID to query")


class StockTool(BaseTool):
    name: str = "Check Inventory"
    description: str = "Checks stock levels for a product name."
    args_schema: Type[BaseModel] = ProductInput

    def _run(self, query: str) -> str:
        return data_loader.check_stock_level(query)


class PriceTool(BaseTool):
    name: str = "Check Pricing"
    description: str = "Checks historical pricing for a product."
    args_schema: Type[BaseModel] = ProductInput

    def _run(self, query: str) -> str:
        return data_loader.get_price_history(query)


class CustomerTool(BaseTool):
    name: str = "Customer Lookup"
    description: str = "Looks up customer details by ID."
    args_schema: Type[BaseModel] = ProductInput

    def _run(self, query: str) -> str:
        return data_loader.get_customer_history(query)


class SupplyTool(BaseTool):
    name: str = "Supply Chain Info"
    description: str = "Gets supplier details for a product."
    args_schema: Type[BaseModel] = ProductInput

    def _run(self, query: str) -> str:
        return data_loader.get_supplier_info(query)


class ForecastTool(BaseTool):
    name: str = "Demand Forecast"
    description: str = "Predicts future sales for a product."
    args_schema: Type[BaseModel] = ProductInput

    def _run(self, query: str) -> str:
        return data_loader.predict_demand(query)


# Create instances
stock_tool = StockTool()
price_tool = PriceTool()
customer_tool = CustomerTool()
supply_tool = SupplyTool()
forecast_tool = ForecastTool()