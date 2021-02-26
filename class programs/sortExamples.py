import random
import time


def timsort(x):
    return sorted(x)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    for i in range(len(arr)):
        if not arr[i].isdigit():
            raise ValueError

    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        if not arr[i].isdigit():
            raise ValueError

    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for startPosition in range(sublist_count):
            insertion_sort_gap(arr, startPosition, sublist_count)
        sublist_count = sublist_count // 2


def insertion_sort_gap(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        key = arr[i]
        j = i

        while j >= gap and key < arr[j - gap]:
            arr[j] = arr[j - gap]
            j = j - gap

        arr[j] = key


def mergesort(arr):
    for i in range(len(arr)):
        if not arr[i].isdigit():
            raise ValueError

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        left_index = 0
        right_index = 0
        new_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                arr[new_index] = left_half[left_index]
                left_index += 1
            else:
                arr[new_index] = right_half[right_index]
                right_index += 1
            new_index += 1

        while left_index < len(left_half):
            arr[new_index] = left_half[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right_half):
            arr[new_index] = right_half[right_index]
            right_index += 1
            new_index += 1
    return arr


def quick_sort_lamuto(arr):
    quick_sort_l_helper(arr, 0, len(arr))


def quick_sort_l_helper(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quick_sort_l_helper(arr, low, index - 1)
        quick_sort_l_helper(arr, index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low

    for j in range(i + 1, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[low], arr[i] = arr[i], arr[low]
    return i


def quicksort(arr):
    for i in range(len(arr)):
        if not arr[i].isdigit():
            raise ValueError

    def quick_sort_hoare_helper(arr, first, last):
        if first < last:
            split_point = partition_h(arr, first, last)

            quick_sort_hoare_helper(arr, first, split_point - 1)
            quick_sort_hoare_helper(arr, split_point + 1, last)

    quick_sort_hoare_helper(arr, 0, len(arr) - 1)
    return arr


def partition_h(arr, first, last):
    pivot = arr[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and arr[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]

    arr[first], arr[right_mark] = arr[right_mark], arr[first]

    return right_mark


def is_sorted(my_list):
    for i in range(len(my_list)):
        if not str(my_list[i]).isdigit():
            raise ValueError

    flag = True
    i = 1
    while i < len(my_list):
        if my_list[i] < my_list[i - 1]:
            flag = False
        i += 1
    return flag


# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
# bubble_sort(arr)
#
# print("Bubble Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
#
# selection_sort(arr)
#
# print("Selection Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
#
# insertion_sort(arr)
#
# print("Insertion Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
#
# shell_sort(arr)
#
# print("Shell Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
#
# mergesort(arr)
#
# print("Merge Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
# arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
#
# quick_sort_lamuto(arr)
#
# print("Quick Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])


def main():
    random.seed(time.time())

    MY_LIST = random.sample(range(10000000), k=60)
    test = MY_LIST.copy()
    print("starting selection_sort")
    time_start = time.perf_counter()
    sorted_test = selection_sort(test)
    time_end = time.perf_counter()
    print("selection_sort duration: %.6f" % (time_end - time_start))
    print("sorted: ", is_sorted(sorted_test), "\n")

    print("starting insertion_sort")
    time_start = time.perf_counter()
    test = MY_LIST.copy()
    sorted_test = insertion_sort(test)
    time_end = time.perf_counter()
    print("insertion_sort duration: %.6f" % (time_end - time_start))
    print("sorted: ", is_sorted(sorted_test), "\n")

    print("starting mergesort")
    time_start = time.perf_counter()
    test = MY_LIST.copy()
    mergesort(test)
    time_end = time.perf_counter()
    print("mergesort duration: %.6f\n" % (time_end - time_start))

    print("starting quick_sort")
    time_start = time.perf_counter()
    test = MY_LIST.copy()
    quicksort(test)
    time_end = time.perf_counter()
    print("quick_sort duration: %.6f\n" % (time_end - time_start))

    print("starting timsort")
    time_start = time.perf_counter()
    test = MY_LIST.copy()
    timsort(test)
    time_end = time.perf_counter()
    print("timsort duration: %.6f\n" % (time_end - time_start))


if __name__ == "__main__":
    main()
