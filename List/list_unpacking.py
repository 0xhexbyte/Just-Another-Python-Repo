swift_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(swift_list)
sasta_rasta = ["a", "b", "c", "d", "e", ]
# we can assign individual list items to variables as such:
# var1 = swift_list[1]
# var2 = swift_list[2]
# var3 = swift_list[3]
# or we can also do this as:
first, second, third, four, five = sasta_rasta  # this is called list unpacking
# or if we want just the first and second, we can do the following:
f1, f2, *extras = swift_list
print(f1)
print(extras)
# also, if we wish to put the last item in a variable, we can do it as:
initial, *others, last = swift_list
print(last)
print(*others)
