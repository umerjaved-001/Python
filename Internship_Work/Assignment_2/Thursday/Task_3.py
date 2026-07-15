def calculate_total(a, b, c):
    return a + b + c

sub_1 = float(input("Enter marks of Subject 1 :"))
sub_2 = float(input("Enter marks of Subject 2 :"))
sub_3 = float(input("Enter marks of Subject 3 :"))

Result = calculate_total(sub_1,sub_2,sub_3)
print("Total Marks: ",Result)

