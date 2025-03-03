import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Configuration
API_KEY = os.getenv("ALPHA_API_KEY")  # Load API Key from .env
STOCK_SYMBOL = "AAPL"  # You can change this to any stock symbol
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"

# Output Directory
RAW_DATA_PATH = "data/raw_stock_data.json"

def fetch_stock_data():
    """Fetch daily stock market data from Alpha Vantage API."""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def save_raw_data(data):
    """Save raw stock data as JSON file."""
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    with open(RAW_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Raw data saved at: {RAW_DATA_PATH}")

if __name__ == "__main__":
    stock_data = fetch_stock_data()
    if stock_data:
        save_raw_data(stock_data)
