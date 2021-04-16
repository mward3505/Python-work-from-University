from time import perf_counter
from hashmap import HashMap

COUNT = 0
CACHE = 0


def weight_on(r, c):
    global COUNT
    if r <= 0:
        return 0
    if c < 0 or c > r:
        return 0
    result = 0
    if c > 0:
        result += 100 + weight_on(r - 1, c - 1) / 2
    if c <= r - 1:
        result += 100 + weight_on(r - 1, c) / 2
    COUNT += 1
    return result


depth = 7

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
            CACHE += 1
            value = weight_on(i, j)
            myMap.set(tupleKey, value)
        line += "{:.2f}".format(value) + "\t"
    print(line)

stop = perf_counter()

print("Elapsed time:", stop-start, "seconds")
print("Number of function calls:", COUNT)
print("Number of cache hits:", CACHE)
