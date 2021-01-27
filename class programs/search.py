import math


def seq_search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(x, nums):
    if len(nums) == 0:
        return False

    midpoint = len(nums) // 2

    if nums[midpoint] == x:
        return True
    else:
        if x < nums[midpoint]:
            return binary_search(x, nums[:midpoint])
        elif x > nums[midpoint]:
            return binary_search(x, nums[midpoint + 1:])


def jump_search(x, nums):
    n = len(nums)
    step = math.sqrt(n)

    prev = 0
    while nums[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            pass

    while nums[int(prev)] < x:
        prev += 1

        if prev == min(step, n):
            pass

    if nums[int(prev)] == x:
        return prev


myArray = [1, 2, 3, 5, 8, 13, 21, 34]
print(jump_search(21, myArray))
