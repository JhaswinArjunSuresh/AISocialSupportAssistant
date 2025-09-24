import streamlit as st
import requests
import json

st.set_page_config(page_title="Social Support AI Prototype", layout='wide')

st.title("AI Social Support Application — Prototype Demo")

with st.form('app_form'):
    name = st.text_input('Full name', 'Ahmed Ali')
    age = st.number_input('Age', 18, 100, 34)
    income = st.number_input('Monthly income (AED)', 0.0, 100000.0, 800.0, step=50.0)
    family_size = st.number_input('Family size', 1, 20, 4)
    address = st.text_area('Address', 'Al Barsha, Dubai')
    submit = st.form_submit_button('Submit application')

if submit:
    payload = {
        "name": name,
        "age": age,
        "income": income,
        "family_size": family_size,
        "address": address
    }
    st.info("Sending application to local API /api/assess (expects backend running on http://localhost:8000)")
    try:
        resp = requests.post("http://localhost:8000/api/assess", data={'applicant_json': json.dumps(payload)})
        if resp.status_code == 200:
            st.success("Received assessment")
            st.json(resp.json())
        else:
            st.error(f"API error: {resp.status_code} - {resp.text}")
    except Exception as e:
        st.error("Failed to contact backend API: " + str(e))

