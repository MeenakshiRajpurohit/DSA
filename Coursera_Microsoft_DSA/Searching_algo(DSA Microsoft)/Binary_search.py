def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return None

result = binary_search([1, 3, 5, 7], 5)
if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found")




