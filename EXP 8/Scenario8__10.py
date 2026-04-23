print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Pass': [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['StudyHours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)
log_acc = accuracy_score(y_test, log_pred)


knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_pred = knn_model.predict(X_test)
knn_acc = accuracy_score(y_test, knn_pred)


print("Actual Values:", list(y_test))

print("\nLogistic Regression Predictions:", list(log_pred))
print("Logistic Regression Accuracy:", log_acc)

print("\nKNN Predictions:", list(knn_pred))
print("KNN Accuracy:", knn_acc)

if log_acc > knn_acc:
    print("\nLogistic Regression performs better.")
elif knn_acc > log_acc:
    print("\nKNN performs better.")
else:
    print("\nBoth models perform equally.")