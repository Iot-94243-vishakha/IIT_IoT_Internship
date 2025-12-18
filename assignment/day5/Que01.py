""". Explore python math and os module. [upload your codes on git]"""

import math
import os

print("Value of PI:", math.pi)
print("Value of e:", math.e)

print("Square root of 25:", math.sqrt(25))
print("Power (2^3):", math.pow(2, 3))
print("Factorial of 5:", math.factorial(5))

print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))



print("Current Directory:", os.getcwd())

print("Files and Folders:", os.listdir())

if not os.path.exists("demo_folder"):
    os.mkdir("demo_folder")
    print("Directory created")
else:
    print("Directory already exists")