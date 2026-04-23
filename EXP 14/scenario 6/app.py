from flask import Flask, render_template, request
import joblib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

model = joblib.load('house_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    chart = False

    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            age = int(request.form['age'])

            features = np.array([[area, bedrooms, age]])
            pred = model.predict(features)[0]
            prediction = round(pred, 2)


            labels = ['Area', 'Bedrooms', 'Age']
            values = [area, bedrooms, age]

            plt.figure(figsize=(5,4))
            plt.bar(labels, values)
            plt.title("Feature Contribution")

            if not os.path.exists('static'):
                os.makedirs('static')

            plt.savefig('static/chart.png')
            plt.close()

            chart = True

        except:
            prediction = "Invalid Input!"

    return render_template('index.html', prediction=prediction, chart=chart)

if __name__ == '__main__':
    app.run(debug=True)