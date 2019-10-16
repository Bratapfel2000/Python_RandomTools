d1 = ["a", "b", "c", "d","e"]
d2 = ["x", "y", "c"]

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

diff = subtract(d1, d2)

for word in diff:
    print(word, end=' ')
