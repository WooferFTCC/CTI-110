# Samuel Abling
# P5LAB
# 04/02/2025
# Simulates a self-checkout machine by generating a random price, then takes the user input to subtract at that price until it's 0 or less and calculates how much change they're owed.


import random

def main():
    # Generate amount owed, establish variable to loop through
    total_owed = round(random.uniform(0.01, 100.00), 2)
    currently_owed = total_owed

    # Loop through querying the user for how much money they will pay until the total has been fully paid
    while currently_owed > 0:
        moneyInput = input(
            f'\nYou owe ${currently_owed}'
            f'\nHow much will you put in the self-checkout? $'
        )
        
        # Checks if moneyInput is a valid number input
        while checkIfMoney(moneyInput) == False:
            moneyInput = input(
                '\nINVALID INPUT'
                '\nVALUE SHOULD BE A DECIMAL OR A WHOLE NUMBER'
                '\n'
                f'\nYou owe ${currently_owed}'
                f'\nHow much will you put in the self-checkout? $'
            )

        # Subtract input money from the price
        currently_owed -= round(float(moneyInput), 2)
        currently_owed = round(currently_owed, 2)


    # Print change as both a decimal and a coin amounts
    print(f'\nChange is ${abs(currently_owed):.2f}')
    disperse_change(currently_owed)


## Functions

# Checks if INPUT is able to convert to float by looping through each character
def checkIfMoney(x):
    for digit in x:
        if digit.isnumeric() == False and digit != '.':
            return False
        
    return True
    

# Calculates change into dollars, quarters, dimes, nickels, and pennies
def disperse_change(change):
    # Convert decimal INPUT into an integer to work with
    mon = int(abs(100 * float(change)))

    # If mon == 0 after calculating previous coin type, the calculations are finished
    # Else, calculate next coin type

    if mon != 0:
        # Dollars
        if mon != 0:
            dol = mon // 100
            if dol != 0:
                print(f'{dol} dollar{"s" if dol > 1 else ""}')

            mon %= 100

        # Quarters
        if mon != 0:
            qu = mon // 25
            if qu != 0:
                print(f'{qu} quarter{"s" if qu > 1 else ""}')

            mon %= 25

        # Dimes
        if mon != 0:
            di = mon // 10
            if di != 0:
                print(f'{di} dime{"s" if di > 1 else ""}')

            mon %= 10

        # Nickels
        if mon != 0:
            ni = mon // 5
            if ni != 0:
                print(f'{ni} nickel{"s" if ni > 1 else ""}')

            mon %= 5

        # Pennies
        if mon != 0:
            pe = mon
            print(f'{pe} penn{"ies" if pe > 1 else "y"}')
        
        print('')

    # If 0 is input, print 'No change'
    else:
        print('No change\n')



main()