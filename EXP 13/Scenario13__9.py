print("SY-5", "Raj Ghule", "Roll_no-40")

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Random Decision API is running!"

@app.route('/decision', methods=['GET'])
def random_decision():
    decision = random.choice(["Approved", "Rejected"])

    return jsonify({
        "prediction": decision
    })

if __name__ == '__main__':
    app.run(debug=True)