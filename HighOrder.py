# High Order Function
def ajax(callback, values):
    result = []
    for e in values:
        result.append(callback(e))

    return result

print(ajax(lambda x: x + "1", ["1", "2", "3", "4", "5"]))  # (str) -> str
print(ajax(lambda x: x + 1, [1, 2, 3, 4, 5]))              # (int) -> int

# Filter
even = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])        # even
print("%s" % list(even))
