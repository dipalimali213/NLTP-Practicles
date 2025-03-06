import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import base64

# Set up Streamlit page
st.set_page_config(
    page_title="Text Preprocessing Tool",
    page_icon="📝",
    layout="wide"
)

# Download necessary NLTK resources
def download_nltk_resources():
    resources = ['punkt', 'stopwords', 'wordnet', 'omw-1.4']
    for resource in resources:
        nltk.download(resource)

download_nltk_resources()

# Load NLTK stopwords safely
try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())  # Tokenization & lowercase
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]  # Remove stopwords
    stemmed = [stemmer.stem(word) for word in filtered_tokens]  # Stemming
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]  # Lemmatization
    return filtered_tokens, stemmed, lemmatized

# Function to create CSV download link
def get_download_link(df, filename):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download Processed CSV</a>'
    return href

# Streamlit App UI
st.title("📝 Text Preprocessing in NLP")
st.write("Upload a CSV file and process text data using NLTK.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        with st.spinner("Loading data..."):
            df = pd.read_csv(uploaded_file)

        # Select text column
        text_column = st.selectbox(
            "Select the text column to process",
            df.columns.tolist()
        )

        if st.button("Process Text"):
            progress_bar = st.progress(0)
            status_text = st.empty()

            processed_results = []
            total_rows = len(df)

            for idx, text in enumerate(df[text_column]):
                filtered_tokens, stemmed, lemmatized = preprocess_text(text)
                processed_results.append({
                    'filtered_tokens': " ".join(filtered_tokens),
                    'stemmed': " ".join(stemmed),
                    'lemmatized': " ".join(lemmatized)
                })

                progress = (idx + 1) / total_rows
                progress_bar.progress(progress)
                status_text.text(f"Processing row {idx + 1} of {total_rows}")

            df['Filtered Tokens'] = [result['filtered_tokens'] for result in processed_results]
            df['Stemmed'] = [result['stemmed'] for result in processed_results]
            df['Lemmatized'] = [result['lemmatized'] for result in processed_results]

            st.subheader("Preview of Processed Data")
            st.dataframe(df)

            st.markdown("### Download Processed Data")
            st.markdown(get_download_link(df, "processed_data.csv"), unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

# Sidebar Information
with st.sidebar:
    st.header("About")
    st.write("""
    This tool helps preprocess text data using NLTK. It performs:
    - Tokenization
    - Stopword Removal
    - Stemming
    - Lemmatization
    """)

    st.header("Instructions")
    st.write("""
    1. Upload a CSV file
    2. Select the text column to process
    3. Click 'Process Text'
    4. View results and download processed data
    """)
