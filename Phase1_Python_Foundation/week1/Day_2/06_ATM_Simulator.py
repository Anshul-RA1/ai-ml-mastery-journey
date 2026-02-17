"""
Challenge 6 · Hard (Bonus)
Simple ATM Simulator
Build an ATM with a starting balance of 
€10,000. 
Menu: 
1) Check Balance, 
2) Deposit, 
3) Withdraw, 
4) Exit. 
Validate: can't withdraw more than balance, 
can't deposit negative. 
Loop until user exits.

Use a while True loop with break on "Exit"
Use if/elif/else for menu choices
Validate all inputs (negative amounts, insufficient balance)
Keep a transaction history list
On exit, show summary of all transactions

"""
print("=" * 70)
print("🏧 RA_ONE BANK ATM 💰")
print("=" * 70)

balance = 10000
history = []    #Keep a transaction of historical transaction

print("Enter the Choice from the Menu! ")

menu = f"""
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Exit
        """

# print(menu)

while True:
    print(menu)
    user_choice = input("Enter your choice! ")
    
    if user_choice == "1":
        print(f"Your current balance is: ${balance:.2f}")

    elif user_choice == "2":
        try:
            user_deposit = float(input("Enter the deposit amount! "))
        except ValueError:
            print("❌ Invalid input! Please enter a number")
            continue
        if user_deposit <=0:
            print("❌ Amount must be positive")
        else:            
            balance = balance + user_deposit
            print(f"✅ Deposited ${user_deposit:.2f}")
            history.append(f"DEPOSIT: +${user_deposit:.2f}")
            print(f"Your current balance is: ${balance:.2f}")

    elif user_choice == "3":
        try:
            user_withdraw = float(input("Enter the withdraw amount! "))
        except ValueError:
            print("❌ Invalid input! Please enter a number")
            continue

        if user_withdraw <= 0:
            print("❌ Amount must be positive!")
        elif user_withdraw > balance:
            print(f"Insufficient balance! You only have ${balance:.2f}")
        else:
            balance = balance - user_withdraw
            print(f"✅ Withdrew ${user_withdraw:.2f}")
            history.append(f"WITHDREW: -${user_withdraw:.2f}")
            print(f"Your current balance is: ${balance:.2f}")

    elif user_choice == "4":
        print("Thank you for using RA_ONE Bank ATM")
        for transaction in history:
            print(transaction)
        break
    else:
        print("❌ Invalid choice! Please enter 1, 2, 3 or 4")
        


print("=" * 70)
print(f"Final Balance is {balance:.2f}")
print(f"Total Transactions: {len(history)}")
print(f"Historical transactions are: {history}")
print("=" * 70)
