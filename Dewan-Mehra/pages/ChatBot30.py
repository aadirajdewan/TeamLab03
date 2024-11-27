import streamlit as st
import google.generativeai as genai
import requests

st.set_page_config(page_title="AI Stock Analysis with Chatbot", page_icon="📈🤖", layout="wide")

FINNHUB_API_KEY = "ct39hvpr01qkff7151fgct39hvpr01qkff7151g0"
FINNHUB_BASE_URL = "https://finnhub.io/api/v1/quote"
GOOGLE_API_KEY = "AIzaSyBvyH3Ao1EY_9TIujbWW2bbEJgQHezUiyE"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "stock_data" not in st.session_state:
    st.session_state.stock_data = None


def fetch_stock_data_finnhub(symbol):
    try:
        params = {"symbol": symbol, "token": FINNHUB_API_KEY}
        response = requests.get(FINNHUB_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if not data or "c" not in data:
            st.error("Invalid stock symbol or no data available.")
            return None
        return {
            "current_price": data["c"],
            "high": data["h"],
            "low": data["l"],
            "open": data["o"],
            "previous_close": data["pc"],
        }
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching stock data: {e}")
        return None


def generate_stock_report(data, report_type):
    prompts = {
        "News Style": f"Write a news-style report analyzing the stock performance of {data['symbol']}. Current price: ${data['current_price']}, High: ${data['high']}, Low: ${data['low']}.",
        "Investment Advisory": f"Provide an investment advisory for {data['symbol']} stock. Current price: ${data['current_price']}, Previous close: ${data['previous_close']}.",
        "Technical Analysis": f"Perform a technical analysis for {data['symbol']} stock. Current price: ${data['current_price']}, High: ${data['high']}, Low: ${data['low']}, Open: ${data['open']}, Previous close: ${data['previous_close']}.",
    }
    prompt = prompts.get(report_type, "Provide a general analysis of the stock market.")
    try:
        response = model.generate_content(prompt)
        if not response or not hasattr(response, "text") or not response.text:
            return "Unable to generate stock report at this time. Please try again later."
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating stock report: {e}")
        return "An error occurred while generating the stock report. Please try again later."


def stock_chatbot(user_input, stock_data, symbol):
    context = f"""
    You are an AI financial advisor. Analyze and provide insights about {symbol} stock based on this data:
    - Current Price: ${stock_data['current_price']}
    - High: ${stock_data['high']}
    - Low: ${stock_data['low']}
    - Open: ${stock_data['open']}
    - Previous Close: ${stock_data['previous_close']}
    """
    prompt = f"{context}\n\nUser Question: {user_input}\n\nResponse:"
    try:
        response = model.generate_content(prompt)
        if not response or not response.text:
            return "Sorry, I couldn't process your query. Please try again."
        return response.text.strip()
    except Exception as e:
        st.error(f"Error in chatbot response: {e}")
        return "Unable to process your query at this time."


st.title("📈🤖 AI Stock Analysis with Chatbot")

with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, AMZN):", "AAPL")
    with col2:
        report_type = st.selectbox(
            "Select Report Type:", ["News Style", "Investment Advisory", "Technical Analysis"]
        )

if st.button("Get AI Analysis"):
    if not stock_symbol.strip():
        st.error("Please enter a valid stock symbol.")
    else:
        with st.spinner("Fetching stock data and generating analysis..."):
            stock_data = fetch_stock_data_finnhub(stock_symbol.strip())
            if stock_data is not None:
                st.session_state.stock_data = stock_data
                st.write(f"### Stock Analysis for {stock_symbol.upper()}")
                st.metric("Current Price", f"${stock_data['current_price']:.2f}")
                st.metric("High", f"${stock_data['high']:.2f}")
                st.metric("Low", f"${stock_data['low']:.2f}")
                st.metric("Open", f"${stock_data['open']:.2f}")
                st.metric("Previous Close", f"${stock_data['previous_close']:.2f}")
                formatted_data = {"symbol": stock_symbol, **stock_data}
                report = generate_stock_report(formatted_data, report_type)
                st.subheader("🤖 AI-Generated Stock Report")
                st.write(report)
            else:
                st.session_state.stock_data = None
                st.error("Unable to fetch stock data. Please check the stock symbol and try again.")

with st.container():
    st.subheader("💬 Chat about Stock Analysis")
    if st.session_state.stock_data is None:
        st.info("Please fetch stock data first.")
    else:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask about the stock analysis..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                response = stock_chatbot(prompt, st.session_state.stock_data, stock_symbol)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
