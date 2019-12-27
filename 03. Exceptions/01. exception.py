# Exception Handling

try:
    age = int(input("Age:"))
except ValueError:
    print("Age is numeric, dumbo!")
else:
    print("No exception.")

# Run this code twice while entering first value as a valid numeric and second as an invalid character.
# Notice, when we enter a valid number, the "else" part also get's executed whereas in the latter, it doesn't.
# This happens because the control jumps out of the try-catch block if we enter an invalid input, eg: 'a'.

# We can handle multiple error types by specifying different except blocks:

try:
    x = int(input("Enter value of x: "))
    intended_error = 1/x
    print(intended_error)
except ValueError:
    print("Only numeric, no character or alpha. 8)")
except ZeroDivisionError:
    print("Cannot be divided by zero. xP")
else:
    print("No exception.")

# In cases where we need to close certain processes, we use the 'finally' keyword.

try:
    # Opening a sample file
    sample = open("excep_sample.txt")
    y = int(input("Enter value of y: "))
    intended_error_call = 1/y
    print(intended_error_call)
    # sample.close()                              # Closing the sample file
except ValueError:
    print("Only numeric, no characters or alpha. 8)")
    # sample.close()
except ZeroDivisionError:
    print("Cannot be divided by zero. xP")
else:
    print("No exception.")
finally:
    sample.close()

# In above example we opened a file, now if we place the .close() method in the try block and an exception arises, then the close() method will
# not be called, if we place it in except clause and if no exception gets called then also it won't be called and placing the close function
# in multiple places creates duplicacy, which is not good practice. So here we introduce a new keyword called "finally" and this block gets
# executed, no matter what.
