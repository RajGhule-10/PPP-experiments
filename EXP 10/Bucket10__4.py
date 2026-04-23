print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

A = tf.constant([[1, 2],
                 [3, 4]], dtype=tf.int32)

B = tf.constant([[5, 6],
                 [7, 8]], dtype=tf.int32)

matrix_mul = tf.matmul(A, B)

element_mul = tf.multiply(A, B)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

print("\nMatrix Multiplication (A x B):\n", matrix_mul)
print("\nElement-wise Multiplication:\n", element_mul)