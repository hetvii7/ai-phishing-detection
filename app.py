import streamlit as st
import joblib

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("AI-Based Phishing Detection System")

user_input = st.text_area("Enter Email Text or URL")

if st.button("Check"):
    if user_input.strip() != "":
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)

        if prediction[0] == 1:
            st.error("⚠ Phishing Detected!")
        else:
            st.success("✅ Safe Content")