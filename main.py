

from fastapi import FastAPI, HTTPException
import requests
from typing import Dict, List
from datetime import datetime

app = FastAPI()


API_KEY = 'OPTZCOC5P8PQJ17C'

# In-memory cache dictionary to store data
cache = {}


# Function to fetch stock data from the AlphaVantage API
def fetch_stock_data(symbol: str):
    # Check cache for existing data
    if symbol in cache:
        return cache[symbol]

    # AlphaVantage API endpoint URL
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Check if there was an error in the API response
    if 'Error Message' in data:
        raise HTTPException(status_code=404, detail="Symbol not found in AlphaVantage API.")

    # Store data in cache
    cache[symbol] = data

    # Return fetched data
    return data


# Endpoint: Lookup
@app.get("/lookup")
async def lookup(symbol: str, date: str) -> Dict[str, float]:
    # Fetch stock data
    data = fetch_stock_data(symbol)

    # Check if the date exists in data
    time_series = data.get('Time Series (Daily)')
    if time_series is None or date not in time_series:
        raise HTTPException(status_code=404, detail="Date not found in data.")

    # Retrieve data for the given date
    daily_data = time_series[date]

    # Return the required fields
    return {
        "open": float(daily_data["1. open"]),
        "high": float(daily_data["2. high"]),
        "low": float(daily_data["3. low"]),
        "close": float(daily_data["4. close"]),
        "volume": int(daily_data["5. volume"])
    }


# Endpoint: Min
@app.get("/min")
async def min(symbol: str, n: int) -> Dict[str, float]:
    # Fetch stock data
    data = fetch_stock_data(symbol)

    # Get the last 'n' data points
    time_series = data.get('Time Series (Daily)')
    if time_series is None:
        raise HTTPException(status_code=404, detail="No data available for the specified symbol.")

    # Get the list of dates sorted in reverse order (most recent first)
    dates = sorted(time_series.keys(), reverse=True)[:n]
    daily_data_list = [time_series[date] for date in dates]

    # Check if there are any data points in the daily_data_list
    if not daily_data_list:
        raise HTTPException(status_code=404, detail="No data points found in the specified range.")

    # Calculate the lowest low price in the last 'n' data points
    lowest_low = float('inf')  # Start with infinity as initial value
    for daily_data in daily_data_list:
        low_price = float(daily_data["3. low"])
        if low_price < lowest_low:
            lowest_low = low_price

    # Return the lowest low price
    return {"min": lowest_low}


# Endpoint: Max
@app.get("/max")
async def max(symbol: str, n: int) -> Dict[str, float]:
    # Fetch stock data
    data = fetch_stock_data(symbol)

    # Get the last 'n' data points
    time_series = data.get('Time Series (Daily)')
    if time_series is None:
        raise HTTPException(status_code=404, detail="No data available for the specified symbol.")

    # Get the list of dates sorted in reverse order (most recent first)
    dates = sorted(time_series.keys(), reverse=True)[:n]
    daily_data_list = [time_series[date] for date in dates]

    # Check if there are any data points in the daily_data_list
    if not daily_data_list:
        raise HTTPException(status_code=404, detail="No data points found in the specified range.")

    # Calculate the maximum high price in the last 'n' data points
    highest_high = float('-inf')  # Start with negative infinity as initial value
    for daily_data in daily_data_list:
        high_price = float(daily_data["2. high"])
        if high_price > highest_high:
            highest_high = high_price

    # Return the highest high price
    return {"max": highest_high}
