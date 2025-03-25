# 📝 Text Preprocessing Tool Using Streamlit and NLTK

This project is a **web-based Text Preprocessing Tool** built with `Streamlit` that allows you to upload a CSV file and preprocess text data using the `Natural Language Toolkit (NLTK)`. The tool performs **Tokenization, Stopword Removal, Stemming, and Lemmatization** on text data and provides a downloadable processed CSV file.

---

## 🚀 **Features**
✅ Upload a CSV file containing text data.  
✅ Select the desired text column to preprocess.  
✅ Perform the following NLP operations:
- **Tokenization:** Splitting text into words.
- **Stopword Removal:** Removing common words that do not add significant meaning.
- **Stemming:** Reducing words to their base form.
- **Lemmatization:** Converting words to their root form.  
✅ Preview the processed data in tabular format.  
✅ Download the processed CSV file.

---

## 🎯 **Project Objective**
The objective of this tool is to simplify and automate the text preprocessing steps required for NLP tasks. This tool helps data scientists, NLP practitioners, and researchers by saving time and reducing manual effort.

---

## 🛠️ **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:**
  - `pandas` – For handling CSV and data manipulation.
  - `nltk` – For text preprocessing.
  - `base64` – For generating download links for processed files.

---

## 📚 **How It Works**
1. **Upload CSV File:**  
   Upload a CSV file containing text data. The application reads the file and provides an option to select the text column to be processed.

2. **Select Text Column:**  
   Choose the text column from the dropdown menu that contains the data to be preprocessed.

3. **Text Preprocessing:**  
   Upon clicking the "Process Text" button, the following tasks are performed:
   - Tokenization
   - Stopword Removal
   - Stemming
   - Lemmatization  

4. **Download Processed Data:**  
   The processed data is displayed as a preview, and you can download it as a CSV file.


