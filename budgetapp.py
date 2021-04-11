class Budget:
    """This is a budget class used to manage your personal budget.
    
    ATTRIBUTES:
    Name: str. The name of the budget
    Balance: int. The balance of the budget
    
    METHODS:
    Balance: Gives you the current balance of the budget
    Deposit: Enables you deposit to the budget
    Withdraw: Enables you withdraw from the budget
    Transfer: Enables you transfer from one budget to another
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def status(self):
        print(f'Your {self.name} balance is {self.balance}')

    def deposit(self):
        amount = input("Please enter amount to be deposited: ")
        print(f'Your {self.name} has been credited with {amount}')

    def withdraw(self):
        amount = input("Please enter amount to be withdrawn: ")
        print(f'Your {self.name} has been debited by {amount}')

    def transfer(self, other):
        amount = input("Please enter amount to be transferred: ")
        print(f'The sum of {amount} has been transferred from {self.name} to {other.name}')

food = Budget('food budget', 0)
clothing = Budget('clothing budget', 0)
entertainment = Budget('entertainment budget', 0)