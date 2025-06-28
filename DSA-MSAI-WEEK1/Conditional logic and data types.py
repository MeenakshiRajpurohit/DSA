x = [1,2,3,4,5,6,7,8,9,10,-10]
for y in x:
    if y%2 == 0:
        print("positive even")
    else:
        print("positive odd")
    if y == 0:
        print("zero")
    elif y < 0:
        print("its a negative number")
print(x[0])
