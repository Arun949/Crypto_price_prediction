import pandas as pd
import ta

def add_technical_indicators(df):
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")  
    df.dropna(inplace=True)  

    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["MACD"] = ta.trend.MACD(df["Close"]).macd()
    df["Bollinger_Upper"] = ta.volatility.BollingerBands(df["Close"]).bollinger_hband()
    df["Bollinger_Lower"] = ta.volatility.BollingerBands(df["Close"]).bollinger_lband()
    
    df.dropna(inplace=True)  
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/BTC-USD_1d.csv", index_col=0, parse_dates=True)

    df.columns = ["Close", "High", "Low", "Open", "Volume"]
    df = df.apply(pd.to_numeric, errors="coerce")

    df = add_technical_indicators(df)
    
    df.to_csv("data/BTC-USD_1d_processed.csv")
    print(df.head())