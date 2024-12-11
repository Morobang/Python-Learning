# List of Common Built-in Exceptions
# 1. ValueError: Raised when a function receives an inappropriate value.
# 2. TypeError: Raised when an operation is applied to an object of inappropriate type.
# 3. IndexError: Raised when trying to access an index that is out of range.
# 4. KeyError: Raised when trying to access a dictionary with a non-existent key.
# 5. FileNotFoundError: Raised when trying to open a file that does not exist.
# 6. AttributeError: Raised when an invalid attribute reference is made.
# 7. ZeroDivisionError: Raised when attempting to divide by zero.
# 8. ImportError: Raised when an import statement fails.
# 9. NameError: Raised when a local or global name is not found.
# 10. StopIteration: Raised when the next() function is called on an exhausted iterator.





# Example 1: Basic Try-Except Block
print("Example 1: Basic Try-Except Block")

try:
    # Attempt to divide by zero
    result = 10 / 0
except ZeroDivisionError:  # Catch specific exception for division by zero
    print("Error: Cannot divide by zero!")  # Print an error message

print()  # Print a newline for better readability

# Example 2: Catching Multiple Exceptions
print("Example 2: Catching Multiple Exceptions")

try:
    value = int(input("Enter a number: "))  # Attempt to convert input to integer
    result = 10 / value  # Attempt to divide by the user input
except ValueError:  # Catch ValueError if input is not a valid integer
    print("Error: Please enter a valid number!")  # Print error message
except ZeroDivisionError:  # Catch division by zero
    print("Error: Cannot divide by zero!")  # Print error message

print()  # Print a newline for better readability

# Example 3: Using Finally
print("Example 3: Using Finally")

try:
    file = open("non_existent_file.txt", "r")  # Attempt to open a non-existent file
except FileNotFoundError:  # Catch the file not found error
    print("Error: File not found!")  # Print error message
finally:
    print("This block always executes, regardless of errors.")  # Final message

print()  # Print a newline for better readability

# Example 4: Raising Exceptions
print("Example 4: Raising Exceptions")


def check_age(age):
    """
    This function checks if the age is valid.

    Parameters:
    age (int): The age to check.

    Raises:
    ValueError: If the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")  # Raise an exception for invalid age
    print("Valid age:", age)  # Print valid age


# Test the function with valid and invalid inputs
try:
    check_age(25)  # Valid age
    check_age(-5)  # This will raise an exception
except ValueError as e:  # Catch the raised ValueError
    print("Error:", e)  # Print the error message

print()  # Print a newline for better readability

# Example 5: Custom Exception Handling
print("Example 5: Custom Exception Handling")


class CustomError(Exception):
    """Custom exception class."""
    pass


def check_positive(number):
    """
    This function checks if a number is positive.

    Parameters:
    number (int or float): The number to check.

    Raises:
    CustomError: If the number is not positive.
    """
    if number <= 0:
        raise CustomError("Number must be positive!")  # Raise custom exception
    print("Number is positive:", number)  # Print valid number


# Test the custom exception
try:
    check_positive(10)  # Valid input
    check_positive(-1)  # This will raise a custom exception
except CustomError as e:  # Catch the custom exception
    print("Error:", e)  # Print the error message


"""
# error_handling_basic_examples.py

# 1. ValueError
print("Example 1: ValueError")
try:
    num = int("not_a_number")  # Attempt to convert an invalid string to an integer
except ValueError:
    print("Caught a ValueError!")

print()  # Newline for better readability

# 2. TypeError
print("Example 2: TypeError")
try:
    result = "string" + 1  # Attempt to add a string and an integer
except TypeError:
    print("Caught a TypeError!")

print()  # Newline for better readability

# 3. IndexError
print("Example 3: IndexError")
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Attempt to access an index that does not exist
except IndexError:
    print("Caught an IndexError!")

print()  # Newline for better readability

# 4. KeyError
print("Example 4: KeyError")
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])  # Attempt to access a key that does not exist
except KeyError:
    print("Caught a KeyError!")

print()  # Newline for better readability

# 5. FileNotFoundError
print("Example 5: FileNotFoundError")
try:
    with open("non_existent_file.txt", "r"):  # Attempt to open a non-existent file
        pass
except FileNotFoundError:
    print("Caught a FileNotFoundError!")

print()  # Newline for better readability

# 6. AttributeError
print("Example 6: AttributeError")
class MyClass:
    pass

obj = MyClass()
try:
    obj.some_method()  # Attempt to call a method that does not exist
except AttributeError:
    print("Caught an AttributeError!")

print()  # Newline for better readability

# 7. ZeroDivisionError
print("Example 7: ZeroDivisionError")
try:
    result = 75 / 0  # Attempt to divide by zero
except ZeroDivisionError:
    print("Caught a ZeroDivisionError!")

print()  # Newline for better readability

# 8. ImportError
print("Example 8: ImportError")
try:
    import non_existent_module  # Attempt to import a non-existent module
except ImportError:
    print("Caught an ImportError!")

print()  # Newline for better readability

# 9. NameError
print("Example 9: NameError")
try:
    print(undefined_variable)  # Attempt to access a variable that has not been defined
except NameError:
    print("Caught a NameError!")

print()  # Newline for better readability

# 10. StopIteration
print("Example 10: StopIteration")
my_iter = iter([1, 2, 3])
try:
    for _ in range(4):  # Attempt to get one more item than exists in the iterator
        print(next(my_iter))
except StopIteration:
    print("Caught a StopIteration!")


"""