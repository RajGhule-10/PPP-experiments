print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

scalar = tf.constant(5)

vector = tf.constant([1, 2, 3])

matrix = tf.constant([[1, 2], [3, 4]])

tensor3d = tf.constant([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])


print("\nScalar:", scalar)
print("Vector:", vector)
print("Matrix:\n", matrix)
print("3D Tensor:\n", tensor3d)


add = tf.add(matrix, matrix)

sub = tf.subtract(matrix, matrix)

mul = tf.multiply(matrix, matrix)

mat_mul = tf.matmul(matrix, matrix)

print("\nAddition:\n", add)
print("Subtraction:\n", sub)
print("Element-wise Multiplication:\n", mul)
print("Matrix Multiplication:\n", mat_mul)

print("\n--- Tensor Attributes ---")

print("Matrix Shape:", matrix.shape)
print("Matrix Rank:", tf.rank(matrix))
print("Matrix Data Type:", matrix.dtype)

print("\n3D Tensor Shape:", tensor3d.shape)
print("3D Tensor Rank:", tf.rank(tensor3d))
print("3D Tensor Data Type:", tensor3d.dtype)