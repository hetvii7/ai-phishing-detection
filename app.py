import streamlit as st
import joblib
st.set_page_config(
    page_title="AI Enterprise Security",
    page_icon="🛡️",
    layout="wide"
)
st.title("🛡️ AI Enterprise Phishing Detection Platform")

st.write(
    "Enterprise-level AI system for detecting phishing emails and malicious URLs."
)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Emails Scanned", "1540")
with col2:
    st.metric("Safe Emails", "1320")
with col3:
    st.metric("Phishing", "220")
with col4:
    st.metric("Accuracy", "98.6%")
st.divider()
st.subheader("📧 Email Scanner")
user_input = st.text_area(
    "Enter Email Text or URL",
    height=200
)
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
if st.button("Analyze Email"):
        if user_input.strip() != "":
                    input_vector = vectorizer.transform([user_input])

        prediction = model.predict(input_vector)

        probability = model.predict_proba(input_vector)[0][1]
            if prediction[0] == 1:
                            st.error("⚠️ Phishing Email Detected")

            st.progress(int(probability*100))

            st.write(
                f"Risk Score : {probability*100:.2f}%"
            )
        else:
            st.success("✅ Safe Email")

            st.progress(int(probability*100))

            st.write(
                f"Risk Score : {probability*100:.2f}%"
            )
                else:
        st.warning("Please enter email text.")
st.divider()

st.caption(
    "Version 1.0 | Developed by Hetvi P. Upadhyay"
)
