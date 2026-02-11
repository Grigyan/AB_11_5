class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance.")
        self.balance -= amount
        return self.balance

acc = BankAccount(100)
try:
    amt = float(input("Withdraw amount: "))
    print(f"New balance: {acc.withdraw(amt)}")
except (ValueError, InsufficientBalanceError) as e:
    print(f"Transaction failed: {e}")

