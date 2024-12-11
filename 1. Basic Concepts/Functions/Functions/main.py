# functions_examples.py

# Example 1: Defining and Calling a Function
print("Example 1: Defining and Calling a Function")


def greet(name):  # Define a function named 'greet' that takes one parameter, 'name'
    """
    This function greets the person passed as an argument.

    Parameters:
    name (str): The name of the person to greet.
    """
    print("Hello,", name)  # Print a greeting message


# Calling the function with different names
greet("Alice")  # Output: Hello, Alice
greet("Bob")  # Output: Hello, Bob
print()  # Print a newline for better readability

# Example 2: Function with Return Value
print("Example 2: Function with Return Value")


def add(a, b):  # Define a function named 'add' that takes two parameters
    """
    This function returns the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b  # Return the sum of a and b


# Call the function and store the result
result = add(5, 3)  # Output: 8
print("The sum of 5 and 3 is:", result)
print()  # Print a newline for better readability

# Example 3: Function with Default Parameter
print("Example 3: Function with Default Parameter")


def multiply(x, y=1):  # Define a function that takes two parameters, with y having a default value of 1
    """
    This function multiplies two numbers, with the second being optional.

    Parameters:
    x (int or float): The first number.
    y (int or float, optional): The second number. Defaults to 1.

    Returns:
    int or float: The product of x and y.
    """
    return x * y  # Return the product of x and y


# Call the function with both parameters and just the first one
print("5 multiplied by 2 is:", multiply(5, 2))  # Output: 10
print("5 multiplied by default value is:", multiply(5))  # Output: 5
print()  # Print a newline for better readability

# Example 4: Function with Variable Number of Arguments
print("Example 4: Function with Variable Number of Arguments")


def print_numbers(*args):  # Accept any number of arguments
    """
    This function prints all the numbers passed to it.

    Parameters:
    *args: A variable number of numerical arguments.
    """
    for number in args:  # Loop through each argument
        print(number)  # Print the number


# Call the function with multiple arguments
print_numbers(1, 2, 3, 4, 5)  # Output: 1, 2, 3, 4, 5
print()  # Print a newline for better readability

# Example 5: Function Documentation and Error Handling
print("Example 5: Function Documentation and Error Handling")


def divide(a, b):
    """
    This function divides a by b and returns the result.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    float: The result of the division or an error message if dividing by zero.
    """
    if b == 0:  # Check for division by zero
        return "Error: Cannot divide by zero!"  # Return an error message
    return a / b  # Return the result of the division


# Call the function with valid arguments
print("10 divided by 2 is:", divide(10, 2))  # Output: 5.0
# Call the function with division by zero
print(divide(10, 0))  # Output: Error message
