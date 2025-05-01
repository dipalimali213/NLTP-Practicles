# 📩 N-gram Based Message Content Prediction

This project implements a **Bigram Language Model (n=2)** using a custom `NgramModel` class to predict the next word in a message sequence. The trained model is deployed using a **Flask web application**, allowing users to enter a message and receive a predicted continuation.

---

## 📁 Dataset: N-gram Message Content

The dataset consists of a collection of short text messages, such as conversations or phrases. These messages are used to train the language model to learn common word sequences and predict the most probable next word given a context.

---

## 🎯 Objective

To build and deploy a simple N-gram model that can:
- Learn word sequences from user messages
- Predict the next likely word based on previous input (context)
- Offer a web-based interface to test the model predictions

---

## ⚙️ How It Works

### 1. **Preprocessing**
- Messages are converted to lowercase and cleaned of punctuation.
- Each message is split into tokens (words).

### 2. **Training the N-gram Model**
- For `n=2` (Bigram), the model learns the probability of a word following another word.
- A dictionary structure stores frequencies of word sequences using nested dictionaries.

### 3. **Saving the Model**
- The trained N-gram model is serialized and saved using `pickle`.

### 4. **Web Application (Flask)**
- A simple Flask app is created to:
  - Accept user input (context text)
  - Predict the next word using the trained model
  - Display the result on a user-friendly web page

---

## 🌐 Application Workflow

1. **User Input:**  
   Enter a message or phrase in the text field.

2. **Prediction Engine:**  
   The last word(s) are used as context to predict the most probable next word.

3. **Display Result:**  
   The predicted word is shown alongside the user input.

---

## 🧠 Techniques Used

- **N-gram Language Modeling** (Bigram in this case)
- **Flask** for backend web integration
- **Regex** for text preprocessing
- **Pickle** for model serialization
- **Pandas** for dataset handling


