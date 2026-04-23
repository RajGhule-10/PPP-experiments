print("SY-5", "Raj Ghule", "Roll_no-40")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Loan Eligibility Checker API is running!"

@app.route('/loan', methods=['POST'])
def check_loan():
    try:

        data = request.get_json()

        salary = float(data['salary'])

        if salary >= 50000:
            decision = "Loan Approved"
        else:
            decision = "Loan Rejected"

        return jsonify({
            "salary": salary,
            "decision": decision
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)