# AI Social Support Application - Prototype

This repository contains a local prototype implementation of an AI workflow automation for a government social security department.
It demonstrates ingestion of multimodal data, local ML model serving, an orchestrator (agent-like) workflow, a demo Streamlit front-end, and a FastAPI backend.

## Contents
- `app/backend/` - FastAPI service for model inference, data validation and simple observability.
- `app/agents/` - Simple agent orchestrator and modular agents (data_extraction, validation, eligibility).
- `app/models/` - Model training & saved model artifact (synthetic).
- `streamlit_app.py` - Interactive demo UI (Streamlit).
- `scripts/train_model.py` - Script to generate synthetic data and train a simple classifier.
- `docs/solution_summary.md` - Solution summary, architecture, and design decisions.
- `requirements.txt` - Python dependencies.

## How to run (local, development)
1. Create a Python 3.10+ virtualenv
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Train the model (creates `app/models/eligibility_model.pkl`):
```bash
python scripts/train_model.py
```
3. Start backend:
```bash
uvicorn app.backend.main:app --reload --port 8000
```
4. Start Streamlit UI:
```bash
streamlit run streamlit_app.py
```

## Notes
- This is a prototype. For production, integrate secure secrets management, database connections (Postgres, MongoDB, Qdrant), containerization, and local LLM hosting (Ollama/OpenWebUI).
- See `docs/solution_summary.md` for architecture diagrams and justification.

