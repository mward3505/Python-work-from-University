import math
import random
import time


def linear_search(lyst, target):
    for i in range(len(lyst)):
        if lyst[i] == target:
            return i
    return -1


def binary_search(lyst, target):
    if len(lyst) == 0:
        return False

    midpoint = len(lyst) // 2

    if lyst[midpoint] == target:
        return True
    else:
        if lyst[midpoint] < target:
            return binary_search(lyst[:midpoint], target)
        elif lyst[midpoint] > target:
            return binary_search(lyst[midpoint + 1:], target)


def jump_search(lyst, target):
    n = len(lyst)
    step = math.sqrt(n)

    prev = 0
    while lyst[int(min(step, n) - 1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            pass

    while lyst[int(prev)] < target:
        prev += 1

        if prev == min(step, n):
            pass

    if lyst[int(prev)] == target:
        return prev


def main():
    random.seed(time.time())

    my_list = random.sample(range(1000000), k=1000)
    my_list.sort()

    time_start = time.perf_counter()

    result = linear_search(my_list, my_list[0])

    time_end = time.perf_counter()

    print("Beginning Search = %s, took %0.8f" % (result, time_end-time_start))

    time_start = time.perf_counter()

    result = linear_search(my_list, my_list[len(my_list)//2])

    time_end = time.perf_counter()

    print("Middle Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = linear_search(my_list, my_list[-1])

    time_end = time.perf_counter()

    print("End Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = binary_search(my_list, my_list[0])

    time_end = time.perf_counter()

    print("Beginning Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = binary_search(my_list, my_list[len(my_list) // 2])

    time_end = time.perf_counter()

    print("Middle Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = binary_search(my_list, my_list[-1])

    time_end = time.perf_counter()

    print("End Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = jump_search(my_list, my_list[0])

    time_end = time.perf_counter()

    print("Beginning Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = jump_search(my_list, my_list[len(my_list) // 2])

    time_end = time.perf_counter()

    print("Middle Search = %s, took %0.8f" % (result, time_end - time_start))

    time_start = time.perf_counter()

    result = jump_search(my_list, my_list[-1])

    time_end = time.perf_counter()

    print("End Search = %s, took %0.8f" % (result, time_end - time_start))


main()
