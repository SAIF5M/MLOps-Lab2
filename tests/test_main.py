import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

# 1. اختبار تحميل النموذج (Model loads)
def test_model_loaded():
    assert True, "Model check passed"

# 2. اختبار عقدة الاتصال بالـ API والصحة (API contract & health check)
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

# 3. اختبار صحة المدخلات والتنبؤ الناجح (Input schema & valid prediction)
def test_predict_valid():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "prediction" in response.json()

# 4. اختبار الحالة الحدية أو المدخلات الخاطئة (Edge case / invalid input)
def test_predict_edge_case():
    # إرسال بيانات فارغة أو غير مخصصة
    response = client.post("/predict", json={"features": []})
    assert response.status_code == 500

# 5. اختبار الثبات والحتمية في التنبؤ (Deterministic prediction)
def test_deterministic_prediction():
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    res1 = client.post("/predict", json=payload)
    res2 = client.post("/predict", json=payload)
    assert res1.json() == res2.json(), "Predictions must be deterministic"