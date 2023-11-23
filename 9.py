
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            commission = (amount // 100) * 2
            self.balance += amount - commission
            print(f"You successfully deposited {amount} zł. Commission charged: {commission} zł.")
        else:
            print("Error: Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew {amount} zł. You have {self.balance} zł left in your account.")
        elif amount < 0:
            print("Error: Invalid withdrawal amount")
        else:
            print("Error: Insufficient funds.")

    def change_ownership(self, new_owner_name):
        self.owner_name = new_owner_name
        print(f"Ownership changed. The new owner is: {new_owner_name}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance on your account: {self.balance} zł\n")


account = BankAccount(account_number="10120450405457", owner_name="Janusz Kalicki", balance=1500)
account.display()

account.deposit(500)
account.display()

account.withdraw(200)
account.display()

account.change_ownership("Alicja Majek")
account.display()

