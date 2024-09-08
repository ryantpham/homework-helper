from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("API key is not set in the environment variables. Check your .env file.")

openai.api_key = api_key

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a homework help tutor named Theresa..."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        response = get_response(user_prompt)
        return jsonify({'response': response})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
