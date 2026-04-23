from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('house_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            age = int(request.form['age'])

            features = np.array([[area, bedrooms, age]])
            pred = model.predict(features)[0]

            prediction = round(pred, 2)

        except:
            prediction = "Invalid Input!"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)