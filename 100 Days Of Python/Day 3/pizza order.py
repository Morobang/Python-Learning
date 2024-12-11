print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
    bill = int(15)
    if add_pepperoni == "Y":
        bill = bill + 2
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    else:
        print("Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    else:
        if extra_cheese == "Y":
            bill = bill + 1
            print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
        else:
            print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
elif size == "M":
    bill = int(20)
    if add_pepperoni == "Y"
    bill = bill + 3
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    else:
    print("Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
  
  else:
    if extra_cheese == Y:
      bill = bill + 1
      print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    else:
      print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
elif size == "L":
  bill = int(25)
  if add_pepperoni == "Y"
     bill = bill + 3
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
  else:
    print("Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")

   else:
    if extra_cheese == "Y":
      bill = bill + 1
      print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    else:
      print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")







print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
