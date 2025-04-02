import numpy as np
from fastapi import APIRouter
from model_loader import get_model

router = APIRouter()

# Load model
model = get_model()

@router.get("/predict/")
async def predict_price(features: str):
    try:
        # Convert input to numpy array
        data = np.array([float(x) for x in features.split(",")]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(data)
        
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}
