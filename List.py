#

# List
country = ["Japan", "Vietnam", "US", 5]

for val in country:
    print("Country: %s" % val)

#
person = {
    "David": 32,
    "Tom": 18,
    "Bob": 27,
}

adults = []
kids = []

# items() returns a list of tuples(k,v)
for k, v in person.items():
    if v > 20:
        adults.append(k)
    else:
        kids.append(k)

print("adults: %s" % adults)
print("kids: %s" % kids)







# Tuple

developers = {
    ("Tom", "Jones"): "Python",
    ("Tom", "Ford"): "Go",
}

print("Tom Ford knows %s" % developers[("Tom", "Ford")])

# Set

go = {"Compiler", "Duck Typing", "OOP"}
python = set(["Interpreter", "Duck Typing", "OOP"])

print("both of them have: %s" % go.intersection(python))
print("either of them have: %s" % go.symmetric_difference(python))





