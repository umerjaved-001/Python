# Write a program that checks whether a bank account has sufficient balance for a withdrawal request.\

# Task 4

withdraw_amount = float(input("Enter the Withdrawal Amount:"))
balance = 100000
if withdraw_amount <= balance :
    print("Withdrawal Request Completed Successfully.")
else:
    print("Withdrawal Request Denied. You donot have enough balance.")
