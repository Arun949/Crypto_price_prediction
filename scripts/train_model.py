import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/BTC-USD_1d_processed.csv", index_col=0, parse_dates=True)

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[['Close', 'RSI', 'MACD', 'Bollinger_Upper', 'Bollinger_Lower']])

X, y = [], []
window_size = 60

for i in range(len(df_scaled) - window_size):
    X.append(df_scaled[i:i+window_size])
    y.append(df_scaled[i+window_size, 0])  

X, y = np.array(X), np.array(y)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(window_size, X.shape[2])),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=32)

model.save("models/lstm_model.h5")