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


start = perf_counter()

depth = 7
f = open("part2.txt", "w")
for row in range(depth):
    for col in range(row + 1):
        f.write(f'{weight_on(row, col):.2f}')
    f.write("\n")

stop = perf_counter()


f.write("\nElapsed time: " + str(stop-start) + " seconds")
f.close()

COUNT = 0

start = perf_counter()
myMap = HashMap()
e = open("part3.txt", "w")
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
    e.write(line)
    e.write("\n")

stop = perf_counter()

e.write("\nElapsed time: " + str(stop-start) + " seconds\n")
e.write("Number of function calls: " + str(COUNT) + "\n")
e.write("Number of cache hits: " + str(CACHE) + "\n")

e.close()
