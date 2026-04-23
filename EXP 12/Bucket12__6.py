print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

text_data = [
    "machine learning is fun",
    "deep learning is powerful",
    "AI is the future"
]

vectorizer = TextVectorization(
    output_mode='int'
)

vectorizer.adapt(text_data)

vectorized_text = vectorizer(text_data)

print("\nOriginal Text:")
for t in text_data:
    print(t)

print("\nVectorized Output:\n", vectorized_text)

print("\nVocabulary:", vectorizer.get_vocabulary())