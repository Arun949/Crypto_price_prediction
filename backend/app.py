from fastapi import FastAPI
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Explicitly define the loss function
custom_objects = {"mse": tf.keras.losses.MeanSquaredError()}

app = FastAPI()
model = tf.keras.models.load_model("models/lstm_model.h5", custom_objects=custom_objects)
scaler = MinMaxScaler()

@app.get("/")
def home():
    return {"message": "Crypto Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    df_scaled = scaler.transform(df)
    df_scaled = np.expand_dims(df_scaled, axis=0)
    prediction = model.predict(df_scaled)
    return {"predicted_price": prediction.tolist()}