print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTraining set size (X_train):", X_train.shape)
print("Testing set size (X_test):", X_test.shape)

print("\nTraining labels size (y_train):", y_train.shape)
print("Testing labels size (y_test):", y_test.shape)