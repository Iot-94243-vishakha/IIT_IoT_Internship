def Greet(name,msg="Good Morning"):
    print(msg,name)
Greet("Vishakha")
Greet("Taehyung","Annyeong")
Greet("Jungkook","Joeun ohu-imnida")


def student(name, age, course):
    print(name, age, course)
student(age=22,name="Vishakha", course="Python")


def add(a, b):#function
    return a + b
def operate(a, b, func):#operate function
    return func(a, b)
result = operate(10, 5, add)#function calls
print("Result:", result)#output