# FOR Loops
for i in range(5):
    print("Oxfords not brogues")

for num in range(3):
    print("Hehe", num+1, (num+1)*".")

for num in range(1, 10, 2):
    print("'t works.")

# For Else
success = False
for num in range(3):
    print("Keep it comin'")
    if success:
        print("Voot voot")
else:
    print("Not happenin'")

# Only for value of 'success' variable to be true, the for block will complete it's execution. The else block will be executed only if
# the for block will not completely get executed, which can be checked by changing the value of variable 'success' to True.

# Nested Loops
for x in range(5):
    for y in range(5):
        print(x, y)

# Something informative
print(type(range(5)))

# Iterables
for x in 'Python':
    print(x)
for x in [1, 2, 3, 4]:
    print(x)

# While Loop
i = 1
while i <= 5:
    print("VIP Parking, re dada", i)
    i = i+1
