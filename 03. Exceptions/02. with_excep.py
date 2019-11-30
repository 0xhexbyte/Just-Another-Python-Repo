try:
    with open("excep_sample.txt") as moifile:
        print("File is currently opened.")
    # All the work we need to do with this file can be done in this 'with' block.
    # "with" statement is used to automatically release external resources, hence in this case, as the control leaves the 'with' block,
    # python will automatically close the file.
        print("Closing the file, tadaa !")
except ValueError:
    print("Only numeric, not alpha. 8)")
except ZeroDivisionError:
    print("Cannot be divided by zero. xP")
else:
    print("No exception.")

# Context Management Protocol
# If an object has Content Management Protocol enabled, we can use the '__enter__' and '__exit__' methods on them.

try:
    with open("excep_sample.txt") as moifile, open("conquer_the_world.txt") as conq_wor:  # to open multiple files
        print("File is currently opened.")
        print("Closing the file, tadaa !")
except ValueError:
    print("Only numeric, not alpha. 8)")
except ZeroDivisionError:
    print("Cannot be divided by zero. xP")
else:
    print("No exception.")
