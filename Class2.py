class Person:
    first = ""
    last = ""


# Return a full name
def full_name(self):
    return self.first + " " + self.last

# Add the method
Person.get_full_name = full_name


david = Person()
david.first = "David"
david.last = "Jones"

print(david.get_full_name())

Person.get_full_name = print

david.get_full_name("Hello")

print(dir(Person))


