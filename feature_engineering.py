import ta

def add_technical_indicators(df):
    df['SMA_50'] = df['close'].rolling(window=50).mean()
    df['SMA_200'] = df['close'].rolling(window=200).mean()
    df['RSI'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['MACD'] = ta.trend.MACD(df['close']).macd()
    df['volatility'] = ta.volatility.BollingerBands(df['close']).bollinger_hband() - \
                        ta.volatility.BollingerBands(df['close']).bollinger_lband()
    return df

def detect_market_regime(option_chain):
    # Example logic: if the put/call ratio > 1, bear market; else, bull market
    put_call_ratio = option_chain['put_volume'] / option_chain['call_volume']
    if put_call_ratio > 1:
        return 'bear'
    else:
        return 'bull'
