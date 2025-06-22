numbers = [1, 3, 3, 4, 2, 5, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

