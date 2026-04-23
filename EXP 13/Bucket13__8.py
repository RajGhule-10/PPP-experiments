print("SY-5", "Raj Ghule", "Roll_no-40")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "POST API is running!"

@app.route('/data', methods=['POST'])
def receive_data():
    try:

        data = request.get_json()

        name = data.get('name')
        age = data.get('age')

        return jsonify({
            "message": "Data received successfully",
            "name": name,
            "age": age
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)