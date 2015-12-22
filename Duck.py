# Impl Class 1
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

class Computer:
    def __init__(self, brand):
        self.brand = brand


def what_your_name(you):
    print(you.full_name())  # dynamic typing

david = Person("David", "Jobs")
mac = Computer("Mac book air")

what_your_name(david)
what_your_name(mac)




