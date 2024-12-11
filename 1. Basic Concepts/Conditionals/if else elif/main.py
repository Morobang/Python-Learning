# Define a number to check
number = 7  # You can change this number to test different cases

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")  # This runs if the number is greater than 0
elif number < 0:
    print(f"{number} is a negative number.")  # This runs if the number is less than 0
else:
    print(f"{number} is zero.")                # This runs if the number is exactly 0

# Example with age classification
age = 18  # You can change this age to test different categories

# Classify age into different groups
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Important notes about if-elif-else statements:
# 1. The `if` statement checks a condition. If it's true, it runs the code below it.
# 2. The `elif` (else if) statement checks another condition if the first one was false.
# 3. The `else` statement runs if none of the above conditions were true.
# 4. Conditions can use comparison operators (like >, <, ==) to compare values.
# 5. Indentation (using spaces) shows which lines of code belong to which condition.
