import yfinance as yf
import pandas as pd

# Define stocks by sector
stocks = {
    "Canadian Banks": ["RY.TO", "TD.TO", "BNS.TO"],
    "Energy":         ["SU.TO", "CNQ.TO", "ENB.TO"],
    "Tech":           ["SHOP.TO", "NVDA", "AAPL"],
    "Consumer":       ["MCD", "SBUX", "WMT"],
    "Index":          ["SPY", "XIU.TO"]
}

# Download 1 year of data for all stocks
all_data = {}

for sector, tickers in stocks.items():
    for ticker in tickers:
        print(f"Downloading {ticker}...")
        df = yf.download(ticker, period="1y", auto_adjust=True, progress=False)
        if not df.empty:
            all_data[ticker] = df["Close"].squeeze()

# Combine into one dataframe and save
prices = pd.concat(all_data, axis=1)
prices.columns = all_data.keys()
prices.to_csv("prices.csv")

print("\nDone! Here's a preview:")
print(prices.tail())