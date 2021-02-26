import random
import time


def timsort(arr):
    """Using built in timsort"""
    return sorted(arr)


def selection_sort(arr):
    """Doing a selection sort of a list of integers"""
    for i in range(len(arr)):
        if not str(arr[i]).isdigit():
            raise ValueError

    for i in range(len(arr)):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_num]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    return arr


def insertion_sort(arr):
    """Doing a insertion sort of a list of integers"""
    for i, val in enumerate(arr):
        if not str(arr[i]).isdigit():
            raise ValueError

    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergesort(arr):
    """Doing a merge sort of a list of integers"""
    for i in range(len(arr)):
        if not str(arr[i]).isdigit():
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


def quicksort(arr):
    """Doing a quick sort of a list of integers"""
    for i in range(len(arr)):
        if not str(arr[i]).isdigit():
            raise ValueError

    def quick_sort_hoare_helper(arr, first, last):
        """Helping quick sort"""
        if first < last:
            split_point = partition_h(arr, first, last)

            quick_sort_hoare_helper(arr, first, split_point - 1)
            quick_sort_hoare_helper(arr, split_point + 1, last)

    quick_sort_hoare_helper(arr, 0, len(arr) - 1)
    return arr


def partition_h(arr, first, last):
    """This is partitioning the quick sort helper"""
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
    """Verifying the list is a sorted list of integers"""
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


def main():
    """Printing out results to console for timin_numg of different sorts"""
    random.seed(time.time())

    my_list = random.sample(range(10000000), k=60)

    test = my_list.copy()
    print("starting selection_sort")
    time_start = time.perf_counter()
    sorted_test = selection_sort(test)
    time_end = time.perf_counter()
    print("selection_sort duration: %.6f" % (time_end - time_start))
    print("sorted: ", is_sorted(sorted_test), "\n")

    print("starting insertion_sort")
    time_start = time.perf_counter()
    test = my_list.copy()
    sorted_test = insertion_sort(test)
    time_end = time.perf_counter()
    print("insertion_sort duration: %.6f" % (time_end - time_start))
    print("sorted: ", is_sorted(sorted_test), "\n")

    print("starting mergesort")
    time_start = time.perf_counter()
    test = my_list.copy()
    mergesort(test)
    time_end = time.perf_counter()
    print("mergesort duration: %.6f\n" % (time_end - time_start))

    print("starting quick_sort")
    time_start = time.perf_counter()
    test = my_list.copy()
    quicksort(test)
    time_end = time.perf_counter()
    print("quick_sort duration: %.6f\n" % (time_end - time_start))

    print("starting timsort")
    time_start = time.perf_counter()
    test = my_list.copy()
    timsort(test)
    time_end = time.perf_counter()
    print("timsort duration: %.6f\n" % (time_end - time_start))


if __name__ == "__main__":
    main()
