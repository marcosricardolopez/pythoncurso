import os
import requests
import urllib3

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

urllib3.disable_warnings()
load_dotenv(".env")

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = (
    "Eres un profesor de Python amable. Explica fácil y claro."
)


def preguntar_a_groq(pregunta, historial=None):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if historial:
        messages.extend(historial)
    messages.append({"role": "user", "content": pregunta})

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        verify=False
    )

    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text}"

    resultado = response.json()
    return resultado["choices"][0]["message"]["content"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}

    pregunta = (data.get("message") or "").strip()
    historial = data.get("history") or []

    if not pregunta:
        return jsonify({"response": "No escribiste ninguna pregunta."})

    if not GROQ_API_KEY:
        return jsonify({"error": "Falta GROQ_API_KEY en el archivo .env"}), 500

    respuesta = preguntar_a_groq(pregunta, historial)

    return jsonify({"response": respuesta})


if __name__ == "__main__":
    app.run(debug=True)