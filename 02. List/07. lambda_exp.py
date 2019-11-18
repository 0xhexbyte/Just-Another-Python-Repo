catalog = [
    ('SRT', 3),
    ('H1', 1),
    ('BC', 2)
]


def sort_item(item):
    return item[1]


# to sort the tuple entries in list, based on the ranking - second param
catalog.sort(key=sort_item)
print(catalog)

# we use LAMBDA expression (one line anonymous function) to make the code cleaner
# here we implement same function as above, but in much shorter way
# syntax of a lambda function => sort(key=lambda parameter_list: expression)

print(catalog.sort(key=lambda item: item[1]))
