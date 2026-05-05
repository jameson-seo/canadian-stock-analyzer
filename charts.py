import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use('Agg')
plt.style.use('seaborn-v0_8-whitegrid')

os.makedirs("outputs", exist_ok=True)

prices = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

sectors = {
    "Canadian Banks": ["RY.TO", "TD.TO", "BNS.TO"],
    "Energy":         ["SU.TO", "CNQ.TO", "ENB.TO"],
    "Tech":           ["SHOP.TO", "NVDA", "AAPL"],
    "Consumer":       ["MCD", "SBUX", "WMT"],
    "Index":          ["SPY", "XIU.TO"]
}

returns = {}
for ticker in prices.columns:
    start = prices[ticker].dropna().iloc[0]
    end = prices[ticker].dropna().iloc[-1]
    returns[ticker] = round(((end - start) / start) * 100, 2)

# --- Chart 1: Individual stock returns ---
sorted_pairs = sorted(zip(returns.values(), returns.keys()))
values_sorted, tickers_sorted = zip(*sorted_pairs)
colors = ["#2ecc71" if v >= 0 else "#e74c3c" for v in values_sorted]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(tickers_sorted, values_sorted, color=colors, edgecolor="none", height=0.6)
ax.axvline(0, color="#333333", linewidth=0.8)
ax.set_xlabel("1-Year Return (%)", fontsize=12, color="#333333")
ax.set_title("1-Year Stock Returns", fontsize=15, fontweight="bold", color="#222222", pad=15)
ax.tick_params(colors="#444444")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
for bar, val in zip(bars, values_sorted):
    ax.text(val + (1 if val >= 0 else -1), bar.get_y() + bar.get_height()/2,
            f"{val}%", va="center", ha="left" if val >= 0 else "right",
            fontsize=9, color="#333333")
plt.tight_layout()
plt.savefig("outputs/chart1_returns.png", dpi=150, bbox_inches="tight")
print("Saved chart 1")

# --- Chart 2: Sector average returns ---
sector_returns = {}
for sector, tickers in sectors.items():
    valid = [t for t in tickers if t in returns]
    sector_returns[sector] = round(sum(returns[t] for t in valid) / len(valid), 2)

colors2 = ["#3498db", "#e67e22", "#2ecc71", "#e74c3c", "#9b59b6"]
fig, ax = plt.subplots(figsize=(9, 5))
bars2 = ax.bar(sector_returns.keys(), sector_returns.values(), color=colors2, edgecolor="none", width=0.5)
ax.set_ylabel("Average Return (%)", fontsize=12, color="#333333")
ax.set_title("Sector Average Returns (1 Year)", fontsize=15, fontweight="bold", color="#222222", pad=15)
ax.tick_params(colors="#444444")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
for bar, val in zip(bars2, sector_returns.values()):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f"{val}%",
            ha="center", va="bottom", fontsize=10, color="#333333")
plt.tight_layout()
plt.savefig("outputs/chart2_sectors.png", dpi=150, bbox_inches="tight")
print("Saved chart 2")

# --- Chart 3: Cumulative sector performance ---
sector_colors = {
    "Canadian Banks": "#3498db",
    "Energy":         "#e67e22",
    "Tech":           "#2ecc71",
    "Consumer":       "#e74c3c",
    "Index":          "#9b59b6"
}

fig, ax = plt.subplots(figsize=(12, 6))
for sector, tickers in sectors.items():
    valid = [t for t in tickers if t in prices.columns]
    sector_prices = prices[valid].dropna()
    cumulative = (sector_prices / sector_prices.iloc[0]).mean(axis=1)
    ax.plot(cumulative.index, cumulative, label=sector,
            color=sector_colors[sector], linewidth=2)

ax.set_ylabel("Cumulative Return (1 = start)", fontsize=12, color="#333333")
ax.set_title("Sector Performance Over 1 Year", fontsize=15, fontweight="bold", color="#222222", pad=15)
ax.legend(frameon=True, fontsize=10)
ax.tick_params(colors="#444444")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("outputs/chart3_cumulative.png", dpi=150, bbox_inches="tight")
print("Saved chart 3")

print("\nAll charts saved!")