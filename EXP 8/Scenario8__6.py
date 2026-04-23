print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
    'Income': [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    'CreditScore': [500, 550, 600, 650, 700, 750, 800, 850],
    'LoanStatus': [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Income', 'CreditScore']]
y = df['LoanStatus']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

new_applicant = [[55000, 720]]
prediction = model.predict(new_applicant)

print("Test Predictions:", y_pred)
print("Actual Values:", list(y_test))

print("\nNew Applicant Prediction (1=Approve, 0=Reject):", prediction[0])