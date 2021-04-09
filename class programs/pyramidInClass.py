import time
WEIGHT = 200
cache = {}


def weightOn(r, c):
    if (r, c) in cache:
        return cache[(r, c)]

    if r == 0:
        result = 0
    elif c == 0:
        result = (WEIGHT + weightOn(r-1, c))/2.0
    elif c == r:
        result = (WEIGHT + weightOn(r-1, c-1))/2.0
    else:
        result = (WEIGHT + weightOn(r-1, c-1) + weightOn(r-1, c))/2.0

    cache[(r, c)] = result
    return result


def main():
    rows = int(input("Enter the number of rows: "))
    print()

    start = time.perf_counter()

    for row in range(rows):
        for col in range(row + 1):
            print(f'{weightOn(row, col):.2f}', end = " ")
        print()

    stop = time .perf_counter()
    print("Elapsed time: ", stop-start," seconds")


if __name__ == "__main__":
    main()