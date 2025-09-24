from typing import Dict, Any, List

class RecommendationAgent:
    def __init__(self):
        pass

    def recommend(self, validated: Dict[str, Any], eligibility: Dict[str, Any]) -> Dict[str, Any]:
        recs = {"support": [], "enablement": []}
        if eligibility.get('approved'):
            recs['support'].append({
                "type": "financial_support",
                "amount_estimate": self.estimate_amount(validated)
            })
        else:
            recs['support'].append({"type":"soft_decline","reason":"Eligibility threshold not met, propose enablement"})
        # Enablement suggestions
        skills = validated.get('skills', [])
        if not skills:
            recs['enablement'].append({"program": "basic_digital_literacy", "description":"Beginner digital skills program"})
        else:
            recs['enablement'].append({"program":"job_matching", "description":"Connect to job matching platform"})
        return recs

    def estimate_amount(self, validated):
        income = validated.get('income',0.0)
        base = max(200, 2000 - income)
        return round(base, 2)

