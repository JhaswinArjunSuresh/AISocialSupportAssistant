from typing import Any, Dict
from .data_validation import Validator
from .eligibility_agent import EligibilityAgent
from .recommendation_agent import RecommendationAgent

class Orchestrator:
    """Simple orchestrator that runs a sequence of agents:
       1. Validate and normalize data
       2. Run eligibility scoring
       3. Produce recommendations for economic enablement
       It follows a simple ReAct-like loop: Observe -> Act -> Reflect (mocked)
    """
    def __init__(self, model=None):
        self.validator = Validator()
        self.elig_agent = EligibilityAgent(model=model)
        self.rec_agent = RecommendationAgent()

    def run(self, extracted: Dict[str, Any]) -> Dict[str, Any]:
        # 1. Validate / normalize
        validated = self.validator.validate(extracted.get("form", {}))
        # 2. Eligibility scoring
        eligibility = self.elig_agent.assess(validated)
        # 3. Recommendations
        recommendations = self.rec_agent.recommend(validated, eligibility)
        # Compose response with simple provenance
        return {
            "validated_data": validated,
            "eligibility": eligibility,
            "recommendations": recommendations,
            "provenance": {
                "agents": ["validator", "eligibility_agent", "recommendation_agent"]
            }
        }

