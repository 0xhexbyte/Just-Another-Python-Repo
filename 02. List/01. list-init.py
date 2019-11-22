# a very simple list
simple_list = ["Watch Dogs 2", "Just Cause 3", "CSGO", "Hacknet"]
print(simple_list)
# every item in the next list, is a list (a matrix)
career = [["success", "hardwork"], ["dedication", "persistence"]]
print(career)
# to repeat items in a list, when we wish to create a list of same items
sample = ["nothing"] * 5
print(sample)
# concatenating lists
combined = sample + simple_list
print(combined)
# we can also pass iterables into a function called list() to make a list of them
new_list = list(range(10))
print(new_list)
