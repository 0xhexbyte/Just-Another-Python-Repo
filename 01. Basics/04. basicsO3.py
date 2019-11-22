import math
# NOT Operator
print("Let's Begin")
dream = "Millionaire Life"
print("Excuses" not in dream)

# Functions with numbers
print(round(2.9))
print(abs(-2.7))
# ceil function in math module is used to round the number to nearest value
print(math.ceil(2.2))

# Type Conversion
'''int(x)
   float(x)
   bool(x)
   str(x)
   print(type(x)) - to print type of a variable
'''
# Comparison Operators
# >, <, >=, <=, ==, !=
# ord("a") to print ASCII value of any character

# Conditional Statement
temp = 15
if temp == 15:
    print("Cold")
else:
    print("Hot")

# Ternary Operators:
age = 18
message = "Eligible" if age == 18 else "Not Eligible"
print(message)

# Logical Operators
# AND Operator
hi = True
bye = True
if hi and bye:
    print("Oye! Chak de phatte")
else:
    print("Lag gayi lottery!")

# OR Operator
hi2 = False
bye2 = False
if hi2 or bye2:
    print("Chak de phatte part 2")
else:
    print("Nahi ho payega")

# NOT Operator
rare = False
if not rare:
    print("Sasta hai re baba.")
else:
    print("Chalega")

# Chaining Comparison Operators
temp_age = 23
if 20 < temp_age < 25:
    print(f"Congrats you are {temp_age} years old.")
