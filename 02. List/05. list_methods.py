# defining a random list:
crocery = ['mig29', 'monster', 'dirt-bike', 'harley-davidson']
'''
Everything in python is an object, so, if 
we can use dot notation to access individual 
functions or methods on that object.
'''
# to add items to the end of a list:
crocery.append('baby-boi')
print(crocery)

# to add an item at a specific position:
crocery.insert(0, 'winner')
print(crocery)

# to remove an item at the end of the list:
crocery.pop()
print(crocery)

# to remove an item at a specific index
crocery.pop(2)
print(crocery)

# if we don't know index of the item we wish to remove:
crocery.remove('dirt-bike')
# this will remove the first appearance of the parameter passed, so if we have multiple strings with same value,
# it'll delete the first instance
print(crocery)

crocery.append('useless')
crocery.append('items')
crocery.append('foor')
crocery.append('myy')
crocery.append('listt')
print(crocery)

# if we want to delete a range of items:
del crocery[0:2]
print(crocery)

# if we wish to remove all the items from the list, use clear()
# crocery.clear() -- obviously not gonna use this one xD
