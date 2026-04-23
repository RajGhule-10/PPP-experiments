print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

data = tf.constant([
    [25, 1, 7],
    [30, 2, 6],
    [40, 3, 8]
], dtype=tf.int32)

print("\nDataset Tensor:\n", data)

print("\nShape:", data.shape)

print("Rank:", tf.rank(data))

print("Data Type:", data.dtype)