import joblib
import numpy as np
model_path = "models\\an_rf_model.joblib"
scaler_path = "models\\an_rf_scaler.joblib"
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def predict_sample(X):
    if X.ndim == 1:
        X = X.reshape(1, -1)

    X = scaler.transform(X)
    pred = model.predict(X)
    prob = model.predict_proba(X)[:, 1]
    importances = model.feature_importances_

    return np.array(pred), np.array(prob), np.array(importances)
