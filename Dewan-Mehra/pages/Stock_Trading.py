import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime

st.title("Stock Tracker 📈")
st.write("Analyze real-time stock prices and trends with dynamic visuals and user interactions.")

stock_symbol = st.text_input("Enter the stock symbol (e.g., AAPL, TSLA, AMZN):", "AAPL")
num_days = st.slider("Select the number of days to analyze:", 1, 30, 7)

api_key = "LN0XPL1F5Z4EJWH7"
base_url = "https://www.alphavantage.co/query"

if stock_symbol:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        st.error("Unable to fetch stock data. Please check the stock symbol and try again.")
    else:
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())[:num_days]
        prices = [float(time_series[date]["4. close"]) for date in dates]

        current_price = prices[0]
        st.metric(label=f"Current Price of {stock_symbol.upper()}:", value=f"${current_price:.2f}") #NEW

        st.write("### Stock Price Trend")
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]
        plt.figure(figsize=(10, 5))
        plt.plot(dates, prices, marker='o')
        plt.title(f"{stock_symbol.upper()} Stock Price Trend (Last {num_days} Days)")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid()
        plt.tight_layout()
        st.pyplot(plt) #NEW

        st.write("### Analyze Price Changes")
        date_index = st.selectbox("Select a date to view price details:", list(range(len(dates)))) #NEW
        selected_date = dates[date_index]
        selected_price = prices[date_index]
        st.write(f"**Date**: {selected_date.strftime('%Y-%m-%d')}")
        st.write(f"**Price**: ${selected_price:.2f}")

        if len(prices) > 1:
            percentage_change = ((prices[0] - prices[-1]) / prices[-1]) * 100
            st.write("### Percentage Change Analysis")
            st.write(f"The stock price has changed by **{percentage_change:.2f}%** over the selected period.")
