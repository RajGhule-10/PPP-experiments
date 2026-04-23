from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = (celsius * 9/5) + 32
            result = round(fahrenheit, 2)
        except:
            result = "Invalid Input!"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)