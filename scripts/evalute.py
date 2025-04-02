import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# Load the test dataset
DATA_PATH = os.path.abspath("data/BTC-USD_1d_processed.csv")
df = pd.read_csv(DATA_PATH)

# Select features & target variable
feature_columns = ["Open", "High", "Low", "Volume"]
target_column = "Close"

X_test = df[feature_columns].values
y_test = df[target_column].values

# Load the trained model
MODEL_PATH = os.path.abspath("models/bilstm_model.h5")

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()

# Make predictions
y_pred = model.predict(X_test)

# Convert to 1D array
y_pred = y_pred.flatten()

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Print evaluation results
print("\n🔹 Model Evaluation Metrics 🔹")
print(f"📌 Mean Absolute Error (MAE): {mae:.4f}")
print(f"📌 Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"📌 R² Score: {r2:.4f}")

# Save evaluation results to a file
with open("evaluation_results.txt", "w") as f:
    f.write(f"Mean Absolute Error (MAE): {mae:.4f}\n")
    f.write(f"Root Mean Squared Error (RMSE): {rmse:.4f}\n")
    f.write(f"R² Score: {r2:.4f}\n")

print("\n✅ Evaluation results saved to 'evaluation_results.txt'")
