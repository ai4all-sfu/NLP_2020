import os
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" # Suppress TF warnings

MAX_SEQUENCE_LENGTH = 400

def tokenize(text, tokenizer):
    seq = tokenizer.texts_to_sequences(text)
    padded_seq = sequence.pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
    return padded_seq

if __name__ == "__main__":
    # Load saved model
    model = tf.keras.models.load_model("toxic_cnn.h5")

    # Load saved tokenizer
    with open("toxic_tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    print("Check if your comment is toxic or not! Press `q` to quit.")

    while True:
        # Get input from user
        comment = input("Enter comment: ")
        if comment.lower() == "q":
            break

        # Tokenize input
        tok_comment = tokenize([comment], tokenizer)

        # Make prediction
        pred = model.predict(tok_comment)

        # Output result
        if pred[0] < 0.5:
            print("Hmm, not toxic...")
        else:
            print("That's toxic!")