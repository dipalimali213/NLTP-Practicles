from flask import Flask, request, render_template_string
from transformers import pipeline
import PyPDF2
import io
app = Flask(__name__)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PDF Q&A System</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #cfd9df, #e2ebf0);
            color: #333;
        }
        header {
            background-color: #3f51b5;
            padding: 25px;
            color: white;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        .main {
            max-width: 700px;
            margin: 60px auto;
            background-color: #ffffffee;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }
        label {
            font-size: 18px;
            font-weight: 600;
        }
        input[type="file"] {
            padding: 12px;
            margin-top: 10px;
            margin-bottom: 20px;
            border: 2px dashed #3f51b5;
            border-radius: 8px;
            width: 100%;
            background-color: #f5f5f5;
            font-size: 16px;
            cursor: pointer;
        }
        input[type="text"] {
            width: 100%;
            padding: 14px;
            margin: 10px 0 25px;
            font-size: 17px;
            border: 1.5px solid #999;
            border-radius: 8px;
        }
        .center-btn {
            text-align: center;
        }
        button {
            background-color: #ec407a;
            color: white;
            padding: 14px 30px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            background-color: #d81b60;
            transform: scale(1.05);
        }
        .result {
            margin-top: 30px;
            background-color: #fce4ec;
            padding: 20px;
            border-left: 6px solid #ec407a;
            border-radius: 10px;
            font-size: 18px;
        }
        footer {
            background-color: #3f51b5;
            color: white;
            text-align: center;
            padding: 14px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        .header-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <header>
        Question and Answering
    </header>
    <div class="main">
        <form method="POST" enctype="multipart/form-data">
            <label>Select a PDF file:</label><br>
            <input type="file" name="pdf_file" required>
            <label>Enter your question:</label>
            <input type="text" name="question" placeholder="Type your question here..." required>
            <div class="center-btn">
                <button type="submit">Get Answer</button>
            </div>
        </form>
        {% if answer %}
        <div class="result">
            <strong>Answer:</strong><br>{{ answer }}
        </div>
        {% endif %}
    </div>
    <footer>
        &copy; 2025 | Designed by TYDS T3 Batch
    </footer>
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        question = request.form['question']
        if pdf_file:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
            context = ""
            for page in pdf_reader.pages:
                context += page.extract_text() or ""
            if context.strip():
                result = qa_pipeline(question=question, context=context)
                answer = result['answer']
            else:
                answer = "Could not extract text from the PDF."
    return render_template_string(HTML_TEMPLATE, answer=answer)
if __name__ == '__main__':
    app.run(debug=True)
