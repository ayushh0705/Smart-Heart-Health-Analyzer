import pickle
import pandas as pd
import streamlit as st

# Load your model (update with correct file path if needed)
# Ensure you've saved your model as a pickle (.pkl) file beforehand.
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

st.title("Heart Disease Prediction App")
st.write("Enter the following health data to check the likelihood of heart disease.")

# Input fields for each feature
age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", options=["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3], help="0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic")
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=50, max_value=200)
chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1], help="1: Yes, 0: No")
restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", options=[0, 1, 2], help="0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy")
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=250)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1], help="1: Yes, 0: No")
oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", options=[0, 1, 2], help="0: Upsloping, 1: Flat, 2: Downsloping")
ca = st.selectbox("Number of Major Vessels (0-3) Colored by Fluoroscopy (ca)", options=[0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", options=[1, 2, 3], help="1: Normal, 2: Fixed Defect, 3: Reversible Defect")

# Prepare input data as a DataFrame
input_data = pd.DataFrame([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                          columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prediction = 0  # Dummy prediction until model is loaded

    if prediction == 1:
        st.write("The model predicts that this person has heart disease.")
    else:
        st.write("The model predicts that this person does not have heart disease.")