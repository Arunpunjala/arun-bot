from flask import Blueprint, request, jsonify, render_template
from .model import generate_response

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"response":"No message"}), 400

    reply = generate_response(message)

    return jsonify({"response":reply})