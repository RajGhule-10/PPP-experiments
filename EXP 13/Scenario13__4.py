from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "BMI Calculator API is running!"

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    try:

        data = request.get_json()

        weight = float(data['weight'])   # in kg
        height = float(data['height'])   # in meters


        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({
            "weight": weight,
            "height": height,
            "bmi": round(bmi, 2),
            "category": category
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)