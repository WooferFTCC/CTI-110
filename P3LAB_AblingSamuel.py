# Samuel Abling
# 03/03/2025
# P3LAB
# Take an input of dollars and cents in the form of a float (EX: 1.23), then breaks that down into the most efficient change.


## Input money as a float, move up two decimal places, convert to int

print('\n')
mon = int(100 * float(input('Enter the amount of money as a float: $')))


## If mon == 0 after calculating previous coin type, the calculations are finished
## Else, calculate next coin type
#   If current coin type != 0, print the amount of that coin

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


## If 0 is input, print 'No change'

else:
    print('No change')

print('\n')
