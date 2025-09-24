# Minimal / mock data extractor for multimodal inputs.
# In production, this would orchestrate OCR (pytesseract/pdf2image), parsers for tables (camelot/openpyxl),
# and resume parsers (spaCy / custom rules). For the prototype we keep it deterministic and simple.

from typing import Dict, Any

class DataExtractor:
    def __init__(self):
        pass

    def extract_from_files(self, files) -> Dict[str, Any]:
        # files: list of UploadFile
        # Return synthetic parsed contents
        return {"parsed_texts": []}

    def merge_form_and_attachments(self, form: Dict[str, Any], attachments: Dict[str, Any]) -> Dict[str, Any]:
        merged = form.copy()
        merged.update(attachments)
        return merged

