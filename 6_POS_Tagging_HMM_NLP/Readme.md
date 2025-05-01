# 🧠 HMM POS Tagger Using Streamlit and NLTK

This project presents a **Part-of-Speech (POS) Tagger** built using a **Hidden Markov Model (HMM)** and implemented with **Streamlit** for a user-friendly web interface. It uses the **Brown Corpus** to train the model and applies the **Viterbi Algorithm** to assign the most probable sequence of POS tags to a user-input sentence.

---

## 📁 Dataset: Brown Corpus

The POS tagger model is trained on the **Brown Corpus**, a standard and widely-used tagged corpus in Natural Language Processing, which provides labeled examples for parts of speech in English.

---

## 🎯 Objective

To develop an interactive POS tagger that:
- Takes user-input text and assigns POS tags.
- Uses a probabilistic model (HMM) and dynamic programming (Viterbi) to identify the most likely tag sequence.
- Offers a clear and responsive interface for educational and demonstrative purposes.

---

## 🚀 Features

✅ Input a sentence through a simple text field.  
✅ Tokenize and tag the sentence in real time.  
✅ Display each word with its corresponding POS tag.  
✅ Sidebar navigation for ease of use.  
✅ Organized interface using **Streamlit**.

---

## ⚙️ How It Works

1. **Model Loading:**  
   A pretrained HMM model is loaded from a `.pkl` file containing:
   - Transition probabilities  
   - Emission probabilities  
   - Start probabilities  
   - Tag list (`all_tags`)

2. **Input Sentence Processing:**  
   The user enters a sentence through the web interface. Each word is:
   - Converted to lowercase  
   - Tokenized into a list of words

3. **POS Tagging Using Viterbi Algorithm:**  
   - The Viterbi algorithm is applied to find the most likely sequence of POS tags for the given sentence.
   - It computes the best path of tags using the HMM's statistical probabilities.

4. **Output Display:**  
   The interface displays each word alongside its predicted tag in a structured format, using Streamlit’s column layout.

---

## 🛠️ Tech Stack

- **Frontend Interface:** Streamlit  
- **Backend Logic:** Python  
- **Modeling:** Hidden Markov Model (HMM)  
- **Algorithm:** Viterbi  
- **Dataset:** Brown Corpus  
- **Serialization:** Pickle  

**Libraries Used:**
- `Streamlit` – For interactive web UI
- `NLTK` – For corpus data and tokenization
- `Pickle` – For loading the trained HMM model

---

## 📄 Application Structure

- **Home Page:** Input sentence and view POS tagging results  
- **Instructions Page:** Placeholder for user guidance  
- **About Page:** Brief description of the project  
