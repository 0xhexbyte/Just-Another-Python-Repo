def fizz_buzz(input):
    if input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    elif input % 5 == 0 and input % 3 == 0:
        print("FizzBuzz")
    else:
        print(input)


fizz_buzz(15)
