import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# -------------------------------------
# 🔹 Load trained model and column structure
model = load('churn_model.pkl')
feature_df = pd.read_csv('feature_columns.csv')
expected_columns = feature_df.columns.tolist()

# -------------------------------------
# 🔹 Streamlit UI
st.title("📞 Customer Churn Prediction App")
st.subheader("Enter customer details to check if they'll churn")

# -------------------------------------
# 🔹 Collect user input
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 1)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

# -------------------------------------
# 🔹 Encode inputs to match training
input_dict = {
    'gender': 1 if gender == 'Male' else 0,
    'SeniorCitizen': 1 if senior == 'Yes' else 0,
    'Partner': 1 if partner == 'Yes' else 0,
    'Dependents': 1 if dependents == 'Yes' else 0,
    'tenure': tenure,
    'PhoneService': 1 if phone_service == 'Yes' else 0,
    'InternetService_DSL': 1 if internet_service == 'DSL' else 0,
    'InternetService_Fiber optic': 1 if internet_service == 'Fiber optic' else 0,
    'Contract_One year': 1 if contract == 'One year' else 0,
    'Contract_Two year': 1 if contract == 'Two year' else 0,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}

# -------------------------------------
# 🔹 Convert to DataFrame and reindex
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=expected_columns, fill_value=0)

# -------------------------------------
# 🔹 Predict churn
if st.button("Predict Churn"):
    result = model.predict(input_df)[0]
    if result == 1:
        st.error("⚠️ This customer is likely to churn!")
    else:
        st.success("✅ This customer is likely to stay.")
