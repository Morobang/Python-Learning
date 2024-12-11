# Prompt the user to enter a two-digit number and store it as a string.
# This ensures the input is stored exactly as the user typed, allowing us to access each digit individually.
two_digit_number = input("Enter a two-digit number: ")

####################################
# Convert the input to a string (though it's already a string by default from input()).
# This is done to explicitly ensure we can treat the number as a sequence of characters (digits).
two_digit_number_string = str(two_digit_number)

# Extract the first digit from the string (index 0), then convert it to an integer.
# This allows us to perform arithmetic operations with it.
first_digit = int(two_digit_number_string[0])

# Extract the second digit from the string (index 1), then convert it to an integer.
# This also ensures the second digit can be used for arithmetic.
second_digit = int(two_digit_number_string[1])

# Calculate the sum of the two digits.
sum_of_digits = first_digit + second_digit

# Print the operation and result using an f-string for better formatting.
# This prints the first digit, plus sign, second digit, equals sign, and the sum result.
print(f"{first_digit} + {second_digit} = {sum_of_digits}")
