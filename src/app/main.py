from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="MLOps Lab 2 API", version="1.0")

# مسار ملف النموذج داخل مجلد التطبيق
MODEL_PATH = "src/app/model.joblib"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)

# تعريف هيكل المدخلات باستخدام Pydantic
class PredictionInput(BaseModel):
    features: list[float]

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict")
def predict(input_data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded.")
    try:
        data = np.array([input_data.features])
        prediction = model.predict(data)
        return {"prediction": prediction.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))