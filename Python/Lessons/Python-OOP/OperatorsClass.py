class Customer:
    """Represents a customer
    states: name, balance
    Behaviour: None"""

    def __init__(self, name, balance, id):
        """Initializes the name and balance attributes"""
        self.name, self.balance, self.id = name, balance, id

customer1 = Customer("Jane", 1000, 123)
customer2 = Customer("Jane", 1000, 123)

print(customer1.name == customer2.name)
print(customer1)
print(customer2)

#  Performing comparison of objects
class BankCustomer:
    """Represents a bank customer
    states: name, id
    Behaviour: __eq__(compare objects of our class)"""

    def __init__(self, name, id):
        self.name, self.id = name, id

    def __eq__(self, other):
        # diagnostic print out
        print("eq has been called performing comparison now")
        
        # returns true if all attributes match
        return (self.id == other.id and \
                self.name == other.name)
    
cust_1 = BankCustomer("James", 110)
cust_2 = BankCustomer("Jack", 117)
print(cust_1 == cust_2)

"""
with code examples:
 - look into the hash method in OOP
 - understand the Liskov Substitution Principle and write code examples of when it is met 
 and when not met
"""