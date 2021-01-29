import math
import random
import time


def linear_search(lyst, target):
    for i in range(len(lyst)):
        if lyst[i] == target:
            return True
    return False


def binary_search(lyst, target):
    lyst.sort()
    low = 0
    high = len(lyst)-1

    while low <= high:

        midpoint = high + low // 2
        r = lyst[midpoint]
        if lyst[midpoint] < target:
            low = midpoint + 1
        elif lyst[midpoint] > target:
            high = midpoint - 1
        else:
            return True

    return False

    # if lyst[midpoint] == target:
    #     return True
    # else:
    #     if lyst[midpoint] > target:
    #         return binary_search(lyst[:midpoint], target)
    #     elif lyst[midpoint] < target:
    #         return binary_search(lyst[midpoint + 1:], target)


def jump_search(lyst, target):
    lyst.sort()
    length = len(lyst)
    step = math.sqrt(length)

    prev = 0
    while lyst[int(min(step, length) - 1)] < target:
        prev = step
        step += math.sqrt(length)
        if prev >= length:
            return False

    while lyst[int(prev)] < target:
        prev += 1

        if prev == min(step, length):
            return False

    if lyst[int(prev)] == target:
        return True


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


if __name__ == "__main__":
    main()
