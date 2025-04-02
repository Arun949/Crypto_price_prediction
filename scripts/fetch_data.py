import yfinance as yf
import pandas as pd

def fetch_crypto_data(symbol="BTC-USD", interval="1d", period="1y"):
    data = yf.download(symbol, period=period, interval=interval)

    # Flatten multi-index column headers
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(1)

    data.to_csv(f"data/{symbol}_{interval}.csv")
    return data

if __name__ == "__main__":
    df = fetch_crypto_data()
    print(df.head())