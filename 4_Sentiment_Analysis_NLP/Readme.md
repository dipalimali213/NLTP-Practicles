# 🧠 Sentiment Analysis System

This project is a **web-based Sentiment Analysis System** built with `Streamlit`. It enables users to **train a sentiment classification model** using their own CSV dataset and then **classify text** in real time using the trained model.

---

## 🚀 Features

✅ Upload your own dataset (CSV format)  
✅ Train a custom sentiment analysis model  
✅ Enter and classify text for sentiment prediction  
✅ Simple and intuitive tab-based UI:
- **Train Model** – Upload data and train
- **Classify Text** – Input text and get predictions  

---

## 🎯 Project Objective

To create an interactive and beginner-friendly platform that allows users—especially students and researchers—to easily build and test sentiment analysis models without writing any code. This tool simplifies the machine learning workflow for text classification.

---

## 🛠️ Tech Stack

- **Frontend & App Framework:** Streamlit  
- **Backend:** Python  
- **Libraries Used:**
  - `pandas` – Data manipulation
  - `scikit-learn` – ML model training
  - `nltk` – Text preprocessing
  - `joblib` – Model serialization

---

## 📚 How It Works

### 🧪 Train Model
1. Navigate to the **Train Model** tab.
2. Upload a CSV file that includes:
   - One column for **text**
   - One column for **sentiment labels**
3. Select the correct columns from the dropdowns.
4. Click **Train Model** to train and save your classifier.

### 🔍 Classify Text
1. Go to the **Classify Text** tab.
2. Enter a sentence or phrase.
3. Click **Classify** to see the predicted sentiment.

---

## 📁 Sample CSV Format

| text                        | sentiment |
|-----------------------------|-----------|
| I love this app!            | positive  |
| This is a terrible product. | negative  |

---

## 💡 Future Enhancements

- Confusion matrix and accuracy metrics  
- Expanded preprocessing options  
- Support for multiple languages  
- Model explainability (e.g., word importance)

