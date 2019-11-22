def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# Scope of variables (Suggestion: Avoid using global variables)
msg = "wut?!?!?!"


def doubt(que):
    global msg
    msg = "wuuut?"


# In here, if we don't define the 'msg' variable declared in the function 'doubt' as global,
# then we'll have the initial value of variable 'msg'.
doubt("hehe")
print(msg)
