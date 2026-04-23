print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf
from tensorflow.keras.layers import TextVectorization, Embedding, Dense, GlobalAveragePooling1D
from tensorflow import keras
import numpy as np

texts = [
    "I love this product",
    "This is amazing",
    "Very bad experience",
    "I hate it",
    "Absolutely fantastic",
    "Not good at all"
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

test_text = ["This product is good"]
test_seq = vectorizer(test_text)

prediction = model.predict(test_seq)

print("\nTest Text:", test_text)
print("Predicted Sentiment (probability):", prediction[0][0])