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

# Change it.
Person.get_full_name = print

david.get_full_name("Hello")

