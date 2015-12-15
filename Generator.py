#


def generator():
    yield 5
    yield 3
    yield 9
    yield 2
    yield 1

for x in generator():
    print(x)

#

from itertools import *

for x in combinations("ABC", 2):
    print(x)

for x in permutations("ABC", 2):
    print(x)

for x in repeat(3, 5):
    print(x)


