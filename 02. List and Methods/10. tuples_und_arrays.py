# We can define tuples either by placing them in curly brackkets or by just writing the items to be placed, separated by commas.
from array import array
lullaby = 1, 2, 3
print(type(lullaby))
print(lullaby)

# Tuple Addition
lullaby1 = (1, 2)+(3, 4)
print(lullaby1)

# Tuple Multiplication
lullaby2 = (1, 2)*4
print(lullaby2)

wire_type = ["Good", "Bery Good", "Bery Bery Good"]

# Changing list into tuple
wire_tuple = tuple(wire_type)
print(wire_tuple)

print(lullaby[0:2])
if 3 in lullaby:
    print("Hai na re baba")

# Arrays
gun = array("i", [1, 2, 3])
print(gun)
gun.append(5)
print(gun)
gun.insert(3, 6)        # Inserts 6 before 3rd indexed item
print(gun)
gun.pop()               # Pops out the last item
print(gun)
gun.remove(1)           # Removes the first occurence of that ite
print(gun)
