# Define some numerical variables
integer_number = 10          # An integer
floating_number = 3.14      # A floating-point number
complex_number = 2 + 3j     # A complex number

# Display the types of these numbers
print(f"Integer: {integer_number}, Type: {type(integer_number)}")
print(f"Float: {floating_number}, Type: {type(floating_number)}")
print(f"Complex: {complex_number}, Type: {type(complex_number)}")

# Basic arithmetic operations
sum_result = integer_number + floating_number  # Addition
difference_result = integer_number - floating_number  # Subtraction
product_result = integer_number * floating_number  # Multiplication
division_result = integer_number / floating_number  # Division
floor_division_result = integer_number // 3  # Floor division
modulus_result = integer_number % 3  # Modulus (remainder)

# Print results of arithmetic operations
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
print(f"Floor Division: {floor_division_result}")
print(f"Modulus: {modulus_result}")

# Built-in numerical methods
abs_value = abs(-5)  # Absolute value
round_value = round(3.75)  # Rounds to the nearest integer
max_value = max(1, 2, 3, 4, 5)  # Maximum value in a set of numbers
min_value = min(1, 2, 3, 4, 5)  # Minimum value in a set of numbers
pow_value = pow(2, 3)  # 2 raised to the power of 3 (2^3)

# Print results of built-in methods
print(f"Absolute Value: {abs_value}")
print(f"Rounded Value: {round_value}")
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")
print(f"Power Value (2^3): {pow_value}")

# Important notes about numbers:
# 1. Integers can be positive, negative, or zero and have no fractional part.
# 2. Floating-point numbers can represent decimal values but may have precision issues due to their binary representation.
# 3. Complex numbers have a real part and an imaginary part (e.g., 2 + 3j).
# 4. Python supports arithmetic operations like +, -, *, /, // (floor division), and % (modulus).
# 5. The `math` module provides advanced mathematical functions (e.g., sqrt, sin, cos).
# 6. Be aware of type conversion; you can convert between types using int(), float(), and complex().

# Additional built-in methods for numbers:
# - `abs(x)`: Returns the absolute value of x.
# - `round(x[, n])`: Rounds x to n digits (default is 0).
# - `max(iterable, *[, key])`: Returns the largest item in an iterable or the largest of two or more arguments.
# - `min(iterable, *[, key])`: Returns the smallest item in an iterable or the smallest of two or more arguments.
# - `pow(x, y)`: Returns x raised to the power of y (x^y).

