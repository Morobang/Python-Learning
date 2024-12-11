"""If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪"""




bill = float(input("What was the total bill? R"))
tip = int(input("How much tip would like to give? 10 , 12 , or 15? "))
total_bill = float(bill + tip/100 * bill)
number_of_people = int(input("Hoaw many people to split the bill? "))
each_person_payment = round(total_bill / number_of_people,2)
print(f"Each peron should pay: R{each_person_payment}")
