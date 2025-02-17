# Samuel Abling
# 02/12/2025
# P1HW2
# Program for calculating user's remaining budget after travel expenses

# Inform user of program's function

print('This program calculates and displays travel expenses\n')


# Initialize variables, prompt user for inputs

budget = int(input('Enter Budget: '))
destination = str(input('Enter your travel destination: '))
expGas = int(input('How much do you think you will spend on gas? '))
expAccom = int(input('Approximately, how much will you need for accomodation/hotel? '))
expFood = int(input('Last, how much do you need for food? '))


# Subtract all expenses from the budget

totalExp = expGas + expFood + expAccom
remainder = budget - totalExp


# Display budget, destination, expenses, total expenses, then remainder

print(
      f'------------Travel Expenses------------\n'
      f'Location: {destination}\n'
      f'Initial Budget: {budget}\n\n'

      f'Fuel: {expGas}\n'
      f'Accomodation: {expAccom}\n'
      f'Food: {expFood}\n\n'

      f'Remaining Balance: {remainder}\n'
      )
