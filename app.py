from flask import Flask, render_template
from transformers import pipeline
import random

app = Flask(__name__)

# Load Hugging Face text generation model
generator = pipeline("text-generation", model="distilgpt2")

prompts = [
    "Give me a motivational quote about success.",
    "Generate an inspirational quote for students.",
    "Write a positive quote about hard work.",
    "Give a quote about learning and growth."
]

@app.route("/")
def home():
    prompt = random.choice(prompts)
    result = generator(
        prompt,
        max_length=50,
        num_return_sequences=1
    )
    quote = result[0]["generated_text"]
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
