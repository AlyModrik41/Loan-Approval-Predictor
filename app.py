import streamlit as st
import pandas as pd
import joblib
import os

# ========================
# Load the trained model
# ========================
MODEL_PATHS = {
    "Logistic Regression": "logistic_regression_smote.pkl",
    "Random Forest": "random_forest_smote.pkl",
    "XGBoost": "gradient_boosting_smote.pkl",
    "KNN":"knn_smote.pkl",
    "SVM":"svm_smote.pkl",
    "Voting Classifier":"VotingClassifierSoft.pkl"
}
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💳",
    layout="centered",
)

st.title("🏦 Loan Approval Prediction App")
st.write("Choose a model and fill in applicant details below to get predictions.")

# =======================
# Model Selection
# =======================
model_choice = st.selectbox("Select Model", list(MODEL_PATHS.keys()))

# Load selected model
model_file = MODEL_PATHS[model_choice]
if not os.path.exists(model_file):
    st.error(f"⚠️ Model file `{model_file}` not found. Please upload it.")
    st.stop()

model = joblib.load(model_file)

# ========================
# Page Config
# ========================


# ========================
# Custom CSS (Bank Portal Look)
# ========================
st.markdown("""
    <style>
        body {
            background-color: #1c2e4a;
        }
        .main {
            background-color: #000033;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #0047AB;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #00357A;
        }
    </style>
""", unsafe_allow_html=True)

# ========================
# Header
# ========================
st.title("💳 Loan Approval Predictor")
st.markdown(
    "<p style='color: #555; font-size:18px;'>Enter applicant details to check loan eligibility.</p>",
    unsafe_allow_html=True
)

# ========================
# Input Form
# ========================
st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    ApplicantIncome = st.number_input("Applicant Income", min_value=0, step=100)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, step=100)
    LoanAmount = st.number_input("Loan Amount", min_value=0, step=10)
    Loan_Amount_Term = st.selectbox("Loan Amount Term (days)", [360, 180, 120, 84, 60, 36])
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])

with col2:
    Gender_Male = st.selectbox("Gender", ["Female", "Male"])
    Married_Yes = st.selectbox("Married", ["No", "Yes"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education_Not_Graduate = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed_Yes = st.selectbox("Self Employed", ["No", "Yes"])
    Property_Area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# ========================
# Convert Inputs to Model Features
# ========================
if st.button("🔍 Predict Loan Status"):
    # Match training columns
    input_dict = {
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Gender_Male': 1 if Gender_Male == "Male" else 0,
        'Married_Yes': 1 if Married_Yes == "Yes" else 0,
        'Dependents_1': 1 if Dependents == "1" else 0,
        'Dependents_2': 1 if Dependents == "2" else 0,
        'Dependents_3+': 1 if Dependents == "3+" else 0,
        'Education_Not Graduate': 1 if Education_Not_Graduate == "Not Graduate" else 0,
        'Self_Employed_Yes': 1 if Self_Employed_Yes == "Yes" else 0,
        'Property_Area_Semiurban': 1 if Property_Area == "Semiurban" else 0,
        'Property_Area_Urban': 1 if Property_Area == "Urban" else 0,
    }

    input_df = pd.DataFrame([input_dict])

    # Predict
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1] * 100

    # ========================
    # Result Card
    # ========================
    if prediction == 1:
        st.markdown(
            f"""
            <div style="padding:20px; border-radius:12px; background-color:#E9F7EF; text-align:center; border: 1px solid #28a745;">
                <h2 style="color:#1E8449;">✅ Loan Approved</h2>
                <p style="color:#1E8449;font-size:18px;">Approval Confidence: <b>{proba:.2f}%</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <style>
            .main{
            background-color:#1E8449
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="padding:20px; border-radius:12px; background-color:#FDEDEC; text-align:center; border: 1px solid #c0392b;">
                <h2 style="color:#922B21;">❌ Loan Rejected</h2>
                <p style="color:#922B21;font-size:18px;">Approval Chance: <b>{proba:.2f}%</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <style>
            .main{
            background-color:#922B21
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# ========================
# Sidebar
# ========================
st.sidebar.title("ℹ️ About This App")
st.sidebar.markdown("""
This Loan Approval Predictor was built using:

- Random Forest Classifier  
- SMOTE for balancing classes  
- Cross-validation (~95% accuracy)  

**How it works:**  
Fill in the applicant details → model predicts if loan will be approved.  

🔗 [GitHub Repo](https://github.com/AlyModrik41/Loan-Approval-Predictor)
""")
