# func, any
def ajax(callback, list):
    result = []
    for e in list:
        result.append(callback(e))
    return result

print(ajax(lambda x: x + "1", ["1", "2", "3", "4", "5"]))  # (str) -> str
print(ajax(lambda x: x + 1, [1, 2, 3, 4, 5]))              # (int) -> int

