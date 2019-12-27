# Dictionary Comprehension
# Example:
from sys import getsizeof
print('Dictionary Comprehension')
swift = {}
for x in range(10):
    swift[x] = x*2

print(swift)
# Same code can be written as:

swiftx = {x: x*2 for x in range(10)}
print(swiftx)

# Generator Expressions:
# Generator obj. are iterable and in each iteration, they generate a new value.
# They do not store all values like a list but generate a value in each iteration, for example:

genx = (x*2 for x in range(10))
print(genx)
for x in genx:
    print(x)

# To get size of the objects created here, we need to import the getsizeof function from sys module.
#from sys import getsizeof

geny = (x*2 for x in range(100000))
print("Generator:", getsizeof(geny))

lisst = [x*2 for x in range(100000)]
print("List:", getsizeof(lisst))

# Also, doing print(len(geny)) will give us a TypeError since the generator object is not storing anything but generating stuff in iterations.
