# creating a parent class called bank account
class BankAccount:
    """Represents a bank account
    states: balance
    Behaviours: withdraw"""

    def __init__(self, balance):
        """Initializes the balance attribute"""
        self.balance = balance

    def withdraw(self, amount):
        """Withdraws the amount from the balance"""
        self.balance -= amount
        return self.balance
    
# creating a child class called SavingsAccount

class SavingsAccount(BankAccount):
    """Represents a savings account that's inheriting from BankAccount
    States: balance, interest_rate
    Behaviours: withdraw, compute_interest"""

    def __init__(self, balance, interest_rate): # constructor speficic to the SavingsAccount with an additional parameter

        BankAccount.__init__(self, balance) # calling the constructor of the parent class
        self.interest_rate = interest_rate # initializing the interest_rate attribute

acc = SavingsAccount(1000, 20.7)
print(acc.interest_rate)


Savings_account = SavingsAccount(5000, 30.9)
print(isinstance(Savings_account, BankAccount))
print("------------------")
# we use isinstance() function to check if an object is an instance of a class 

print(isinstance(Savings_account, SavingsAccount))