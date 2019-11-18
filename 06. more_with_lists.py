laptop = ['sleek', 'fast', 'good-looking', 'fame', 'shahpura']
# to find the index of an item in a list
print(laptop.index('fast'))

# print(laptop.index('wow'))
# this gives error, so we put it like this:
if 'wow' in laptop:
    print(laptop.index('wow'))
else:
    print('Hehehehehe')

# to print the number of occurences of a particular item in a list:
print(laptop.count('wow'))

# SORTING LISTS:

rand_nos = [1, 2, 21, 13, 97, 1987, 45]
print(type(rand_nos[3]))

# to sort numbers in ascending order
rand_nos.sort()
print(rand_nos)
# to sort numbers in reverse orders
rand_nos.sort(reverse=True)
print(rand_nos)

# we can also take any iterable annd pass it into sorted()
print(sorted(rand_nos))
# we can also use reverse param in order to reverse sort using sorted() function
print(sorted(rand_nos, reverse=True))
