print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization, Embedding, Dense, GlobalAveragePooling1D
from tensorflow import keras

texts = [
    "I love this product",
    "This is amazing",
    "Very bad experience",
    "I hate it",
    "Excellent quality",
    "Worst product ever"
]

labels = np.array([1, 1, 0, 0, 1, 0])

vectorizer = TextVectorization(output_mode='int')
vectorizer.adapt(texts)

X = vectorizer(texts)

vocab_size = len(vectorizer.get_vocabulary())
embedding_dim = 8

model = keras.Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim),
    GlobalAveragePooling1D(),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X, labels, epochs=20, verbose=1)