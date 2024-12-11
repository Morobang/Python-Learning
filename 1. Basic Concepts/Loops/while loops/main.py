# while_loops_examples.py

# Example 1: Simple While Loop
print("Example 1: Simple While Loop")
count = 0  # Initialize a counter
while count < 5:  # Continue looping while count is less than 5
    print("Current count:", count)  # Print the current count
    count += 1  # Increment the counter by 1
print()  # Print a newline for better readability

# Example 2: While Loop for User Input
print("Example 2: While Loop for User Input")
user_input = ""  # Initialize an empty string
while user_input != "exit":  # Continue until the user types "exit"
    user_input = input("Type something (type 'exit' to quit): ")  # Get user input
    print("You typed:", user_input)  # Print what the user typed
print()  # Print a newline for better readability

# Example 3: While Loop with Break Statement
print("Example 3: While Loop with Break Statement")
number = 0
while True:  # This creates an infinite loop
    if number >= 5:  # Check if the condition to break is met
        break  # Exit the loop if the condition is true
    print("Current number:", number)  # Print the current number
    number += 1  # Increment the number
print()  # Print a newline for better readability

# Example 4: While Loop with Continue Statement
print("Example 4: While Loop with Continue Statement")
count = 0
while count < 5:
    count += 1  # Increment count first
    if count == 3:  # If count is 3, skip the print statement
        continue  # Skip the rest of the loop iteration
    print("Current count:", count)  # This will not print when count is 3
