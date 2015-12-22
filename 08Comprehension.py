# [0, 1, 2, 3, 4] -> [0, 1, 4, 9, 16]
print([x**2 for x in range(5)])

# [0, 1, 2, 3, 4] -> [0, 2, 4] -> [0, 4, 16]
print([x**2 for x in range(5) if x % 2 == 0])


# using map and lambda
print(list(map(lambda x: x**2, range(5))))



