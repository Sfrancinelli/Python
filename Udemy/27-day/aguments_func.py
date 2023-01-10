def add(*args):
    print(args[3])
    total = 0
    for n in args:
        total += n
    return total

print(add(30, 20, 10, 5, 5, 5, 5))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    try:
        n += kwargs["add"]
    except:
        pass
    try:
        n *= kwargs["multiply"]
    except:
        pass
    try:
        n -= kwargs["cut"]
    except:
        pass
    try:
        n /= kwargs["divide"]
    except:
        pass
    return n


print(calculate(2, add=3, multiply=5))

# To avoid all this Try except thing to avoid errors, we use te method
# "get("key")" just as we would use the brackets nomenclature: kw["key"]
# The get method wont throw an error if there's no key or no value. It will
# Return "none" :)
# ej:

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)
print(my_car.make)