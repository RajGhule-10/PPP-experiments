print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
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

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc_before = accuracy_score(y_test, y_pred)

param_grid = {
    'n_neighbors': [1, 3]
}

grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=2)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
y_pred_tuned = best_model.predict(X_test)

acc_after = accuracy_score(y_test, y_pred_tuned)

print("Accuracy BEFORE tuning:", acc_before)
print("Accuracy AFTER tuning:", acc_after)

print("Best Parameters:", grid.best_params_)

if acc_after > acc_before:
    print("Model improved after tuning.")
elif acc_after < acc_before:
    print("Model performance decreased after tuning.")
else:
    print("No change in performance.")