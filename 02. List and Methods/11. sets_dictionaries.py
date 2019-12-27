# Sets are defined in curly braces and are a collection of items without any duplicates
numb = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6]
uniq = set(numb)
print(uniq)

elpha = {1, 2, 3, 4, 4}
elpha.add(4)
print(elpha)
elpha.remove(1)
print(elpha)
# elpha.clear()
# Removes all items from a set

first = {5, 3}
second = {3, 8}

# Union of Sets:
print(first | second)
# Intersection of Sets:
print(first & second)
# Difference of Sets:
print(first - second)
# Semantic Difference:
print(first ^ second)

# Items of a set are not in sequence, hence, we can't access them using indexing.

# Dictonaries:
# Are always in a key:value pair.

# oxphurd={"x":1,"y":2}
# -----OR-----
oxphurd = dict(x=1, y=2)
# Key of any entry is used as its indexing value.
oxphurd["x"] = 10
print(oxphurd)
oxphurd["y"] = 20
'''
if a in oxphurd:
    print("Found you!")
'''
# -----OR-----
print(oxphurd.get("a"))

# To delete particular entry, enter it's key value in place of x:
del oxphurd["x"]
print(oxphurd)

# Iterating over dictionaries:
for key in oxphurd:
    print(key, oxphurd[key])
# -----OR-----
for key, value in oxphurd.items():
    print(key, value)
