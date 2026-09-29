class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Added {amount} to the balance.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Sorry not enough money.")
            return

        self.balance -= amount
        print(f"Withdrew {amount} from the balance.")

    def __str__(self):
        return f"Owner: {self.owner} \n Balance: {self.balance}"

account = Account("Ivan",10000)
print(account.balance)
account.deposit(100)
account.withdraw(550)
print(account.balance)