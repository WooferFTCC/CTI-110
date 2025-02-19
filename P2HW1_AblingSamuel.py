# Samuel Abling
# 02/19/2020
# P2HW1
# Program for calculating user's remaining budget after travel expenses


# Inform user of program's function

print('\nThis program calculates and displays travel expenses.')


# Initialize variables, prompt user for inputs

budget = float(input('\nEnter Budget: '))

destination = str(input('\nEnter your travel destination: '))

expGas = float(input('\nHow much do you think you will spend on gas? '))

expAccom = float(input('\nApproximately, how much will you need for accomodation/hotel? '))

expFood = float(input('\nLast, how much do you need for food? '))


# Subtract all expenses from the budget

totalExp = expGas + expFood + expAccom
remainder = budget - totalExp


# Display budget, destination, expenses, total expenses, then remainder

print(
      f'\n------------Travel Expenses------------\n'
      f'{"Location:":20}  {destination}\n'
      f'{"Initial Budget:":20}  ${budget:.2f}\n'
      f'{"Fuel:":20}  ${expGas:.2f}\n'
      f'{"Accomodation:":20}  ${expAccom:.2f}\n'
      f'{"Food:":20}  ${expFood:.2f}\n'
      f'----------------------------------------\n\n'

      f'{"Remaining Balance:":20}  ${remainder:.2f}\n'
      )