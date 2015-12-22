class Person:

    # Constructor
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    # Method
    def full_name(self):
        return self.first + " " + self.last

# Create an instance of Person
david = Person("David", "Fox", 23)

print("My first name is %s" % david.first)
print("My full name is %s" % david.full_name())












