number = input("Enter a number: ")
clean_number = number.replace("-", "")
digit_count = len(clean_number)

print("The number of digits is:", digit_count)