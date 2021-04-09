import sys

WEIGHT = 100


def weightOn(r, c):
    # Base case
    if r == 0:
        print(0.00)
        return WEIGHT
    else:
        weight = weightOn(r - 1, c - 1)
        print(weight)
        return weight + WEIGHT


def main():
    rowNum = sys.argv[1]
    weightOn(rowNum, 0)


if __name__ == "__main__":
    main()
