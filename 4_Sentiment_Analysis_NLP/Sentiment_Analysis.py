import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🧠",
    layout="wide"
)

# Download necessary NLTK resources
@st.cache_resource
def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')

download_nltk_resources()

# Preprocessing the text data
def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(filtered_tokens)

# Encode sentiment labels to numerical values
def encode_labels(df, label_column):
    label_map = {'positive': 0, 'negative': 1, 'neutral': 2}
    return df[label_column].map(label_map)

# Train model using Naive Bayes
def train_model(df, text_column, label_column):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df[text_column])
    y = encode_labels(df, label_column)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    return model, vectorizer, y_test, y_pred

# Save trained model and vectorizer
def save_model(model, vectorizer, filename_prefix):
    with open(f'{filename_prefix}_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open(f'{filename_prefix}_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

# Load trained model and vectorizer
def load_model(filename_prefix):
    with open(f'{filename_prefix}_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open(f'{filename_prefix}_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

# Plot confusion matrix
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    return plt

# Streamlit UI
st.title("🧠 Sentiment Analysis System")

tab1, tab2 = st.tabs(["Train Model", "Classify Text"])

# Train Model Tab
with tab1:
    st.header("Train New Model")
    uploaded_file = st.file_uploader("Upload training data (CSV)", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(df.head())
        
        col1, col2 = st.columns(2)
        with col1:
            text_column = st.selectbox("Select text column", df.columns.tolist())
        with col2:
            label_column = st.selectbox("Select label column", df.columns.tolist())
        
        if st.button("Train Model"):
            with st.spinner("Training model..."):
                df['processed_text'] = df[text_column].apply(preprocess_text)
                model, vectorizer, y_test, y_pred = train_model(df, 'processed_text', label_column)
                
                save_model(model, vectorizer, 'sentiment_classifier')
                
                st.success("Model trained successfully!")
                
                st.subheader("Model Performance")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("Classification Report:")
                    report = classification_report(y_test, y_pred, target_names=['Positive', 'Negative', 'Neutral'])
                    st.text(report)
                
                with col2:
                    st.write("Confusion Matrix:")
                    fig = plot_confusion_matrix(y_test, y_pred)
                    st.pyplot(fig)

# Classify Text Tab
with tab2:
    st.header("Classify Text")
    
    try:
        model, vectorizer = load_model('sentiment_classifier')
        model_status = "Using trained model"
    except:
        model_status = "No trained model found. Please train a model first."
    
    st.info(model_status)
    
    if model_status == "Using trained model":
        text_input = st.text_area("Enter text:", height=200)
        
        if st.button("Classify"):
            if text_input:
                processed_text = preprocess_text(text_input)
                text_vectorized = vectorizer.transform([processed_text])
                prediction = model.predict(text_vectorized)[0]
                probability = model.predict_proba(text_vectorized)[0]
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### Sentiment: {'Positive' if prediction == 0 else 'Negative' if prediction == 1 else 'Neutral'}")
                    
                with col2:
                    st.markdown("### Confidence Scores:")
                    st.write(f"Positive probability: {probability[0]:.2%}")
                    st.write(f"Negative probability: {probability[1]:.2%}")
                    st.write(f"Neutral probability: {probability[2]:.2%}")
                
                confidence_bar = st.progress(0)
                confidence_bar.progress(float(probability.max()))
            else:
                st.warning("Please enter some text to classify")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("""
This sentiment analysis system allows you to:
1. Train a new model using your own dataset
2. Classify text using the trained model
""")

st.sidebar.header("Instructions")
st.sidebar.write("""
To train a new model:
1. Go to 'Train Model' tab
2. Upload a CSV file with text and sentiment labels
3. Select appropriate columns
4. Click 'Train Model'

To classify text:
1. Go to 'Classify Text' tab
2. Enter text for sentiment classification
3. Click 'Classify'
""")
