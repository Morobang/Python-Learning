print("Welcome to the rollcoaster!")
height = input("What is your height in cm?\n")
age = int(input("how old are you:\t"))

ticket1 = 7
ticket2 = 20
#height = int(input("What is your height in cm?\n"))
height = int(height)

if height > 120:
    if age <= 18:
        print(f"Please, pay $ {ticket1}.")
    else:
        print("Please, pay $" + str(ticket2))
else:
    print("Sorry: you can not ride the rollercoaster")
 