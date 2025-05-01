from flask import Flask, render_template, request
import pickle
from ngram_model import NgramModel, nested_dict

app = Flask(__name__)

# Load the trained model (ensure the pickle file exists in the correct path)
with open("model/ngram_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    context = request.form['context']
    prediction = model.predict(context)
    return render_template('index.html', context=context, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use a different port if necessary
