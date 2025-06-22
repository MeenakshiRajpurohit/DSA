def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j +1], array[j]
                swapped = True

        if not swapped:
            break

    return array

data = [3, 7, 5, 9, 1, 2]
sorted_data = bubble_sort(data.copy())
print("Sorted array:", sorted_data)

data1 = [1,2,3,4]
sorted_data1 = bubble_sort(data1.copy())
print("Sorted array:", sorted_data1)








