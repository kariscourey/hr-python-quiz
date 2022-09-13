# Create a Car class that has the required state of:

# make, a string
# model, a string
# year, an integer
# in that order.

# Create a __str__ method on the class that returns the year, make, and model separated by spaces.

# Example values:
#   make:  Oldsmobile
#   model: Alero
#   year:  2001

# __str__ would return "2001 Oldsmobile Alero"

# Put your class declaration here.
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # self, make, model, year are only accessible within __init__ because of scope

    # def __str__(self):  # if you try to turn one of these objects into a string (via print), will print return ____
    #     return f"{self.year} {self.make} {self.model}"
    #     # make is only available if used as a parameter or called through self.make

    def __len__(self):
        return len(self.make)


my_car = Car("Oldsmobile", "Alero", 2001)  # constructing a new instance of car; using positional paramaters (if car="Oldsmobile", using keywords)
second_car = Car("Toyota", "Sienna", 2015)

print(my_car)
print(second_car)
print(len(my_car))
print(len(second_car))

lst = Car([1,2,3,4], [1], [2])
print(len(lst))
