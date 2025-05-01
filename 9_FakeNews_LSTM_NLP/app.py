import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
import os

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Load model and vectorizer
current_dir = os.path.dirname(__file__)
model = joblib.load(os.path.join(current_dir, "fake_news_model.pkl"))
vectorizer = joblib.load(os.path.join(current_dir, "tfidf_vectorizer.pkl"))

# Clean text function
def clean_text(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    return " ".join(tokens)

# Page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Dark theme custom styling
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: #e0e0e0;
    }
    .main {
        background-color: #0f0f0f;
    }
    h1 {
        text-align: center;
        color: #00ffae;
    }
    .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton > button {
        color: white;
        background: #00ffae;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>📰 Fake News Detector</h1>", unsafe_allow_html=True)

# Manual Text Input Only
st.markdown("Paste a news article or type some content below to analyze 👇")

manual_text = st.text_area("Enter article text here", height=300)

if st.button("Analyze Text"):
    if manual_text.strip() == "":
        st.warning("⚠️ Please enter some text before analyzing.")
    else:
        with st.spinner("Analyzing text..."):
            cleaned = clean_text(manual_text)
            transformed = vectorizer.transform([cleaned])
            prediction = model.predict(transformed)[0]

            st.subheader("🧠 Prediction Result:")
            if prediction == 1:
                st.success("✅ This news article appears to be *Real*.")
            else:
                st.error("❌ This news article appears to be *Fake*.")
