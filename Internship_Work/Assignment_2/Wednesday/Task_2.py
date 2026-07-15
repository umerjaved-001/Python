def table(number):
    for i in range(1,11):
        result = number * i
        print(number ,"*", i ,"=", result)

number = int(input("Enter a Number:"))
table(number)