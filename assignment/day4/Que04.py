"""Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For
example, histogram([4, 9, 7]) """

def histogram(a):
    s="*"
    return s*a 

def histogram(b):
    s="*"
    return s*b

def histogram(c=0):
    s="*"
    return  s*c

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

print("a=",histogram(a))
print("b=",histogram(b))
print("c=",histogram(c))