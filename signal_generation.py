def generate_alpha_signals(df, market_regime):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0
    
    # Example signals: simple moving average crossover strategy
    signals['signal'][50:] = np.where(df['SMA_50'][50:] > df['SMA_200'][50:], 1, 0)
    signals['signal'] = np.where(market_regime == 'bear', 0, signals['signal'])
    
    return signals
