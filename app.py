def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1

        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [78, 56, 43, 32, 3, 4,5]
sorted_data = merge_sort(data)
print("sorted array:", sorted_data)






