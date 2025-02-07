# Samuel Abling
# 02/05/2025
# P1HW1
# Program for calculating an exponent and a basic addition-subtraction expression from integers

# Calculate Exponents
print('\n\n~~~~Calculating Exponents~~~~\n\n')
    # Input base value and exponent
expoBase = int(input('Enter an integer as the base value: '))
expoInput = int(input('Enter an integer as the exponent: '))
expoTotal = int()

    # Calculate
expoTotal = expoBase ** expoInput

    # Print results
print(f'\n{expoBase} raised to the power of {expoInput} is {expoTotal} !!')



# Add and Subtract
print('\n\n~~~~Addition and Subtraction~~~~\n\n')
    # Input base value, addition value, and subtraction value
addSubBase = int(input('Enter a starting integer: '))
addInput = int(input('Enter an integer to add: '))
subInput = int(input('Enter an integer to subtract: '))
addSubTotal = int()

    # Calculate
addSubTotal = int(addSubBase + addInput - subInput)

    # Print results
print(f'\n{addSubBase} + {addInput} - {subInput} is equal to {addSubTotal}')

print('\n\n')