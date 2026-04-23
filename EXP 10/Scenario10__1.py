print("SY-5", "Raj Ghule", "Roll_no-40")

import tensorflow as tf

temperature = tf.constant(36.5)

daily_sales = tf.constant([100, 200, 150, 300, 250])

student_marks = tf.constant([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print("\nScalar (Temperature):", temperature)
print("Vector (Daily Sales):", daily_sales)
print("Matrix (Student Marks):\n", student_marks)

print("\n--- Scalar Properties ---")
print("Shape:", temperature.shape)
print("Rank:", tf.rank(temperature))
print("Data Type:", temperature.dtype)

print("\n--- Vector Properties ---")
print("Shape:", daily_sales.shape)
print("Rank:", tf.rank(daily_sales))
print("Data Type:", daily_sales.dtype)

print("\n--- Matrix Properties ---")
print("Shape:", student_marks.shape)
print("Rank:", tf.rank(student_marks))
print("Data Type:", student_marks.dtype)