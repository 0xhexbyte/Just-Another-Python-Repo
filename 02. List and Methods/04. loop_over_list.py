cars = ["Bugatti Veyron", "Bugatti Chiron",
        "Lamborghini Aventador", "Rolls Royce Phantom"]

for car in cars:
    print(car)

# enumerate() gives us a tuple
for car in enumerate(cars):
    print(car)

# tuple is like a list, except that it is read-only
