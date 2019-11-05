def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        print("FizzBuzz")
    elif input % 5 == 0:
        print("Buzz")
    elif input % 3 == 0:
        print("Fizz")
    else:
        print(input)


fizz_buzz(7)
