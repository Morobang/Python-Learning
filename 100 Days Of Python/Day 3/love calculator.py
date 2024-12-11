'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
    1.) Take both people's names and check for the number of times the letters in the word TRUE occurs.
    2.) Then check for the number of times the letters in the word LOVE occurs.
    3.) Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is *z*."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
'''

print("The love calculator is calculating your score...")
name1 = input("what is your name? ")
name2 = input("What is their name?")

combined_name = name1 + name2

lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

first_digit = t + r + u + e


l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

second_digit = l + o + v + e

love_score = str(first_digit) + str(second_digit)

