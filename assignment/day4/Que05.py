# List of lambda functions for weight conversion
conversions = [
    lambda t: t * 1000,             # tons to kilograms
    lambda kg: kg * 1000,            # kilograms to grams
    lambda g: g * 1000,              # grams to milligrams
    lambda mg: mg / 453592.37        # milligrams to pounds
]

# Input from user (in tons)
tons = float(input("Enter weight in tons: "))

# Applying conversions step by step
kg = conversions[0](tons)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

# Printing results
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")







"""Create a list of lambda functions that converts from tonns to kilograms, kilograms to grams, grams to
milligrams, and milligrams to pounds. Input a weight from user in tonns and print it in remaining all
units. E.g. if user inputs 0.002 tonns, then output should be 2 kg, 2000gm, 2000000 mg, and
4.409245244 lbs"""

'''tkc=lambda n:n*1000
kgc=lambda n:n*1000
gmc= lambda n:n*1000
mpc=lambda n:n*1

n=float(input("Enter number for convertion: "))

print("convertion=",tkc(n),"kg")
print("convertion=",kgc(n)*10**3,"gm")
print("convertion=",gmc(n)*10**6,"mg")
print("convertion=",mpc(n)*2000,"lbs")'''


"""
# Lambda functions
ton_to_kg = lambda t: t * 1000
kg_to_g = lambda kg: kg * 1000
g_to_mg = lambda g: g * 1000
mg_to_lb = lambda mg: mg * 0.00000220462

weight = float(input("Enter weight in tonns: "))

kg = ton_to_kg(weight)
g = kg_to_g(kg)
mg = g_to_mg(g)
lb = mg_to_lb(mg)

print("Kilograms:", kg)
print("Grams:", g)
print("Milligrams:", mg)
print("Pounds:", lb)
"""