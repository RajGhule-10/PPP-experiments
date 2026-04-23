print("SY-5", "Raj Ghule", "Roll_no-40")

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    number = request.form['usernumber']
    return f"Hello {name}, your number is {number}"

if __name__ == '__main__':
    app.run(debug=True)