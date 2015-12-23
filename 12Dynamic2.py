class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last


# Return a full name
def full_name(self):
    return self.first + " " + self.last

# Add the method dynamically.
Person.get_full_name = full_name

david = Person("David", "Jones")

print(david.get_full_name())


# Decorate it
def wrap(f):
    def new_method(self):
        return "I am " + f(self) + "."
    return new_method

Person.get_full_name = wrap(Person.get_full_name)

print(david.get_full_name())
