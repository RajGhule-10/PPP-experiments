print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

A = tf.constant([[1, 2],
                 [3, 4]], dtype=tf.float32)

B = tf.constant([[2, 0],
                 [1, 2]], dtype=tf.float32)

result = tf.matmul(A, B)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nResult of A x B:\n", result)