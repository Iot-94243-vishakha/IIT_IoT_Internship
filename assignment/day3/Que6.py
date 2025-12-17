def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b


def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)



print(calculate(10, 5, add))
print(calculate(10, 5, subtract))
print(calculate(10, 5, multiply))
print(calculate(10, 5, divide))
print(calculate(10, 0, divide))