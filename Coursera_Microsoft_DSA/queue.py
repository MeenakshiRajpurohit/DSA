
from collections import deque
queue = deque()

queue.append("Calculate: 15 + 5")
queue.append("Calculate: 12 - 3")
queue.append("Calculate: 9 * 2")
queue.append("Calculate: 16 / 4")
queue.append("Calculate: 2 ^ 3")

first_expression = queue.popleft()
print("First pending calculation (dequeued):", first_expression)

print("Remaining actions in the queue:")
for expression in queue:
    print(expression)










