def bakula(ehh):
    if ehh <= 2:
        raise ValueError("Can't be less than $2 mil.")
    return (print(f"Awesomazing, you have a salary of ${ehh} millions."))


inc_stream = int(input("Income? :"))
try:
    bakula(inc_stream)
except ValueError:
    print("Gotta work more, my man!")