# 💳 Loan Approval Predictor  

This project predicts whether a **loan application will be approved or rejected** based on applicant details such as income, credit history, dependents, and property area.  

It uses **Machine Learning (Random Forest Classifier)** with **SMOTE** for handling class imbalance and achieves strong predictive performance.  

---
## 🚀 Live Demo  
Try the Loan Approval Predictor online here:  

👉  https://forest-cover-type-ktgzla6jdpjfezzh8kuww8.streamlit.app/

No installation needed — just open the link and test predictions instantly. 🎉  

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
- **Rows:** ~381 records  
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
<img width="1268" height="754" alt="download" src="https://github.com/user-attachments/assets/209ab908-dd59-4892-97c0-8ddb3b82da11" />


---

## 🏆 Model Performance

### ROC-AUC Curve
<img width="536" height="468" alt="download" src="https://github.com/user-attachments/assets/83fbb07e-a54d-428b-9fba-eccc2e6385c6" />

### Average Precision (AP) Curve
<img width="691" height="545" alt="download" src="https://github.com/user-attachments/assets/0c41f89f-65d1-4755-bd70-05034891e4ce" />

### Confusion Matrix
<img width="709" height="625" alt="download" src="https://github.com/user-attachments/assets/0485a212-2680-4e2f-8dc8-3d8a9f937a8b" />

### Feature Importance
<img width="985" height="1219" alt="download" src="https://github.com/user-attachments/assets/75973d31-9294-4b2e-8c57-de121662ebd7" />

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

<img width="1656" height="872" alt="loan approval predictor screenshot" src="https://github.com/user-attachments/assets/a38cef02-91e9-4e39-a42e-626341f88974" />


## 📂 Project Structure

Loan-Approval-Predictor/                                                                                                                                                                                                                                    
│── app.py                        # your Streamlit app                                                                                                                                                                                                                    
│── loan_model.pkl                # saved trained model                                                                                                                                                                                                                
│── Loan Approval Predictor.ipynb # notebook (optional)                                                                                                                                                                                                                    
│── requirements.txt              # dependencies                                                                                                                                                                                                                          
│── README.md                                                                                                                                                                                                                                                        
│── images/                       # plots/screenshots                                                                                                                                                          


---

## 📌 How It Works

-User enters applicant details (income, dependents, credit history, etc.)                                                                                                                                                                                  
-Model transforms categorical inputs → encoded features                                                                                                                                                                                                
-Random Forest predicts loan approval status                                                                                                                                                                                            
-App displays Approved/Rejected with probability score

## 📜 License
This project is licensed under the MIT License.
