"""
Make a class that represents a bank account. Create four methods named set_details, display,
withdraw and deposit.

In the set_details method, create two instance variables : name and balance.
The default value for balance should be zero. In the display method,
display the values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter.
Inside withdraw, subtract the amount from balance and inside deposit,
add the amount to the balance.

Create two instances of this class and call the methods on those instances.


"""
class BankAccount:

    def __init__(self):
        self.value = None
        self.name = None

    def set_details(self, name, value=0):
        self.name = name
        self.value = value

    def display(self):
        print(fr'name of the account holder : {self.name}, ammount : {self.value}')

    def withdraw(self, deduct):
        self.value-=deduct

    def deposit(self, deposit):
        self.value+=deposit


a1 = BankAccount()
a1.set_details('Mike', 200)

a2 = BankAccount()
a2.set_details('Tom')

a1.display()
a2.display()

a1.withdraw(100)
a2.deposit(500)

a1.display()
a2.display()
