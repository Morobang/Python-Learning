#simple functions
def greet():
    print("Hello")
    print("Hello")
    print("Hello")

greet()


#function that alllows for input 
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How Are You Doing {name}")

greet_with_name(input("Enter Your Name: "))


#function with more than one input


def greetings(name, lastname):
    print(f"Hello {name} {lastname}")
    print(f"Name: {name} \t Lastname: {lastname}")

greetings("Rocket", "Tshigidimisa")