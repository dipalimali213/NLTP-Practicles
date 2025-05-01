# 🤖 Practical No. 5 – Chatbot Using TF-IDF and Cosine Similarity

This project presents a basic **rule-based chatbot** that utilizes **TF-IDF Vectorization** and **Cosine Similarity** to generate responses based on predefined conversational data. It is an introductory implementation of Natural Language Processing (NLP) techniques in a chatbot context.

---

## 📁 Dataset: `chatbot_data.csv`

The dataset used for this chatbot consists of two main columns:

- `user_input`: Sample user queries or phrases.
- `bot_response`: Corresponding bot replies to each input.

---

## 🎯 Objective

To create a simple chatbot that:
- Matches user inputs with the most relevant question in a dataset.
- Returns the corresponding bot response using similarity scoring.
- Demonstrates how NLP techniques like **text preprocessing**, **vectorization**, and **similarity measures** can be applied in chatbot development.

---

## 🚀 Features

✅ Accepts user input in a conversational loop.  
✅ Preprocesses text by converting to lowercase and removing special characters.  
✅ Converts text data to numeric format using **TF-IDF vectorization**.  
✅ Uses **cosine similarity** to compare user input with dataset entries.  
✅ Responds with the closest matching predefined response.  
✅ Exits the conversation gracefully with a command.

---

## 🛠️ Tools and Technologies

- **Programming Language:** Python  
- **Libraries Used:**
  - `pandas` – Data manipulation and CSV reading.
  - `nltk` – Natural language text preprocessing.
  - `scikit-learn` – TF-IDF vectorizer and cosine similarity.
  - `re` – Regular expressions for text cleaning.




