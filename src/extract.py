import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
STOCK_SYMBOL = "AAPL"
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"

def fetch_stock_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

if __name__ == "__main__":
    stock_data = fetch_stock_data()
    print(stock_data)
