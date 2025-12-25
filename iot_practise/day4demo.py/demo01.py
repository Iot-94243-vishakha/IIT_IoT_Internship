def function1():
    l1 = [
        [1,2,3,4],
        [10,20,30,40],
        [11,22,33,44]
    ]

    print("l1:")
    for l in l1:
        for e in l:
            print(e,end=" ")
        print("")

def function2():
    students = [
        [12,"abc",98.5],
        [10,"xyz",87.6],
        [13,"mno",90.0]
    ] 

    for rollno, name, marks in students:
        print(f"rollno = {rollno}, name = {name}, marks = {marks}")   

function2()         