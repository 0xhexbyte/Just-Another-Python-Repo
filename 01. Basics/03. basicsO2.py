one = "lets "
plus = "do "
two = "this"
full = one+plus+two
print(full)

# formatted strings - by using these we can put any valid expression between curly brackets.
full2 = f"{one} {two}"
print(full2)

print(one.upper())
print(one.isdigit())
# to strip any spaces in the variable value
print(one.strip())
# to replace certain string pattern from the string
full_new = full.replace("s", "a")
print(full_new)
# boolean return type, tells us about if the condition is true or false
print("do" in full)
