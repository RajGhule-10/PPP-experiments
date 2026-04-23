print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf
from tensorflow.keras.layers import TextVectorization, Embedding

text_data = [
    "machine learning",
    "deep learning",
    "artificial intelligence"
]

vectorizer = TextVectorization(output_mode='int')
vectorizer.adapt(text_data)

vectorized_text = vectorizer(text_data)

print("\nVectorized Text:\n", vectorized_text)

vocab_size = len(vectorizer.get_vocabulary())
embedding_dim = 4

embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dim)

embedded_output = embedding_layer(vectorized_text)

print("\nEmbedding Output:\n", embedded_output)