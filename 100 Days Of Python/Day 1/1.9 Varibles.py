"""
Variables
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains jiuce
write 3 lines of code to switch the contents of the variables
you are not allowed to type the words "milk" or "juice".
You are only allowed to use variables to solve this exercise
"""

glass1 = "juice"
glass2 = "milk"
print(glass1 + glass2)

glass3 = glass1
glass1 = glass2 
glass2 = glass3

print(glass1+glass2)

