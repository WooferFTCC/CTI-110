# Samuel Abling
# P4LAB2
# 03/21/2025
# Requests a positive integer then prints that int's multiplication table from 1 - 12.


# Program runs in loop until cont(inue) == no
fakeBreak = 0
while fakeBreak == 0:
    
    # Loop checking userIn until the user inputs a positive integer as a string.
    userIn = ''
    while not userIn.isnumeric():
        userIn = input('\nEnter a nonnegative integer: ')

        # Check if input string is negative.
        if userIn[0] == '-':
            print('\nThis program does not accept negative integers.')
        # Check if input is an integer.
        elif userIn.isnumeric() == False:
            print('\nPlease type an integer.')

    # Convert input to an int
    num = int(userIn)


    # Print multiplication table
    print('\n')
    for x in range(12):
        print(f'{num} * {x + 1} = {num * (x + 1)}')

    # Ask user if they want to run the program again.
    cont = input('\nWould you like to run the program again? (yes / no) ')
    cont = cont.lower()

    while cont != 'yes' and cont != 'no':
        cont = input(
            '\nINVALID INPUT'
            '\nPlease enter only "yes" or "no"'
            '\nWould you like to run the program again? (yes / no) '
        )
    if cont == 'no':
        print('\n')
        fakeBreak = 1