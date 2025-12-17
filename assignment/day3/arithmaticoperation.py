def add(a,b):
   return a + b

def sub(a,b):
   return a - b

def mul(a,b):
   return a * b

def div(a,b):
   return a / b


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
            print("Result =", sub(a,b))
        case 3:
            print("Result =", mul(a,b))
        case 4:
             if b == 0:
              print("Error: Division by zero")
             else:
              print("Result =", div(a,b))
        case _:
          print("Invalid choice!")