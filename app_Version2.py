from flask import Flask, request, render_template, jsonify
from assistant.core import get_virtual_assistant_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/assistant", methods=["POST"])
def assistant():
    user_message = request.json.get("message")
    response = get_virtual_assistant_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)