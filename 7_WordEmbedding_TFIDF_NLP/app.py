from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.utils import simple_preprocess
import gensim.downloader as api

app = Flask(__name__)

# 1. Load pre-trained embeddings once (this may take a moment first run)
wv = api.load('glove-wiki-gigaword-100')

@app.route("/", methods=["GET", "POST"])
def index():
    tfidf_result = None
    w2v_result = None
    error = None

    if request.method == "POST":
        raw_text = request.form.get("input_text", "").strip()
        query = request.form.get("word", "").strip().lower()

        if not raw_text or not query:
            error = "Please provide both a block of text and a word."
        else:
            # --- TF-IDF on user’s corpus ---
            docs = [line for line in raw_text.split("\n") if line]
            tfidf = TfidfVectorizer()
            mat = tfidf.fit_transform(docs)
            tfidf_result = {
                "features": tfidf.get_feature_names_out().tolist(),
                "matrix": mat.toarray().tolist()
            }

            # --- Word2Vec via pre-trained GloVe ---
            try:
                vec = wv[query].tolist()
                sims = wv.most_similar(query, topn=5)
                w2v_result = {
                    "vector": vec,
                    "similar": sims
                }
            except KeyError:
                w2v_result = None
                error = f"‘{query}’ not in vocabulary of the pre-trained model."

    return render_template("index.html",
                           tfidf_result=tfidf_result,
                           w2v_result=w2v_result,
                           error=error)

if __name__ == "__main__":
    app.run(debug=True)
