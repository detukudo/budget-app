from budgetapp import Budget
from budgetapp import food, clothing, entertainment

"""This is the frontend of the budget app for users to interact with"""

print("Welcome to your budget app")
print('Here are the budget types:')
print('1. Food')
print('2. Clothing')
print('3. Entertainment')

budget_type = int(input('Please select an option: '))

print("Which operation would you like to perform?")
print("1. Check balance")
print("2. Deposit funds")
print("3. Withdraw funds") 
print("4. Transfer funds")

operation_type = int(input('Please select an option: '))

if (budget_type == 1 and operation_type == 1):
    food.status()

elif (budget_type == 1 and operation_type == 2):
    food.deposit()

elif (budget_type == 1 and operation_type == 3):
    food.withdraw()

elif (budget_type == 1 and operation_type == 4):
    print('1. Clothing')
    print('2. Entertainment')
    credit_budget = int(input('Please enter budget to be credited: '))
    
    if (credit_budget == 1):
        food.transfer(clothing)
    
    elif (credit_budget == 2):
        food.transfer(entertainment)
    
    else:
        print('Invalid selection, pls try again')

elif (budget_type == 2 and operation_type == 1):
    clothing.status()

elif (budget_type == 2 and operation_type == 2):
    clothing.deposit()

elif (budget_type ==2 and operation_type == 3):
    clothing.withdraw()

elif (budget_type == 2 and operation_type == 4):
    print('1. food')
    print('2. Entertainment')
    credit_budget = int(input('Please enter budget to be credited: '))
    
    if (credit_budget == 1):
        clothing.transfer(food)
    
    elif (credit_budget == 2):
        clothing.transfer(entertainment)
    
    else:
        print('Invalid selection, pls try again')

elif (budget_type == 3 and operation_type == 1):
    entertainment.status()

elif (budget_type == 3 and operation_type == 2):
    entertainment.deposit()

elif (budget_type ==3 and operation_type == 3):
    entertainment.withdraw()

elif (budget_type == 3 and operation_type == 4):
    print('1. food')
    print('2. Clothing')
    credit_budget = int(input('Please enter budget to be credited: '))
    
    if (credit_budget == 1):
        entertainment.transfer(food)
    
    elif (credit_budget == 2):
        entertainment.transfer(clothing)

    else:
        print('Invalid selection, pls try again')

else:
    print('Invalid selection, pls try again')