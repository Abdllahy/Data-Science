# static vs Instance method example

class BankAccount:
    MIN_BALANCE = 100 # is it a convention to capitalize the constant variables

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
        # if amount > 0:
            self.balance += amount
            print(f"{self.owner}'s new balance is {self.balance}")
        else:
            print("Invalid amount")

    def _is_valid_amount(self, amount):
        return amount > 0


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    

account = BankAccount("Mark", 500)
account.deposit(100)
print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(6))
    