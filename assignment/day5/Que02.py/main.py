"""Create a module named calculator.py that contains the following functions:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
Write another Python program that imports this module and performs all operations for two user-input
numbers."""



from calculator import *
while True:
    print("---------------------------")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n---- Calculator Menu ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("---------------------------")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Result =", add(a,b))
        case 2:
            print("Result =", subtract(a, b))
        case 3:
            print("Result =",multiply(a, b))
        case 4:
             if b == 0:
              print("Error: Division by zero")
             else:
              print("Result =",divide(a, b))
        case _:
          print("Invalid choice!")
    

    