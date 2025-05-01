# 📰 Fake News Detection Web App

This project is a web-based application that detects whether a news article is **real** or **fake** using Natural Language Processing (NLP) techniques and a trained machine learning model.

---

## 📁 Dataset: Fake News Articles

The dataset contains labeled news articles where each sample is marked as either:

- `1` → Real news  
- `0` → Fake news

The data includes article text which has been used to train a classification model using TF-IDF features and logistic regression (or similar algorithms).

---

## 🎯 Objective

To create an end-to-end application that:
- Accepts news content as input
- Cleans and vectorizes the input text
- Uses a trained model to classify the article as **real** or **fake**
- Displays the result interactively through a user-friendly web interface

---

## ⚙️ How It Works

### 1. **Text Cleaning**
- Converts text to lowercase
- Removes punctuation
- Filters out stopwords (common but meaningless words like "the", "and", "is")

### 2. **Vectorization**
- Uses a pre-trained **TF-IDF Vectorizer** to convert cleaned text into numerical features

### 3. **Prediction**
- Loads a pre-trained machine learning model (`fake_news_model.pkl`)
- Predicts whether the input article is real or fake

### 4. **User Interface**
- Built with **Streamlit**
- Clean, dark-themed design with input field, result display, and feedback messages

---

## 🌐 Application Flow

1. **User Input:**  
   The user pastes or types a news article into the text area.

2. **Preprocessing & Transformation:**  
   The app cleans the text and transforms it using the loaded TF-IDF vectorizer.

3. **Prediction:**  
   The trained model outputs a prediction — *Real* or *Fake*.

4. **Result Display:**  
   The prediction result is shown with visual feedback (green for real, red for fake).

---

## 🧠 Technologies Used

- **Streamlit** – For web interface  
- **scikit-learn** – For machine learning model  
- **TF-IDF** – For feature extraction  
- **Joblib** – For model serialization  
- **NLTK** – For text preprocessing (stopwords, tokenization)




