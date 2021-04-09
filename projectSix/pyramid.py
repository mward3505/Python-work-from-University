from time import perf_counter
from hashmap import HashMap


def weight_on(r,c):
    if r <= 0:
        return 0
    if c < 0 or c > r:
        return 0
    result = 0
    if c > 0:
        result += 100 + weight_on(r - 1, c - 1) / 2
    if c <= r - 1:
        result += 100 + weight_on(r - 1, c) / 2
    return result


depth = 22

start = perf_counter()
myMap = HashMap()
for i in range(depth):
    line = ""
    for j in range(i + 1):
        value = 0
        tupleKey = (i, j)
        try:
            value = myMap.get(tupleKey)
        except:
            value = weight_on(i, j)
            myMap.set(tupleKey, value)
        line += "{:.2f}".format(value) + "\t"
    print(line)