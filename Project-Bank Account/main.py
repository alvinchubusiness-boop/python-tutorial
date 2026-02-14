import random
from datetime import datetime

class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = float(balance)

        self.accountNumber = random.randint(100000, 999999)

        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"

        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"=== Account Created: {self._now()} ===\n")
            f.write(f"Name: {self.name}\n")
            f.write(f"Type: {self.accountType}\n")
            f.write(f"AccountNumber: {self.accountNumber}\n")
            f.write(f"Initial Balance: {self.balance:.2f}\n")
            f.write("--------------------------------------\n")

    def _now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False

        self.balance += amount
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{self._now()} | DEPOSIT  | +{amount:.2f} | BAL={self.balance:.2f}\n")
        return True

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False

        if amount > self.balance:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(f"{self._now()} | WITHDRAW | FAILED (Insufficient funds) | TRY={amount:.2f} | BAL={self.balance:.2f}\n")
            return False

        self.balance -= amount
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{self._now()} | WITHDRAW | -{amount:.2f} | BAL={self.balance:.2f}\n")
        return True

    def get_balance(self):
        return self.balance

    def get_user_id(self):
        return self.accountNumber

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except IOError:
            return "ERROR: Could not read statement file."

def main():
    acc1 = BankAccount("John", "chequing", 0)
    acc2 = BankAccount("Amy", "savings", 100)

    acc1.deposit(200)
    acc1.withdraw(50)

    acc2.withdraw(30)
    acc2.withdraw(5000)

    print("Account 1 balance:", acc1.get_balance())
    print("Account 2 balance:", acc2.get_balance())

    print("\n--- Account 1 History ---")
    print(acc1.get_transaction_history())

    print("\n--- Account 2 History ---")
    print(acc2.get_transaction_history())

    return True

main()
