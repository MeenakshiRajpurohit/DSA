def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index
    return "Not found"


array = [10,25,34,56,44]
target = 56

result = linear_search(array,target)

if result != "Not found":
    print(f"Element found at index {result}")
else:
    print("Element not found")





