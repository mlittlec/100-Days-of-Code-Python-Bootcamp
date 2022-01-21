def add(*args):
     sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    
    n += kwargs["add"]
    n += kwargs["multiply"]


calculate(2, add=3, multiply=5)

class Car:
  
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model";
                        
my_car = Car(make="Ford")
print(my_car.model)

