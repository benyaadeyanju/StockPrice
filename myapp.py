from matplotlib import ticker
import streamlit as st
import pandas as pd
import yfinance as yf
from matplotlib import ticker

# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet


st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!



| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

""")
st.markdown('---')
#define the ticker symbol
tickerSymbol = 'AAPL'
#tickerSymbol ='GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='id',start='2021-5-31', end='2022-5-31')
# Open High  Low Close Volume Dividends Stocks Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


