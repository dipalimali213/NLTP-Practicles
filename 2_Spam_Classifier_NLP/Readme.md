# 📧 Spam Classification System Using Streamlit, NLTK and Scikit-learn

This project is a **Spam Classification System** built with `Streamlit`, `NLTK` and `Scikit-learn` that allows you to:
- ✅ **Train a New Model** using your own dataset.
- ✅ **Classify Emails** to identify whether they are **HAM** or **SPAM**.
- ✅ Visualize model performance and download trained models.

---

## 🚀 **Features**
- **Train a Model:**
    - Upload a CSV file containing email text and labels.
    - Automatically preprocess the text by removing stopwords and tokenizing.
    - Use `TfidfVectorizer` and `Multinomial Naive Bayes` for training.
    - Evaluate model performance and visualize confusion matrix.
    - Save the trained model and vectorizer for future classification.

- **Classify Email:**
    - Load the trained model to classify email content.
    - Get predictions with probability scores.
    - Display classification results with confidence scores.

- **Data Preprocessing:**
    - Tokenization and lowercase conversion.
    - Stopword removal using NLTK.
    - Tfidf Vectorization of processed text.

---

## 🎯 **Project Objective**
The objective of this project is to build an interactive web application that performs **email spam classification**. It allows users to train a model on their dataset and use the trained model to classify new emails.

---

## 🛠️ **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:**
  - `pandas` – For CSV file processing and data handling.
  - `nltk` – For text tokenization and stopword removal.
  - `scikit-learn` – For model training, vectorization, and classification.
  - `seaborn` & `matplotlib` – For visualization.
  - `pickle` – For saving and loading models.

---

## 📚 **How It Works**
### ▶️ **Training the Model**
1. **Upload CSV File:**  
   - The CSV file should contain at least two columns:
     - One with the email text.
     - One with the label (`ham` or `spam`).
2. **Preprocess Text:**
   - Text is converted to lowercase, tokenized, and stopwords are removed.
3. **Train Model:**
   - `TfidfVectorizer` transforms the processed text.
   - `MultinomialNB` trains the classification model.
4. **Save Model:**
   - The trained model and vectorizer are saved as `.pkl` files.

---

### 📩 **Classifying Email**
1. **Load Model:**
   - The trained model and vectorizer are loaded from the saved files.
2. **Preprocess New Text:**
   - The input text is tokenized and stopwords are removed.
3. **Prediction:**
   - The processed text is classified as either **HAM** or **SPAM**.
4. **Confidence Score:**
   - Display probability scores for HAM and SPAM classification.
