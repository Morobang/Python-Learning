# Define some Boolean variables
is_true = True       # A Boolean representing true
is_false = False     # A Boolean representing false

# Display the values and types of the Boolean variables
print(f"Is True: {is_true}, Type: {type(is_true)}")
print(f"Is False: {is_false}, Type: {type(is_false)}")

# Boolean operations
and_result = is_true and is_false    # AND operation
or_result = is_true or is_false      # OR operation
not_result = not is_true             # NOT operation

# Print results of Boolean operations
print(f"AND Result: {and_result}")   # Outputs: False
print(f"OR Result: {or_result}")     # Outputs: True
print(f"NOT Result: {not_result}")   # Outputs: False

# Comparison examples
a = 5
b = 10
is_equal = (a == b)                  # Checks if a is equal to b
is_greater = (a > b)                 # Checks if a is greater than b
is_less_or_equal = (a <= b)          # Checks if a is less than or equal to b

# Print results of comparisons
print(f"Is Equal: {is_equal}")                  # Outputs: False
print(f"Is Greater: {is_greater}")              # Outputs: False
print(f"Is Less or Equal: {is_less_or_equal}")  # Outputs: True

# Important notes about Boolean data types:
# 1. Boolean values can only be True or False.
# 2. Boolean operations can be performed using `and`, `or`, and `not`.
# 3. Boolean values are often the result of comparisons or logical operations.
# 4. The `bool()` function can convert other types to Boolean:
#    - Non-zero numbers, non-empty strings, and non-empty collections return True.
#    - Zero, None, and empty collections return False.
