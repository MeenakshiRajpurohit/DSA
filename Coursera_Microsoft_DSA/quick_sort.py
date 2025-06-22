def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


data = [10,50,20,40,56,23,21]
sorted_data = quick_sort(data)
print("Sorted array:", sorted_data)

data1 = [1]
sorted_data1 = quick_sort(data1)
print(sorted_data1)






