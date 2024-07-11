import os
import pickle
import gradio as gr
from tensorflow.keras.layers import TextVectorization
import tensorflow as tf

# Define categories
categories = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

# Load the vectorizer
vectorizer_pickle = pickle.load(open(os.path.join("models", "vectorizer.pkl"), "rb"))
vectorizer = TextVectorization.from_config(vectorizer_pickle['config'])
vectorizer.set_weights(vectorizer_pickle['weights'])

# Load the model
model = tf.keras.models.load_model(os.path.join("models", "safe_chat.h5"))

def predict_hate(text):
    results = model.predict(vectorizer([text]))[0] > 0.5

    results_text = ""

    for idx, category in enumerate(categories):
        results_text += f"{category}: {results[idx]}\n"

    return results_text

demo = gr.Interface(fn=predict_hate,
                         inputs=gr.Textbox(lines=2, placeholder="Toxic comments go here!"),
                         outputs="text")

demo.launch()