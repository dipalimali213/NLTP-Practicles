# 🤖 Chatbot Using TF-IDF and Cosine Similarity

This project presents a basic **rule-based chatbot** that utilizes **TF-IDF Vectorization** and **Cosine Similarity** to generate responses based on predefined conversational data. It demonstrates essential Natural Language Processing (NLP) techniques using Python.

---

## 📁 Dataset: `chatbot_data.csv`

The dataset used for this chatbot contains two key columns:

- `user_input`: Sample user queries or phrases.
- `bot_response`: Appropriate responses for each user query.

---

## 🎯 Objective

To build a simple chatbot capable of:
- Matching real-time user queries with existing inputs in the dataset.
- Retrieving the most relevant response using similarity scoring techniques.
- Applying core NLP methods like preprocessing, vectorization, and semantic similarity.

---

## 🚀 Features

✅ User-friendly conversational interface.  
✅ Real-time input processing and response generation.  
✅ Basic text preprocessing: lowercasing and punctuation removal.  
✅ TF-IDF-based text vectorization.  
✅ Cosine similarity for response matching.  
✅ Exit the conversation using a command (`quit`).

---

## 🛠️ Tools and Technologies

- **Programming Language:** Python  
- **Libraries Used:**
  - `pandas` – For CSV file handling and data manipulation.
  - `nltk` – For stopword handling and preprocessing.
  - `scikit-learn` – For TF-IDF vectorization and cosine similarity.
  - `re` – For text cleaning using regular expressions.

---

## ⚙️ How It Works

The chatbot works through the following steps:

1. **Load the Dataset:**  
   The CSV file `chatbot_data.csv` is read using `pandas`.

2. **Text Preprocessing:**  
   All text in `user_input` and `bot_response` columns is:
   - Converted to lowercase  
   - Stripped of punctuation and special characters

3. **TF-IDF Vectorization:**  
   Preprocessed user inputs are transformed into TF-IDF vectors that numerically represent the importance of words in each phrase.

4. **User Query Handling:**  
   - The chatbot accepts real-time input from the user.
   - This input is also preprocessed and vectorized.

5. **Cosine Similarity Computation:**  
   - The chatbot calculates the similarity between the user's query and every pre-existing user input.
   - The most similar (i.e., highest cosine score) input is identified.

6. **Response Generation:**  
   - The corresponding `bot_response` for the best-matching input is retrieved and printed.
   - The chatbot continues the conversation until the user types `"quit"`.


