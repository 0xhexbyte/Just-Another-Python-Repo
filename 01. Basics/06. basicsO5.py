# Defining Functions
def dogs_unleashed():
    print("Who let the dogs out?!")


print("Opening door...")
print("Calling dogs_unleashed:")
dogs_unleashed()

# On a basic note, there are 2 types of functions: one which return a value, another one which performs a task


def hehe(name):
    return f"{name}"


pew = hehe("You")
print(pew)


# Keyword Arguements


def letsdothis(passion):
    print(f"Your passion is {passion}")
    #mission = passion+"hardwork"
    return(passion+"hardwork")
    # In the above statement, we can also return variable 'mission'


letsdothis("blew blue blew")
# the return value of the function defined above is saved in the variable 'keepgoing'
keepgoing = letsdothis("boom")
print(keepgoing)

# Default Parameters
# At times we just might wish to keep some parameters pre-defined, if we don't receive any input from the user so here is, how to do that:


def baby_default(intake, protein=5):
    print(f"Baby takes {intake} which has {protein}gms of protein.")


baby_default("milk")
# In the call below, the value of protein overwrites the default value
baby_default("protein milk", 20)
