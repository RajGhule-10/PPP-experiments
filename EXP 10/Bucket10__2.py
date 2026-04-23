print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

int_tensor = tf.constant([1, 2, 3], dtype=tf.int32)
float_tensor = tf.constant([1.5, 2.5, 3.5], dtype=tf.float32)
string_tensor = tf.constant(["AI", "ML", "DL"], dtype=tf.string)

print("\nInteger Tensor:", int_tensor)
print("Float Tensor:", float_tensor)
print("String Tensor:", string_tensor)

print("\nData Types:")
print("Integer Tensor dtype:", int_tensor.dtype)
print("Float Tensor dtype:", float_tensor.dtype)
print("String Tensor dtype:", string_tensor.dtype)

print("\nComparison Example:")
print("int_tensor + 1:", int_tensor + 1)
print("float_tensor * 2:", float_tensor * 2)
