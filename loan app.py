import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('loan_rf_model.pkl')

# Set page config
st.set_page_config(page_title="Loan Eligibility Predictor", layout="centered")

# Title and description
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Predict whether a loan will be approved based on applicant details.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=0)
loan_term = st.number_input("Loan Amount Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", ["Has Credit History", "No Credit History"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding user input same as training
def preprocess_input():
    return [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        1.0 if credit_history == "Has Credit History" else 0.0,
        {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]
    ]

# Predict button
if st.button("Predict Loan Approval"):
    input_data = np.array(preprocess_input()).reshape(1, -1)
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
