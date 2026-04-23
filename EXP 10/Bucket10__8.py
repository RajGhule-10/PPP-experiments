print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

tensor = tf.constant([[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]])

print("\nOriginal Tensor:\n", tensor)


print("\nElement at (0,1):", tensor[0, 1])

print("Element at (2,2):", tensor[2, 2])

print("\nFirst Row:", tensor[0])

print("First Column:", tensor[:, 0])

print("\nSub-matrix:\n", tensor[0:2, 0:2])

print("\nLast Two Rows:\n", tensor[1:])