from flask import Flask, render_template, request, session, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key is loaded correctly
if api_key is None:
    raise ValueError("API key is not set in the environment variables. Check your .env file.")

# Set the OpenAI API key
openai.api_key = api_key

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Function to get a response from OpenAI
def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 
                 "You are a homework help tutor. You are to explain any questions I ask in a way that anyone from K-12, Young aspiring professionals, and Non-native english speakers can understand. Also, When it comes to writing content, two factors are crucial, 'perplexity' and 'burstiness'. Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness."
                 },
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        response = get_response(user_prompt)
        return response  # Return only the response text
    
    # On GET request, clear chat history
    session.pop('chat_history', None)
    return render_template("index.html", chat_history=[])