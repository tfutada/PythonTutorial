
def to_upper(word):
    return str.upper(word)


def ajax(array, callback):
    result = []
    for w in array:
        ret = callback(w)
        result.append(ret)

    return result


val = ["abc", "def"]
print(ajax(val, to_upper))



