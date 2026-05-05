# Canadian Stock Sector Analyzer

A Python-based data analysis project that pulls 1 year of real stock market data for 14 TSX and NYSE stocks across 5 sectors, analyzing returns, volatility, and sector performance.

## What I Found

- **Energy was the top performing sector** with an average return of 69.5%, led by Suncor (SU.TO) at +106%
- **Canadian Banks** came in second at 59.5%, significantly outperforming the S&P 500 index (+30%)
- **Shopify** was the most volatile stock but only returned 6.5% — high risk, low reward this year
- **McDonald's** was the only stock with a negative return at -7.3%

## Sectors Analyzed

| Sector | Tickers |
|---|---|
| Canadian Banks | RY.TO, TD.TO, BNS.TO |
| Energy | SU.TO, CNQ.TO, ENB.TO |
| Tech | SHOP.TO, NVDA, AAPL |
| Consumer | MCD, SBUX, WMT |
| Index | SPY, XIU.TO |

## Charts

![Sector Performance Over 1 Year](outputs/chart3_cumulative.png)
![Sector Average Returns](outputs/chart2_sectors.png)

## Tech Stack

- **Python** — core language
- **pandas** — data manipulation and analysis
- **yfinance** — pulling live stock data from Yahoo Finance
- **matplotlib** — data visualization
- **Git** — version control

## How to Run

1. Clone the repo
2. Install dependencies: