import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Score': [15, 25, 35, 45, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Score']

# Train model
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')

print("Model trained and saved!")