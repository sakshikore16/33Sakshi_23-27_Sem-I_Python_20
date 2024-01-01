# 20. Build a simulation of ATM system with classes for accounts, 
# transactions, and users. Implement methods for withdrawing 
# cash, checking balances, and handling PIN verification.

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

class Transaction:
    @staticmethod
    def verify_pin(user_pin, entered_pin):
        return user_pin == entered_pin

def main():
    accounts = []

    while True:
        print("\nATM Simulation")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            accounts.append(Account(account_number, pin))
            print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")

            user_account = next((account for account in accounts if account.account_number == account_number), None)

            if user_account and Transaction.verify_pin(user_account.pin, pin):
                print("\nLogin successful!")
                while True:
                    print("\n1. Check Balance")
                    print("2. Withdraw Cash")
                    print("3. Add Money")
                    print("4. Logout")

                    option = input("Enter your choice (1-4): ")

                    if option == "1":
                        print(f"Current Balance: ${user_account.check_balance()}")

                    elif option == "2":
                        amount = float(input("Enter the amount to withdraw: $"))
                        if user_account.withdraw_cash(amount):
                            print(f"Withdrawal successful! Remaining Balance: ${user_account.check_balance()}")
                        else:
                            print("Invalid withdrawal amount or insufficient funds.")

                    elif option == "3":
                        amount = float(input("Enter the amount to add: $"))
                        if user_account.add_money(amount):
                            print(f"Money added successfully! New Balance: ${user_account.check_balance()}")
                        else:
                            print("Invalid amount to add.")

                    elif option == "4":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")

            else:
                print("Invalid account number or PIN. Please try again.")

        elif choice == "3":
            print("Exiting ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
