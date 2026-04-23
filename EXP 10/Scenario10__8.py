print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

data = tf.constant([
    [25, 1, 7],
    [30, 2, 6],
    [40, 3, 8]
], dtype=tf.int32)

print("\nDataset Tensor:\n", data)

print("\nFirst Row:", data[0])

print("Second Row:", data[1])

print("\nFirst Column:", data[:, 0])

print("Second Column:", data[:, 1])

print("\nElement at (1,2):", data[1, 2])

print("\nSub-matrix:\n", data[0:2, 0:2])