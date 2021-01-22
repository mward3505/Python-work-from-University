import time


def sum_02_wrapper(n):
    start = time.time()
    total = sum(range(n+1))
    end = time.time()

    return total, end - start


def sum_02(n):
    #return n + sum
    pass
