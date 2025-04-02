import tensorflow as tf
import os

# Ensure the correct model path
MODEL_PATH = os.path.abspath("models/bilstm_model.h5")

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

def get_model():
    return model
