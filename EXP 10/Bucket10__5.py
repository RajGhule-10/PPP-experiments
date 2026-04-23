print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

tensor = tf.constant([[1, 2, 3],
                      [4, 5, 6]], dtype=tf.int32)

print("\nTensor:\n", tensor)

print("\nShape:", tensor.shape)

print("Rank:", tf.rank(tensor))

print("Size:", tf.size(tensor))

print("Data Type:", tensor.dtype)