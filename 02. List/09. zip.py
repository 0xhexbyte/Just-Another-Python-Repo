# If we wish to combine 2 or more lists in a list of tuples with items at same index positions clubbed together, we use zip:

list1 = [1, 3, 4, 7, 9, 76, 23]
list2 = [5, 8, 13, 52, 34, ""]

print(list(zip(list1, list2)))
