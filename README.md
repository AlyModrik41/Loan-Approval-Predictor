# 💳 Loan Approval Predictor  

This project predicts whether a **loan application will be approved or rejected** based on applicant details such as income, credit history, dependents, and property area.  

It uses **Machine Learning (Random Forest Classifier)** with **SMOTE** for handling class imbalance and achieves strong predictive performance.  

---

## 🚀 Features
- Clean **bank portal style Streamlit App** for deployment  
- Input form for applicant data  
- Shows **loan approval prediction** with confidence score  
- Interactive UI with approval probability visualization  
- Model evaluation with **ROC-AUC, Average Precision, Confusion Matrix, Feature Importance**  

---

## 📊 Dataset
- **Source:** Kaggle Loan Prediction dataset  
- **Rows:** ~600 records  
- **Columns:** 14 processed features after encoding  

---

## 🔧 Tech Stack
- **Python** (scikit-learn, pandas, numpy, joblib)  
- **Streamlit** (for app deployment)  
- **Matplotlib & Seaborn** (for visualization)  
- **SMOTE** (for balancing classes)  

---

## 🔍 Exploratory Data Analysis (EDA)

### Correlation Heatmap
![Correlation Heatmap](images/heatmap.png)  

---

## 🏆 Model Performance

### ROC-AUC Curve
![ROC AUC](images/roc_auc.png)  

### Average Precision (AP) Curve
![AP Curve](images/ap_curve.png)  

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)  

### Feature Importance
![Feature Importance](images/feature_importance.png)  

---

## 🎯 Best Model
- **Model Used:** Random Forest Classifier  
- **Handling Imbalance:** SMOTE applied  
- **Best Metrics:**  
  - Accuracy: **~95%**  
  - ROC-AUC: **0.97**  
  - AP Score: **0.94**  
  - Precision/Recall balanced  

---

## 🖥️ Streamlit App

![App Screenshot](images/app_screenshot.png)  

Run the app locally:
```bash
streamlit run app.py
