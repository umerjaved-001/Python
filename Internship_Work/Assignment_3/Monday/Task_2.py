Five_Num = []

for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    Five_Num.append(number)

total = sum(Five_Num)
average = total / len(Five_Num)
highest = max(Five_Num)
lowest = min(Five_Num)

print("Sum:", total)
print("Average:", average)
print("Highest number:", highest)
print("Lowest number:", lowest)