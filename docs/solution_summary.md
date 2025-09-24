# Solution Summary — AI Social Support Application Prototype

## 1. High-level architecture
- **Front-end**: Streamlit demo for interactive applications.
- **API / Orchestration**: FastAPI service exposing `/api/assess` endpoint and coordinating the orchestrator.
- **Agents**:
  - DataExtractor: handles multimodal ingestion (OCR & parsers) — mocked here.
  - Validator: field validation, normalization, conflict detection.
  - EligibilityAgent: local ML-based scoring (Scikit-learn) with a heuristic fallback.
  - RecommendationAgent: produces support and enablement suggestions.
- **Model artifact**: `app/models/eligibility_model.pkl` trained on synthetic data.
- **Observability and Persistence**: For prototype, simple provenance returned. In production: integrate Langfuse for observability, Postgres for relational storage, MongoDB for document storage, Qdrant for vectors, and Neo4j for relationship queries.

## 2. Tool choices and justification
- **Python**: ecosystem for ML, web, and data processing.
- **FastAPI**: modern ASGI framework, fast to develop and production-ready.
- **Streamlit**: rapid UI prototyping for demos and interactive exploration.
- **Scikit-learn**: robust classical ML models for tabular eligibility scoring.
- **Local LLM hosting**: recommend Ollama / OpenWebUI for local LLMs (not included here).
- **Agentic orchestration**: prototype uses a simple orchestrator. For scale, use LangGraph / Crew.AI / Agno for multi-agent flows.
- **Databases**: Postgres (ACID), MongoDB (document), Qdrant (vectors), Neo4j (relationships).

## 3. Data flow
1. Applicant fills form + uploads attachments.
2. DataExtractor parses attachments (OCR, table parsers).
3. Validator normalizes data and detects conflicts.
4. EligibilityAgent scores with local ML.
5. RecommendationAgent prepares support and enablement responses.
6. Response is returned to UI with provenance.

## 4. Security & Privacy
- All PII should be encrypted at rest and in transit. Use TLS for APIs, field-level encryption for identity docs.
- Access controls: RBAC on APIs, audit logging, and data retention policies.
- For OCR and sensitive document parsing, run offline and short-lived processing.

## 5. Future improvements
- Replace mocked extractor with real OCR (Tesseract + pdf2image) and robust resume/bank-statement parsers.
- Use a vector DB (Qdrant) for semantic search across applicant histories and LLM context windows.
- Integrate local LLM for Chat/Agent flows (Ollama/OpenWebUI) and Langfuse for observability.
- Add workflow engine for human-in-the-loop reviews and appeals.
- Harden model: fairness audits, explainability (SHAP), and monitoring for data drift.

