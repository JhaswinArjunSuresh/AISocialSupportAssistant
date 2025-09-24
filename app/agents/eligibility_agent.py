from typing import Dict, Any
import numpy as np

class EligibilityAgent:
    def __init__(self, model=None):
        self.model = model

    def assess(self, validated: Dict[str, Any]) -> Dict[str, Any]:
        # If a trained model is available, use it; otherwise use rule-based heuristics
        if self.model:
            # Build feature vector in same order as training script
            X = [[validated.get('income',0.0), validated.get('age',0), validated.get('family_size',1)]]
            prob = self.model.predict_proba(X)[0][1]
            pred = bool(self.model.predict(X)[0])
            return {"approved": bool(pred), "score": float(prob), "method": "sklearn_model"}
        else:
            # Heuristic: low income and larger family -> approve
            income = validated.get('income', 0.0)
            family = validated.get('family_size', 1)
            score = max(0.0, min(1.0, (2000 - income) / 2000 + (family-1)*0.1))
            approved = (score > 0.5)
            return {"approved": approved, "score": float(score), "method": "heuristic"}

