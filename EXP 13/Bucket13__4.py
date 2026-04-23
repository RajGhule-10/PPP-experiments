from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/sum', methods=['GET'])
def calculate_sum():

    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))


    result = num1 + num2


    return jsonify({
        "num1": num1,
        "num2": num2,
        "sum": result
    })

if __name__ == '__main__':
    app.run(debug=True)