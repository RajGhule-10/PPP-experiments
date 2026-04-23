print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 7, 8],
    [7, 8, 9],
    [8, 9, 10]
])

y = np.array([0, 0, 0, 1, 1, 1, 1, 1])
y = keras.utils.to_categorical(y, num_classes=2)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = keras.Sequential([
    keras.Input(shape=(3,)),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=30, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test)

predictions = model.predict(X_test)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)

print("\nPredictions (Softmax Probabilities):\n", predictions)