# The input() function prompts the user to enter some data.
# It takes a string argument which will be displayed as the prompt message.

# In this case, the input function asks the user for their name.
# The result of this input is passed directly to the print statement.
print("Hello " + input("What is your name?\n")) 

# The first part to execute is the input() function, which displays the message "What is your name?"
# The user enters their name, and the input function returns the entered name as a string.
# The result is concatenated with "Hello " and printed to the console.

# Alternatively, we can break this down into two steps for better readability.

# The input function prompts the user for their name and stores the result in the variable 'name'.
name = input("What Is Your name?")

# The print function then prints the message "Hello" followed by the user's name.
print("Hello " + name)
