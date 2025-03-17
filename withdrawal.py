balance = 5000
withdraw = int(input("Enter amount tp withdrawal:"))

if withdraw < 0:
    print("Invalid amount! Enter a positive number.")
elif withdraw > balance:
    print("Insufficiant balance!")
else:
    balance -= withdraw
    print("Withdrawal successful. Remaining balance:", balance)