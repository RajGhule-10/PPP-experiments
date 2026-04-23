from flask import Flask, render_template, request
import joblib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    plot_path = None

    if request.method == "POST":
        try:
            f1 = float(request.form["f1"])
            f2 = float(request.form["f2"])
            f3 = float(request.form["f3"])
            f4 = float(request.form["f4"])

            features = np.array([[f1, f2, f3, f4]])

            pred = model.predict(features)[0]
            classes = ["Setosa", "Versicolor", "Virginica"]
            prediction = classes[pred]

            feature_names = ["Sepal Len", "Sepal Wid", "Petal Len", "Petal Wid"]
            values = [f1, f2, f3, f4]

            plt.figure(figsize=(6, 4))
            plt.bar(feature_names, values)
            plt.title("Feature Contribution")

            if not os.path.exists("static"):
                os.makedirs("static")

            plot_path = "static/plot.png"
            plt.savefig(plot_path)
            plt.close()

        except:
            error = "Invalid input! Please enter all values correctly."

    return render_template("index.html", prediction=prediction, error=error, plot_path=plot_path)


if __name__ == "__main__":
    app.run(debug=True)