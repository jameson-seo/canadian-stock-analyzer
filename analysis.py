import pandas as pd

# Load the saved data
prices = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

# Define sectors
sectors = {
    "Canadian Banks": ["RY.TO", "TD.TO", "BNS.TO"],
    "Energy":         ["SU.TO", "CNQ.TO", "ENB.TO"],
    "Tech":           ["SHOP.TO", "NVDA", "AAPL"],
    "Consumer":       ["MCD", "SBUX", "WMT"],
    "Index":          ["SPY", "XIU.TO"]
}

# Calculate % return for each stock over the year
returns = {}
for ticker in prices.columns:
    start = prices[ticker].dropna().iloc[0]
    end = prices[ticker].dropna().iloc[-1]
    returns[ticker] = round(((end - start) / start) * 100, 2)

returns_df = pd.Series(returns).sort_values(ascending=False)
print("=== 1-Year Returns (%) ===")
print(returns_df)

# Calculate average return per sector
print("\n=== Sector Average Returns (%) ===")
for sector, tickers in sectors.items():
    valid = [t for t in tickers if t in returns]
    avg = round(sum(returns[t] for t in valid) / len(valid), 2)
    print(f"{sector}: {avg}%")

# Calculate daily returns and volatility
daily_returns = prices.pct_change().dropna()
volatility = daily_returns.std() * 100
print("\n=== Volatility (daily std %) ===")
print(volatility.round(2).sort_values(ascending=False))