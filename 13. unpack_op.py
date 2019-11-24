# Unpacking Operator : We use this operator when we just need to get individual elements out instead of other things, example:
nums = [1, 2, 3, 4, 5]
print(nums)

nums2 = [1, 2, 3, 4, 5, 6]
print(*nums2)  # by placing an asterik

van = [*range(5), *"Hello"]
print(van)

# Unpacking dictionaires is a little different:
first = {"x": 1}
second = {"x": 10, "y": 2}

# Here we get 2 values of x, so the last unpacked value is stored.

comb = {**first, **second, "z": 1}
print(comb)
