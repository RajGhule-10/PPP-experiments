print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from tensorflow.keras.layers import TextVectorization

reviews = [
    "This product is amazing",
    "Very bad experience",
    "I love it",
    "Not good at all",
    "Excellent quality",
    "Worst product"
]

labels = np.array([1, 0, 1, 0, 1, 0])

vectorizer = TextVectorization(output_mode='int')
vectorizer.adapt(reviews)

X = vectorizer(reviews)

print("\nOriginal Reviews:")
for r in reviews:
    print(r)

print("\nLabels:", labels)

print("\nVectorized Reviews:\n", X)

print("\nVocabulary:", vectorizer.get_vocabulary())