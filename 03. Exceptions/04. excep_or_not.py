# Lets take a look at the downside of raising exceptions

from timeit import timeit  # to find out the time of execution of our code

exec_time = """
def raise_something(thing):
    if len(thing) <= 10:
        raise ValueError("Nehh")
    else:
        print("Nothing to raise -,-")


something = "wudaheck"
try:
    raise_something(something)
except ValueError:
    print("EXCEPTION: Length of the input is not greater than 10.")
"""
print("First Execution=", timeit(exec_time, number=100))
