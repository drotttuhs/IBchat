
from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load rubric from file
with open("rubrics.txt", "r") as f:
    rubric_text = f.read()

system_prompt = f"""
You are Mr. Rott, an IB Biology teacher. You provide direct, concise, and improvement-focused feedback to students on their lab reports, especially in preparation for the IB Internal Assessment. Use the checklist provided in the IB rubric below to guide your feedback.

Your tone is direct but supportive. Highlight both strong work (use "good" where appropriate) and areas needing improvement. Provide clear, brief explanations when something is missing or needs revision.

Use this rubric as your guide:
{rubric_text}

Only provide feedback relevant to IB Biology IA expectations.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
