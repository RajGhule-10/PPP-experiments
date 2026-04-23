print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.Input(shape=(2,)),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.summary()