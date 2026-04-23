from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Temperature Conversion API is running!"

@app.route('/convert', methods=['POST'])
def convert_temperature():
    try:

        data = request.get_json()

        celsius = float(data['celsius'])

        fahrenheit = (celsius * 9/5) + 32

        return jsonify({
            "celsius": celsius,
            "fahrenheit": round(fahrenheit, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)