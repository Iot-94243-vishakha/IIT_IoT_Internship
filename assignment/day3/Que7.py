def factorial(n):#def function
    if n == 0 or n == 1:#stopping condition prevents infinite recursion
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 19:", factorial(19))
print("Factorial of 22:", factorial(22))
print("Factorial of 59:", factorial(59))
print("Factorial of 45:", factorial(45))
print("Factorial of 50:", factorial(50))
print("Factorial of 10:", factorial(10))
print("Factorial of 1:", factorial(1))


def power(base, exp):#def function
    if exp == 0:#stopping condition , prevents infinte recursion
        return 1
    return base * power(base, exp - 1)#recursive call

print("2 raised to power 4:", power(2, 4))
print("2 raised to power 24:", power(2, 24))
print("2 raised to power 100:", power(2, 100))
print("2 raised to power 12:", power(2, 12))
print("2 raised to power 98:", power(2, 98))
print("2 raised to power 43:", power(2, 43))
print("2 raised to power 45:", power(2, 45))
print("2 raised to power 65:", power(2, 65))
print("2 raised to power 9:", power(2, 9))