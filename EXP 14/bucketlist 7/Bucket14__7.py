print("SY-5", "Raj Ghule", "Roll_no-40")

from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    chart = False

    if request.method == 'POST':
        try:
            v1 = int(request.form['value1'])
            v2 = int(request.form['value2'])
            v3 = int(request.form['value3'])

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

        except:
            chart = False

    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    app.run(debug=True)