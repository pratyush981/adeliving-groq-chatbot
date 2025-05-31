from flask import Flask, request, jsonify, render_template
import requests

# Hardcoded Groq API Key
GROQ_API_KEY = "12345tytresa"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are AdeLiving, a helpful real estate AI assistant."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Error: {e}"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
