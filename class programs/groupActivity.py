import math


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False


def binary_search(arr, x):
    mid = 0
    start = 0
    end = len(arr)
    step = 0

    while start <= end:
        step = step + 1
    mid = (start + end) // 2

    if x == arr[mid]:
        return True

    if x < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return False


def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
    step += math.sqrt(n)
    if prev >= n:
        return False

    while arr[int(prev)] < x:
        prev += 1

    if prev == min(step, n):
        return False

    if arr[int(prev)] == x:
        return prev

    return False
