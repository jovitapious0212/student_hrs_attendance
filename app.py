import streamlit as st
import joblib
import os

# Load model
model_path = os.path.join(
    os.path.dirname(__file__),
    "student_result_prediction_model.pkl"
)

model = joblib.load(model_path)

# App title
st.title("Student Pass/Fail Prediction")
st.write("Predict student result based on Study Hours and Attendance")

# User inputs
hours = st.number_input(
    "Enter Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

attendance = st.number_input(
    "Enter Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

# Prediction button
if st.button("Predict"):

    # Input order must match training order
    prediction = model.predict([[hours, attendance]])

    if prediction[0] == 1:
        st.success("Student is predicted to PASS ✅")
    else:
        st.error("Student is predicted to FAIL ❌")
