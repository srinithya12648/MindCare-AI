import os
from flask import Flask, render_template, request
import google.generativeai as genai

# Paste your Gemini API key here or set GEMINI_API_KEY in your environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    prompt = f"""
You are MindCare AI.

You provide:
- emotional support
- stress management tips
- anxiety coping techniques
- study motivation
- positive encouragement

Never diagnose diseases.
Never claim to be a doctor.
If user mentions suicide or self-harm, advise contacting emergency services, a crisis helpline, or a trusted person immediately.

User: {userText}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)