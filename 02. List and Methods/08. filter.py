# Filter Function
filterit = [
    ('SRT', 3),
    ('H1', 1),
    ('BC', 2),
    ('Inti', 4)
]

# We use filter() when we want to filter the items in a list on the basis of some criteria.

xc = filter(lambda item: item[1] >= 2, filterit)
print(type(xc))
print(xc)

# filter() returns a 'filter object' which is an iterable and can be converted into list using list().

xf = list(filter(lambda item: item[1] >= 2, filterit))
print(xf)

# List Comprehension:
# Syntax for a comprehension is:  [expression for item in items]

x1 = [item[1] for item in filterit]
print(x1)

# We can re-write the function on line 17 as:
y = [item for item in filterit if item[1] >= 2]
print(y)
