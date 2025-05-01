# ngram_model.py

from collections import defaultdict
import re

def nested_dict():
    return defaultdict(int)

class NgramModel:
    def __init__(self, n):
        self.n = n
        self.model = defaultdict(nested_dict)

    def preprocess(self, text):
        return re.sub(r'[^\w\s]', '', text.lower()).split()

    def train(self, messages):
        for text in messages:
            tokens = self.preprocess(text)
            for i in range(len(tokens) - self.n + 1):
                context = tuple(tokens[i:i+self.n-1])
                next_word = tokens[i+self.n-1]
                self.model[context][next_word] += 1

    def predict(self, context_text):
        tokens = self.preprocess(context_text)
        context = tuple(tokens[-(self.n - 1):])
        if context in self.model:
            sorted_words = sorted(self.model[context].items(), key=lambda x: x[1], reverse=True)
            return sorted_words[0][0]
        return "No prediction available"
