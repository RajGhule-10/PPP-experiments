print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Result': ['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass']
}

df = pd.DataFrame(data)

df['Result'] = df['Result'].map({'Fail': 0, 'Pass': 1})

X = df[['StudyHours']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Actual values:", list(y_test))
print("Predicted values:", list(y_pred))

print("\nAccuracy Score:", accuracy)
print("\nConfusion Matrix:\n", cm)