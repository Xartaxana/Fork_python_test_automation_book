def bubble_sort_asc(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def bubble_sort_desc(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def bubble_sort_with_stop(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break

arr = [39, 12, 18, 85, 72, 10, 2, 18]
arr2 = [39, 12, 18, 85, 72, 10, 2, 18]
arr3 = [10, 2, 12, 18, 18, 39, 72, 85]
print("Unsorted array:")
print(arr)
bubble_sort_asc(arr)
print("Sorted array in ascending order:")
print(arr)

bubble_sort_desc(arr2)
print("Sorted array in descending order:")
print(arr2)

bubble_sort_with_stop(arr3)
print(arr3)