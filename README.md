# 📞 Customer Churn Prediction App

A Streamlit-based interactive web application that predicts customer churn in a telecom environment using machine learning. Built using the **Telco Customer Churn** dataset, the app enables users to input customer attributes and receive real-time predictions on whether a customer is likely to churn.

---

## 🚀 Features

- **Interactive Interface**  
  User-friendly Streamlit interface to input customer data and get predictions.

- **ML-Powered Predictions**  
  Utilizes a trained machine learning classification model (e.g., XGBoost, Random Forest) to make accurate predictions.

- **Feature Matching**  
  Inputs are aligned with real-world telecom attributes such as tenure, charges, contract type, and services.

- **Instant Feedback**  
  Predicts churn likelihood instantly and visually displays the result on screen.

---

## 🏗️ Project Structure
Customer_Churn_Prediction/
- **├── app.py # Streamlit app script**
- **├── churn_model.pkl # Serialized trained ML model (Joblib format)**
- **├── feature_columns.csv # Expected input columns for model prediction**
- **├── Customer Churn Prediction.ipynb # Jupyter notebook for EDA and model training**
- **└── README.md # Project documentation**

---


---

## 🧠 How It Works

- **Input Encoding**  
  User inputs are mapped to encoded numerical features using the same preprocessing logic used during training.

- **Prediction Logic**  
  The trained model evaluates the encoded input and returns a binary classification:
  - **1** → Customer will churn  
  - **0** → Customer will not churn

- **Training Workflow**  
  The machine learning workflow includes:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Categorical Encoding
  - Model Training and Evaluation  
  The full pipeline is documented in the notebook: `Customer Churn Prediction.ipynb`

---

## 📊 Dataset Information

- **Source:**  
  [Telco Customer Churn Dataset – Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)

- **Key Features:**
  - **Demographics:**
    - Gender  
    - SeniorCitizen  
    - Partner  
    - Dependents
  - **Service Details:**
    - InternetService  
    - PhoneService  
    - Contract type  
  - **Usage Metrics:**
    - Tenure  
    - MonthlyCharges  
    - TotalCharges
  - **Target:**
    - Churn (Yes/No)

---

## Example

![Screenshot 2025-07-25 013520](https://github.com/user-attachments/assets/ea663689-f2d2-4a90-943f-9cd25ba3e906)


