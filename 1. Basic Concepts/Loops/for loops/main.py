# This script demonstrates how to use for loops in Python.

# 1. Using a for loop with a range
# The range function generates a sequence of numbers.
for i in range(5):  # This will loop through numbers 0 to 4
    print("Current number:", i)  # Print the current number

# 2. For loop with a string
# You can iterate over each character in a string.
word = "hello"
for char in word:  # Loop through each character in the string
    print("Current character:", char)  # Print the current character

# 3. For loop with a tuple
# A tuple is like a list, but it's immutable (cannot be changed).
my_tuple = (10, 20, 30)
for number in my_tuple:  # Loop through each number in the tuple
    print("Current number from tuple:", number)  # Print the current number

# 4. Nested for loops
# You can use a for loop inside another for loop.
for i in range(2):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"Outer loop {i}, Inner loop {j}")  # Print current loop values

# 5. Using for loops with the enumerate function
# This helps you keep track of the index while looping.
animals = ["cat", "dog", "bird"]
for index, animal in enumerate(animals):  # Loop with index and value
    print(f"Index {index}: {animal}")  # Print the index and animal
