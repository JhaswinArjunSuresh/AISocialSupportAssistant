from typing import Dict, Any
import re

class Validator:
    def __init__(self):
        pass

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Basic validation rules and normalization
        out = data.copy()
        # Normalize keys
        out['name'] = out.get('name', out.get('full_name', 'Unknown'))
        out['age'] = int(out.get('age', 0))
        # Normalize income from various fields
        income = out.get('income') or out.get('monthly_income') or out.get('annual_income') or 0
        try:
            income = float(income)
        except:
            income = 0.0
        out['income'] = income
        # Simple address consistency check (mock)
        addr_form = out.get('address', '')
        addr_credit = out.get('credit_report_address', '')
        out['address_conflict'] = (addr_form != addr_credit and addr_credit != '')
        # Basic family size
        family = out.get('family_size', out.get('household_members', 1))
        out['family_size'] = int(family)
        # Ensure employment history presence
        out['employment_history'] = out.get('employment_history', [])
        return out

