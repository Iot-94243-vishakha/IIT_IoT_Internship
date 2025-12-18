# Conversion functions
def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inches):
    return inches * 2.54


# Higher-order function
def distance_converter(distance, conversion_type, conversion_function):#takes distance value,takes conversion types,takes conversion function
    result = conversion_function(distance)#calls given conversion
    print(f"{distance} {conversion_type.split(' to ')[0]} = {result} {conversion_type.split(' to ')[1]}")


# Taking input from user
distance = float(input("Enter distance value: "))

print("\nConversions:")
distance_converter(distance, "km to m", km_to_m)#calls distance converter,same input value different conversion
distance_converter(distance, "m to cm", m_to_cm)#calls distance converter
distance_converter(distance, "cm to mm", cm_to_mm)#calls distance converter
distance_converter(distance, "feet to inches", feet_to_inches)#calls distance converter
distance_converter(distance, "inches to cm", inches_to_cm)#calls distance converter
