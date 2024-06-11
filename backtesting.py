def backtest_signals(df, signals):
    df['signal'] = signals['signal']
    df['daily_return'] = df['close'].pct_change()
    df['strategy_return'] = df['daily_return'] * df['signal'].shift(1)
    cumulative_returns = (1 + df[['daily_return', 'strategy_return']]).cumprod()
    
    return cumulative_returns

def plot_performance(cumulative_returns):
    import matplotlib.pyplot as plt
    cumulative_returns.plot(figsize=(10, 5))
    plt.title('Strategy Performance')
    plt.show()
