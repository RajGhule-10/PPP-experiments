from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    chart = False
    error = ""

    if request.method == 'POST':
        try:
            value1 = request.form['value1']
            value2 = request.form['value2']
            value3 = request.form['value3']

            # Validation for empty input
            if value1 == "" or value2 == "" or value3 == "":
                error = "Please fill all fields."
            else:
                v1 = int(value1)
                v2 = int(value2)
                v3 = int(value3)

                values = [v1, v2, v3]
                labels = ['Value 1', 'Value 2', 'Value 3']

                plt.figure(figsize=(5,4))
                plt.bar(labels, values)
                plt.title("Bar Chart")

                if not os.path.exists('static'):
                    os.makedirs('static')

                plt.savefig('static/chart.png')
                plt.close()

                chart = True

        except ValueError:
            error = "Please enter valid numeric values."

    return render_template('index.html', chart=chart, error=error)

if __name__ == '__main__':
    app.run(debug=True)