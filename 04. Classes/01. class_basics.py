# Classes are like blueprint of objects, with predefined porperties, ready to be used.
# Object: Instance of a class.

# All methods we define in a class need to have at least one parameter, 'self, by convention.
# self variable refers to the current class point object.


class Judy:
    uip_piu = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wut(self):
        print(f"Point {self.x} and {self.y}")

    def find(self):
        print('Found')


# Creating object of a class
# We can call multiple methods from an object by typing name of object followed by a dot operator, for example in this case:
# judy.  (That is not a full stop, but a dot operator.)
# This will bring a list of methods that can be applied.
judy = Judy(0, 1)
print(type(judy))
print(isinstance(judy, Judy))

# These default or pre-defined methods are often referred to as magic methods,
# there are several magic methods and one of them is '__init__'
# To supply initial/default values for any variable, we need to use constructors.
# '__init__' is called a magic method and is called automatically when the object is created.

judy.wut()

# Objects in python are dynamic just like in java so we can define them afterwards, like:
judy.z = 5
print(judy.z)
# One thing to note here is that these objects: x,y,z are instance attributes and not global.
# We can define class level attributes, like uip_piu
print(judy.uip_piu)
Judy.uip_piu = "blue"
print(judy.uip_piu)

# As we can see, specifically declaring the uip_piu variable of Judy class, overrides the
# value and this will happen for every object of that class because uip_piu is a class level variable.
