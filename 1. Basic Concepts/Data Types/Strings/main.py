# Define variables for name components
name = "John"
middle_name = 'dog'  # Using single quotes for the middle name
lastname = "Wick"

# Determine the data type of the 'name' variable
datatype = type(name)

# Print formatted name components, with title case applied
print(f"name: {name}\nmiddlename: {middle_name}\nlast name: {lastname} ".title())
print(f"the data type of name variable : {datatype}".title())

# Print each character in the name variable separately
print(name[0] + name[1] + name[2] + name[3])  # Outputs: John

# String manipulation examples
print("the rocket is going up".upper())  # Convert to uppercase
print("the rocket is going up".lower())  # Convert to lowercase
print("     i think this can work better when storing data into a database".strip().title())  # Remove whitespace and capitalize

# Combine first and last names
fullname = name + " " + lastname
print(fullname)  # Outputs: John Wick

# Encode the string "Rocket" to bytes
print("Rocket".encode())  # Outputs: b'Rocket'

# Important notes about strings:
# 1. Strings are immutable in Python; you cannot change them in place.
# 2. You can use slicing to access specific parts of a string, e.g., name[1:3] returns 'oh'.
# 3. The '+' operator can be used to concatenate strings.
# 4. Strings support a variety of methods, such as .find(), .replace(), .split(), and .join().
# 5. Using f-strings (like f"{var}") allows for easier and more readable string formatting.
