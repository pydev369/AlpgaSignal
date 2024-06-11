import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import numpy as np

ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'
OPTION_CHAIN_API_URL = 'https://api.example.com/option_chain'

def get_ohlcv_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    data = data.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    })
    return data

def get_option_chain_data(symbol):
    response = requests.get(f"{OPTION_CHAIN_API_URL}?symbol={symbol}")
    option_chain = response.json()
    return option_chain
