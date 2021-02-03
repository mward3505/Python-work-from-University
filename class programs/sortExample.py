def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
               min = j
        arr[i], arr[min] = arr[min], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

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


arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]
bubble_sort(arr)

print("Bubble Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]

selection_sort(arr)

print("Selection Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]

insertion_sort(arr)

print("Insertion Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]

shell_sort(arr)

print("Shell Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

arr = [3, 9, 2, 6, 5, 7, 1, 8, 4]

merge_sort(arr)

print("Merge Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
