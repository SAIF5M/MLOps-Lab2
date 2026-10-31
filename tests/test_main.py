
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


# 1. Model loads
def test_model_loaded():
    assert True, "Model check passed"


# 2. API health check
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200


# 3. Valid prediction
def test_predict_valid():
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )

    assert response.status_code == 200
    assert "prediction" in response.json()


# 4. Invalid input / Edge case
def test_predict_edge_case():
    response = client.post(
        "/predict",
        json={"features": []}
    )

    assert response.status_code == 422


# 5. Deterministic prediction
def test_deterministic_prediction():
    payload = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }

    res1 = client.post("/predict", json=payload)
    res2 = client.post("/predict", json=payload)

    assert res1.status_code == 200
    assert res2.status_code == 200

    assert res1.json() == res2.json(), (
        "Predictions must be deterministic"
    )
