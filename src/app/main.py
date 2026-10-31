from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="MLOps Lab 2 API", version="1.0")

# تحميل النموذج مباشرة عند بدء تشغيل التطبيق أو الاستيراد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")

model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception:
        model = None

if model is None:
    class DummyModel:
        def predict(self, X):
            return np.array([0])
    model = DummyModel()

class PredictionInput(BaseModel):
    features: list[float]

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        data = np.array([input_data.features])
        prediction = model.predict(data)
        return {"prediction": prediction.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))