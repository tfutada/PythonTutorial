def gen1():
    yield 5
    yield 3
    yield 9
    yield 2
    yield 1

# for in [5, 3, 9, 2, 1]
for x in gen1():
    print(x)

#

from itertools import *

for x in combinations("ABC", 2):
    print("C:", x)

# Ordered Combination
for x in permutations("ABC", 2):
    print("P:", x)

for x in repeat(3, 500):
    print(x)


