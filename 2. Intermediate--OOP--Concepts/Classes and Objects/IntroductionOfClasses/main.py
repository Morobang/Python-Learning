class Laptop:
    def __init__ (self, brand, name, color , year ):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year

    def Switch_On(self):
        print("Laptop is on")

Laptop1 = Laptop("Lenovo" ,"IdeaPad","Gray", 2024)
Laptop2 = Laptop("Dell","Inspiration","black",2025)

print(f"{Laptop1.brand} and {Laptop2.brand} are good brands" )

On = str(input("Do you want to switch on the pc:".title()))

if On == "Yes":
    Laptop1.Switch_On()
