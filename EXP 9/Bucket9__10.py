print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

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

model = KNeighborsClassifier()

param_grid = {
    'n_neighbors': [1, 3]
}

grid = GridSearchCV(model, param_grid, cv=2)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)