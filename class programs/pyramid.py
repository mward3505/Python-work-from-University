import sys

weight = 200.00
cache = {}
person = (0, 0)

def weightOn(r, c):

    holdingWeight = 0.00
    cache.update({person: holdingWeight})

    if (r, c) == person:

        print(cache)
        return holdingWeight

    else:

        if r == 1:
            holdingWeight = (weight / (2 ** r))
            cache[1] = holdingWeight

        # holdingWeight = (weight / (2 ** r))

        # holdingWeight = (weight / (2 ** r)) + 100


def main():

    r = int(input("Please enter a row: "))
    c = int(input("Please enter the column: "))
    personPos = (r, c)

    weightOn(r, c)
    print(cache[personPos])


if __name__ == "__main__":
    main()