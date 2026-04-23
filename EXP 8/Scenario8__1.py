print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([30, 40, 50, 60, 70])

model = LinearRegression()

model.fit(X, y)

new_hours = np.array([[6], [7]])
predicted_marks = model.predict(new_hours)

print("New Study Hours:", new_hours.flatten())
print("Predicted Marks:", predicted_marks)