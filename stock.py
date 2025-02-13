import yfinance as yf
import streamlit as st

def main():
    st.write("""
    # Simple Stock Price App

    Shown are the stock **closing price** and ***volume*** of Amazon!
    """)

    # Define the ticker symbol
    tickerSymbol = 'AMZN'
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.write("## Closing Price")
    st.line_chart(tickerDf.Close)

    st.write("## Volume Price")
    st.line_chart(tickerDf.Volume)

# Ensure the script can be run independently or as a module
if __name__ == "__main__":
    main()
