import collections

from collections import deque

results = deque()

results.append("Result: 8")
results.append("Result: 5")
results.append("Results: 28")
results.append("Results: 4")
results.append("Results: 9")

results.remove("Result: 5")

print("Contents of the linked list:")
for result in results:
    print(result)










