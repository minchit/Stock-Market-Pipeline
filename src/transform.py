import json
import pandas as pd
import os

# Input and Output file paths
RAW_DATA_PATH = "data/raw_stock_data.json"
PROCESSED_DATA_PATH = "data/processed_stock_data.csv"

def load_raw_data():
    """Load raw stock data from JSON file."""
    with open(RAW_DATA_PATH, "r") as f:
        data = json.load(f)
    return data

def transform_data(data):
    """Transform raw stock data into a structured Pandas DataFrame."""
    # Extract time series data
    time_series = data.get("Time Series (Daily)", {})

    if not time_series:
        print("No time series data found.")
        return None

    # Convert JSON to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient="index")
    
    # Rename columns for clarity
    df.rename(columns={
        "1. open": "open_price",
        "2. high": "high_price",
        "3. low": "low_price",
        "4. close": "close_price",
        "5. volume": "volume"
    }, inplace=True)

    # Convert index to Date format
    df.index = pd.to_datetime(df.index)

    # Convert all columns to float type
    df = df.astype(float)

    return df

def save_transformed_data(df):
    """Save the transformed DataFrame as a CSV file."""
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH)
    print(f"Transformed data saved at: {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    raw_data = load_raw_data()
    transformed_df = transform_data(raw_data)

    if transformed_df is not None:
        save_transformed_data(transformed_df)
