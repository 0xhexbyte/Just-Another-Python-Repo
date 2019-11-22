# For longer comments of messages we can use:
msg = """Hey
This is a
very long
message, 
you see?
"""
print(msg)
print(len(msg))
print(" ")
print(msg[0:11])

# Escape Character
print("Python \"Programming\"")


def earning(value, by=2):
    return value*by


achieved = earning(1000, 5)
print(achieved)
