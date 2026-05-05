import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import os
os.makedirs("outputs", exist_ok=True)

# Load data
prices = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

sectors = {
    "Canadian Banks": ["RY.TO", "TD.TO", "BNS.TO"],
    "Energy":         ["SU.TO", "CNQ.TO", "ENB.TO"],
    "Tech":           ["SHOP.TO", "NVDA", "AAPL"],
    "Consumer":       ["MCD", "SBUX", "WMT"],
    "Index":          ["SPY", "XIU.TO"]
}

# Calculate returns
returns = {}
for ticker in prices.columns:
    start = prices[ticker].dropna().iloc[0]
    end = prices[ticker].dropna().iloc[-1]
    returns[ticker] = round(((end - start) / start) * 100, 2)

# --- Chart 1: Individual stock returns bar chart ---
fig, ax = plt.subplots(figsize=(12, 6))
tickers = list(returns.keys())
values = list(returns.values())
colors = ["green" if v >= 0 else "red" for v in values]
sorted_pairs = sorted(zip(values, tickers))
values_sorted, tickers_sorted = zip(*sorted_pairs)
colors_sorted = ["green" if v >= 0 else "red" for v in values_sorted]
ax.barh(tickers_sorted, values_sorted, color=colors_sorted)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel("1-Year Return (%)")
ax.set_title("1-Year Stock Returns")
plt.tight_layout()
plt.savefig("outputs/chart1_returns.png", dpi=150)
print("Saved chart 1")

# --- Chart 2: Sector average returns ---
sector_returns = {}
for sector, tickers in sectors.items():
    valid = [t for t in tickers if t in returns]
    sector_returns[sector] = round(sum(returns[t] for t in valid) / len(valid), 2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(sector_returns.keys(), sector_returns.values(), color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])
ax.set_ylabel("Average Return (%)")
ax.set_title("Sector Average Returns (1 Year)")
plt.tight_layout()
plt.savefig("outputs/chart2_sectors.png", dpi=150)
print("Saved chart 2")

# --- Chart 3: Cumulative returns over time per sector ---
fig, ax = plt.subplots(figsize=(12, 6))
for sector, tickers in sectors.items():
    valid = [t for t in tickers if t in prices.columns]
    sector_prices = prices[valid].dropna()
    cumulative = (sector_prices / sector_prices.iloc[0]).mean(axis=1)
    ax.plot(cumulative.index, cumulative, label=sector)
ax.set_ylabel("Cumulative Return (1 = start)")
ax.set_title("Sector Performance Over 1 Year")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_cumulative.png", dpi=150)
print("Saved chart 3")

print("\nAll charts saved to outputs/ folder!")