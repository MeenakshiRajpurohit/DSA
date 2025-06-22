stack = []

stack.append("Entered 5 + 3")
stack.append("Entered 10 - 2")
stack.append("Entered 7 * 4")
stack.append("Entered 20 / 5")
stack.append("Entered 3 ^ 2")

recent_action = stack.pop()
print("Most recent action (popped):", recent_action)

print("Remaining actions in the stack:")
for action in reversed(stack):
    print(action)










