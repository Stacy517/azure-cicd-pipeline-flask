import pytest
from app import app  # 从主模块导入Flask应用
import joblib
import numpy as np

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sklearn Prediction Home" in response.data

def test_predict_endpoint(client):
    test_payload = {
        "CRIM": [0.00632],
        "ZN": [18.0],
        "INDUS": [2.31],
        "CHAS": [0],
        "NOX": [0.538],
        "RM": [6.575],
        "AGE": [65.2],
        "DIS": [4.09],
        "RAD": [1],
        "TAX": [296],
        "PTRATIO": [15.3],
        "B": [396.9],
        "LSTAT": [4.98]
    }

    # send request
    response = client.post('/predict', json=test_payload)
    print('----------lichao--------', response.get_json())
    
    #assert response
    assert response.status_code == 200
    json_data = response.get_json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], list)
    
    try:
        predictions = [float(x) for x in json_data["prediction"]]
    except ValueError:
        pytest.fail("prediction contain float")

def test_missing_model_handling(client):
    # simulate load model failed
    import os
    original_name = "./Housing_price_model/LinearRegression.joblib"
    temp_name = "./Housing_price_model/LinearRegression.joblib.tmp"
    
    if os.path.exists(original_name):
        os.rename(original_name, temp_name)
        try:
            response = client.post('/predict', json={})
            assert response.status_code == 500
            assert "error" in response.get_json()
        finally:
            os.rename(temp_name, original_name)