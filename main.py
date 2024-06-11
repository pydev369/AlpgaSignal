def main(symbol):
    ohlcv_data = get_ohlcv_data(symbol)
    ohlcv_data = add_technical_indicators(ohlcv_data)
    
    option_chain = get_option_chain_data(symbol)
    market_regime = detect_market_regime(option_chain)
    
    signals = generate_alpha_signals(ohlcv_data, market_regime)
    cumulative_returns = backtest_signals(ohlcv_data, signals)
    
    plot_performance(cumulative_returns)
    print(cumulative_returns.tail())

if __name__ == "__main__":
    main('AAPL')  # Example symbol
