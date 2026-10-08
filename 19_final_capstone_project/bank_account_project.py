from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount} to {self.owner}")
        else:
            print(f"Invalid amount.")
    @abstractmethod
    def withdraw(self,amount):
        pass

    def get_balance(self):
        return f"Balance: {self.balance:.2f}"

    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")

    @abstractmethod
    def account_type(self):
        pass

class CheckingAccount(Account):
    overdraft = 500
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount <= self.balance + self.overdraft:
            self.balance -= amount
            print(f"Successfully withdrawn {amount:.2f}")
        else:
            print(f"Not enough money.")

    def account_type(self):
        return "Checking Account"

class SavingsAccount(Account):
    min_balance = 100

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.balance - amount  >= self.min_balance:
            self.balance -= amount
            print(f"Successfully withdrawn {amount:.2f}")
        else:
            print(f"At least {self.min_balance} must remain in the saving account!")

    def account_type(self):
        return "Saving Account"

class BusinessAccount(Account):
    transaction_fee = 3.50

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount.")
        elif self.balance >= amount + self.transaction_fee:
            self.balance -= amount + self.transaction_fee
            print(f'Successfully withdrawn {amount:.2f}')
            print(f"Fee is {self.transaction_fee}")
        else:
            print(f"Not enough money.")
    def account_type(self):
        return "Business Account"

def atm_menu(account):

    while True:
        print("______________________")
        print(account.account_type())
        print("______________________")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Information")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print(account.get_balance())

        elif choice == "2":
            try:
                amount = float(input("Enter amount: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            account.show_info()

        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    checking = CheckingAccount("Ivan", 1500)
    savings = SavingsAccount("Petar", 5000)
    business = BusinessAccount("Georgi", 1000)

    while True:
        print("________________________")
        print("           ATM          ")
        print("________________________")
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Business Account")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm_menu(checking)

        elif choice == "2":
            atm_menu(savings)

        elif choice == "3":
            atm_menu(business)

        elif choice == "4":
            print("Thank you for your time!")
            break
        else:
            print("Invalid choice.")
main()