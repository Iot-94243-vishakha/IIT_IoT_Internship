
#num=(input("enter 5 numbers:"))
#a=str(len(num))
#print("length of numbers is:",a)
#if a!=reversed(num):
 #   print("number is not palindrome")
#else:
 #  print("number is palindrome")

num = (input("Enter number: "))
i=len(num)
print("length of num=",i)
k=0
m=int(num)
y=int(num)

while y > 0:
    j=y%10
    k=k*10+j
    y//=10

if m==k:
    print("Palindrome",m)
else:
    print("Not Palindrome",m)
