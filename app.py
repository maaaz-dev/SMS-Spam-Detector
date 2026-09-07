import streamlit as st
import joblib

st.set_page_config(
    page_title="SMS Spam Detector"
)

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("SMS Spam Detector")
st.subheader("Check whether your message is SPAM or GENUINE")

st.write("Enter an SMS below and click the button to check it.")

message = st.text_area(
    "Your SMS",
    placeholder="Type or paste your message here..."
)

if st.button("Check Message"):
    if message.strip():
        message_tfidf = vectorizer.transform([message])
        prediction = model.predict(message_tfidf)

        if prediction[0] == 1:
            st.error("SPAM")
        else:
            st.success("GENUINE")
    else:
        st.warning("Please enter an SMS.")

st.divider()

st.write("Model Accuracy: 96.68%")
st.caption("Built with Python, Scikit-learn and Streamlit")