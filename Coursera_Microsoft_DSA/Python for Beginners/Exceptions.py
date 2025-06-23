try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age can not be zero!")
except ValueError:
    print("Invalid Value")






