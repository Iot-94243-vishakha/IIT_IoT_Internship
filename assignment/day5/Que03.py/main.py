"""Create a module named geometry.py with functions to calculate:
Area of a circle
Area of a rectangle
Write a Python program that imports only the required functions from the module and calculates areas
based on user input."""


from geometry import calculate_Area_of_circle as cir
from geometry import calculate_Area_of_rectangle as rec

while True:
   
    print("\n---- Calculator Menu ----")
    print("1. Area of a circle")
    print("2. Area of a rectangle")
    print("---------------------------")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            r = float(input("Enter Radius number: "))

            print("Result =",cir(r))
            print("---------------------------")
        case 2:
            l= float(input("Enter Length number: "))
            b = float(input("Enter Breadth number: "))

            print("Result =",rec(l,b))
            print("---------------------------")
        case _:
          print("Invalid choice!")
    

    