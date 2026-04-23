import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Age': [10, 5, 3, 2, 1],
    'Price': [50, 70, 90, 110, 130]
}

df = pd.DataFrame(data)

X = df[['Area', 'Bedrooms', 'Age']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'house_model.pkl')

print("Model saved!")