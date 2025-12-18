def is_prime(num):#function to check prime number
    if num <= 1:#less than or equal to 1 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):#loopstartfrom2 and goes square root of number
        if num % i == 0:#number divisible by any number then false
            return False
    return True
start = int(input("Enter start of range:"))#input
end = int(input("Enter end of range: "))#input
print("Prime numbers is given range:")
for n in range(start, end + 1):#loop runs through each number in range
    if is_prime(n):
        print(n, end="")#returns true,number printed

