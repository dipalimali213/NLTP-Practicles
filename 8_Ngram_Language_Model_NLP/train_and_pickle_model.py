# train_and_pickle_model.py

import pickle
import pandas as pd
from ngram_model import NgramModel  # Import the NgramModel class from the new ngram_model.py

# Load your dataset (ensure you have a file 'messages.csv' with a 'message' column)
df = pd.read_csv('messages.csv')  # Adjust path if necessary

# Initialize the Ngram model with n=2 (bigram)
model = NgramModel(n=2)

# Train the model
model.train(df['message'])

# Save the trained model as a pickle file
with open("model/ngram_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as ngram_model.pkl")
