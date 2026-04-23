print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'RiskScore': [2, 3, 4, 5, 6, 7, 8, 9],
    'Disease': [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Age', 'RiskScore']]
y = df['Disease']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

report = classification_report(y_test, y_pred)

print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
print("\nClassification Report:\n", report)