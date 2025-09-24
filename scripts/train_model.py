"""Train a simple classifier on synthetic data and save the model artifact.
Features: income, age, family_size
Label: binary approve/reject
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

def generate_synthetic(n=2000, random_state=42):
    rng = np.random.RandomState(random_state)
    income = rng.normal(loc=1500, scale=800, size=n).clip(0, 10000)
    age = rng.randint(18, 70, size=n)
    family = rng.randint(1, 8, size=n)
    # Label: approve if income low and family large
    score = (2000 - income)/2000 + (family-1)*0.12 + (50 - age)/200.0
    prob = 1/(1+np.exp(-score*3))
    label = (prob > 0.5).astype(int)
    df = pd.DataFrame({"income":income, "age":age, "family_size":family, "label":label})
    return df

def train_and_save(path="app/models/eligibility_model.pkl"):
    df = generate_synthetic()
    X = df[["income","age","family_size"]]
    y = df["label"]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, path)
    print("Saved model to", path)

if __name__ == "__main__":
    train_and_save()
