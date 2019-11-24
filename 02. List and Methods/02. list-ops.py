# Items in a list can be accessed individually through indexing, beginning from 0
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list[1])
print(num_list[-1])

# To change a particular item in a list
num_list[3] = "changed"

# To slice a list and get the required items
print(num_list[0:5])

# To print items at a specific interval from a list
print(num_list[::2])

# To print a list in reverse order
print(num_list[::-1])
