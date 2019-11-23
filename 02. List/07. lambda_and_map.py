catalog = [
    ('SRT', 3),
    ('H1', 1),
    ('BC', 2)
]


def sort_item(item):
    return item[1]


# To sort the tuple entries in list, based on the ranking - second param
catalog.sort(key=sort_item)
print(catalog)

# We use LAMBDA expression (one line anonymous function) to make the code cleaner
# Here we implement same function as above, but in much shorter way
# Syntax of a lambda function => sort(key=lambda parameter_list: expression)

print(catalog.sort(key=lambda item: item[1]))

# The map() function takes 2 parameters, a function and one or more iterables.
# It will apply the lambda function to each item of the list.

x = map(lambda item: item[1], catalog)
print(type(x))
print(x)
for x in x:
    print(x)

# 'map' object is another iterable so we can use list() function to iterate over it.
x = list(map(lambda item: item[1], catalog))
print(x)
