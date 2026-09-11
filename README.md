<div align="center">

# 📩 SMS Spam Detector

### Machine Learning based SMS Classification

<p>
  <a href="https://sms-spam-detector-maaaz.streamlit.app">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  </a>
  <a href="https://github.com/maaaz-dev/SMS-Spam-Detector">
    <img src="https://img.shields.io/badge/⭐%20GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

<p>
  <strong>Classify SMS messages as SPAM or GENUINE using Machine Learning.</strong>
</p>

</div>

---

## 🚀 Live Demo

<div align="center">

### Try the application

### 🔗 [sms-spam-detector-maaaz.streamlit.app](https://sms-spam-detector-maaaz.streamlit.app)

</div>

---

## 📌 About the Project

**SMS Spam Detector** is a Machine Learning project that predicts whether an SMS message is **SPAM** or **GENUINE**.

The project uses:

- **TF-IDF** for converting text into numerical features
- **Multinomial Naive Bayes** for classification
- **Streamlit** for the web interface
- **Joblib** for saving and loading the trained model

The model is trained on the SMS Spam Collection dataset.

---

## 🧠 How It Works

```text
                📩 SMS Message
                       │
                       ▼
              ┌─────────────────┐
              │   TF-IDF        │
              │  Vectorization  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Multinomial    │
              │  Naive Bayes    │
              └────────┬────────┘
                       │
                       ▼
                🎯 Prediction
                   /       \
                  /         \
                 ▼           ▼
              🚨 SPAM    ✅ GENUINE
