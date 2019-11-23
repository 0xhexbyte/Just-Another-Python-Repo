# A very simple list
simple_list = ["Watch Dogs 2", "Just Cause 3", "CSGO", "Hacknet"]
print(simple_list)

# Every item in the next list, is a list (a matrix)
career = [["success", "hardwork"], ["dedication", "persistence"]]
print(career)

# To repeat items in a list, when we wish to create a list of same items
sample = ["nothing"] * 5
print(sample)

# Concatenating lists
combined = sample + simple_list
print(combined)

# We can also pass iterables into a function called list() to make a list of them
new_list = list(range(10))
print(new_list)

char_list = list("Hummer da best")
print(char_list)
print(type(char_list))
print(len(char_list))
