# 🎬 Movie Review Sentiment Classification Using TF-IDF and Word2Vec

This project demonstrates two popular Natural Language Processing (NLP) techniques—**TF-IDF vectorization** and **Word2Vec embeddings**—applied to a **movie review dataset** to classify sentiments using a machine learning model. It evaluates how textual data can be converted into numerical form and used to train classification models effectively.

---

## 📁 Dataset: Movie Review

The dataset contains user-written movie reviews labeled with sentiment tags (e.g., positive or negative). Preprocessing is applied to clean and normalize the review text for both vectorization methods.

---

## 🎯 Objective

The main objective of this project is to:
- Implement and compare two popular word representation techniques: **TF-IDF** and **Word2Vec**
- Train classification models to identify sentiments in movie reviews
- Save both the models and vectorizers for future inference

---

## 🚀 Features

✅ Preprocesses raw movie reviews by removing noise and lowercasing text  
✅ Converts text into numerical format using:
- **TF-IDF Vectorization** (for sparse representation)
- **Word2Vec Embeddings** (for dense semantic representation)  
✅ Trains a **Logistic Regression** classifier on both representations  
✅ Evaluates the performance of both approaches using classification metrics  
✅ Saves trained models and vectorizers to the `models/` directory

---

## 🧠 Techniques Used

### 🔹 TF-IDF (Term Frequency-Inverse Document Frequency)
- Transforms text data into a matrix of feature vectors based on term importance.
- Captures word frequency weighted by how rarely they appear across the corpus.

### 🔹 Word2Vec
- Learns vector representations of words based on their context in sentences.
- Averages word vectors to represent full reviews for classification.

---

## ⚙️ How It Works

1. **Data Cleaning:**  
   All reviews are lowercased and stripped of special characters.

2. **Train-Test Split:**  
   The dataset is divided into training and testing sets (80/20 ratio).

3. **TF-IDF Pipeline:**
   - Reviews are vectorized using TF-IDF.
   - A logistic regression model is trained on the resulting features.
   - The model is evaluated and saved.

4. **Word2Vec Pipeline:**
   - Reviews are tokenized and used to train a Word2Vec model.
   - Each review is represented by the average of its word vectors.
   - Another logistic regression model is trained and evaluated.

5. **Model Saving:**  
   All trained models and vectorizers are saved using `pickle` and `gensim`.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **ML Models:** Logistic Regression  
- **Libraries Used:**
  - `pandas`, `numpy` – Data processing
  - `sklearn` – TF-IDF, ML model, and evaluation
  - `gensim` – Word2Vec embeddings
  - `re` – Text cleaning
  - `pickle` – Saving models


