import pandas as pd
import numpy as np

class RetailDataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None
        
    def load_data(self):
        try:
            self.df = pd.read_csv(self.filepath, encoding='latin1')
            self.df = self.df.dropna(subset=['CustomerID'])
            self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'])
            print("Data Loaded Successfully!")
        except FileNotFoundError:
            print(f"Error: File not found at {self.filepath}")
            self.df = pd.DataFrame()

    def check_stock_level(self, product_name: str):
        if self.df is None: self.load_data()
        item = self.df[self.df['Description'].str.contains(product_name, case=False, na=False)].head(1)
        if item.empty: return "Product not found."
        total_sold = self.df[self.df['Description'] == item.iloc[0]['Description']]['Quantity'].sum()
        current_stock = 2000 - total_sold # Mock initial stock
        status = "CRITICAL LOW" if current_stock < 100 else "HEALTHY"
        return f"Product: {item.iloc[0]['Description']} | In Stock: {current_stock} ({status})"

    def get_price_history(self, product_name: str):
        if self.df is None: self.load_data()
        item = self.df[self.df['Description'].str.contains(product_name, case=False, na=False)]
        if item.empty: return "No price history."
        return f"Avg Price: ${item['UnitPrice'].mean():.2f} | Max: ${item['UnitPrice'].max()}"

    def get_customer_history(self, customer_id: str):
        if self.df is None: self.load_data()
        cust = self.df[self.df['CustomerID'] == float(customer_id)]
        if cust.empty: return "Customer not found."
        return f"Customer {customer_id}: Total Spend: ${cust['Quantity'].sum() * cust['UnitPrice'].mean():.2f}"

    def get_supplier_info(self, product_name: str):
        return f"Supplier for '{product_name}': Global Logistics Ltd. Lead time: 14 days."

    def predict_demand(self, product_name: str):
        if self.df is None: self.load_data()
        item = self.df[self.df['Description'].str.contains(product_name, case=False, na=False)]
        if item.empty: return "No data."
        return f"Forecast: Expect {int(item['Quantity'].sum() * 1.1)} units demand next month."

# Instance
data_loader = RetailDataLoader('data/online_retail.csv')