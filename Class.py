class Person:
    first = ""
    last = ""
    age = 0

    # Constructor
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    # Method
    def full_name(self):
        return "My name is {} {}".format(self.first, self.last)

david = Person("David", "Fox", 23)
print(david.full_name())


def how_old_are_you(self):
    return self.age

Person.getAge = how_old_are_you
print(david.getAge())













