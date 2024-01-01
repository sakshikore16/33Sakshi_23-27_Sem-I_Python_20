# 4. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account created successfully. Account number: {account_number}")

        else:
            print("Account already exists. Please choose a different account number.")

    def check_balance(self, account_number):
        balance = self.accounts.get(account_number, None)
        if balance is not None:
            print(f"Balance for account {account_number}: ${balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposit successful. New balance: ${self.accounts[account_number]:.2f}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                print(f"Withdrawal successful. New balance: ${self.accounts[account_number]:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

# Create a bank
bank = Bank()

while True:
    print("\nBank Operations:")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        account_number = input("Enter the account number: ")
        initial_balance = float(input("Enter the initial balance: "))
        bank.create_account(account_number, initial_balance)

    elif choice == '2':
        account_number = input("Enter the account number: ")
        bank.check_balance(account_number)

    elif choice == '3':
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the deposit amount: "))
        bank.deposit(account_number, amount)

    elif choice == '4':
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the withdrawal amount: "))
        bank.withdraw(account_number, amount)

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
