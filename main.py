import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Canion Financial Services Stock Price App

Shown are the stock "closing price" and volume of Microsoft!

""")

#define the ticker symbol
tickerSymbol = 'MSFT'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-1-1', end='2022-1-25')
# Open High Low Close Volume Dividends Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
