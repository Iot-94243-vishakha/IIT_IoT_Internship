""" Create a package named operations with the following structure:
operations/ 
│── __init__.py 
│── arithmetic.py 
│── string_ops.py 
arithmetic.py should contain functions for addition and multiplication.
string_ops.py should contain functions to reverse a string and count vowels.
Write a Python program to import this package and demonstrate all functions."""

import Operations.arithmetic as Oa
import Operations.string_ops as Os

while True:
    print("\n---- Calculator Menu ----")
    print("1. Wanna do Arithmetic Operation")
    print("2. Wanna do String Function")
    print("---------------------------")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1: 
            a= float(input("Enter number: "))
            b = float(input("Enter number: "))

            print("\n---- Calculator Menu ----")
            print("1.Addition")
            print("2.Multiplication")
            print("---------------------------")
            
            select =int(input("Select function:"))

            match select:
                case 1:
                 print("Result =",Oa.addition(a,b))
                 print("---------------------------")
                case 2:
                 print("Result =",Oa.multiplication(a,b))
                 print("---------------------------")
                case _:
                 print("Invalid choice!")
        case 2:
            text=(input("Enter string : ")).lower()

            print("\n---- Calculator Menu ----")

            print("1.Reverse")
            print("2.Count Vowels")
            print("---------------------------")
            
            select =int(input("Select function:"))

            match select:
                case 1:                 
                 print("Result =",Os.reverse(text))
                 print("---------------------------")
                case 2:
                 print("Result =",Os.vowels(text))
                 print("---------------------------")
                case _:
                 print("Invalid choice!")
        case _:
          print("Invalid choice!")
    

    