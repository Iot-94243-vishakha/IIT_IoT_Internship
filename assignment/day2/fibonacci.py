num=int(input("enter number:"))
k=0
i=1
j=0
for j in range(num):
    print(k)
    a=k
    k=i+k
    i=a
    j+=1
    #a=0,b=1,0+1=1+1=2+1=3+2=5+3=8
