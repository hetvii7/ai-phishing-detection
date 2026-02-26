import streamlit as st
import joblib

# Load trained model
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🔐 AI-Based Phishing Detection System")

st.caption("AI-powered system to detect phishing emails and malicious URLs for cybersecurity protection.")

st.write("Enter email content or URL to check if it's phishing.")

user_input = st.text_area("Enter Email Text or URL")

if st.button("Check"):
    if user_input.strip() != "":
        input_vector = vectorizer.transform([user_input])

        prediction = model.predict(input_vector)
        probability = model.predict_proba(input_vector)[0][1]

        if prediction[0] == 1:
            st.error(f"⚠ Phishing Detected! Risk Score: {probability*100:.2f}%")
            st.write("This result is based on suspicious language patterns and potential malicious links.")
        else:
            st.success(f"✅ Safe Content (Risk Score: {probability*100:.2f}%)")
            st.write("No significant phishing indicators were detected.")

    else:
        st.warning("Please enter some text")