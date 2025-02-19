# Samuel Abling
# 02/17/2025
# P2LAB2
# The user can input the model of a car from the given key list to view that car's miles per gallon (mpg), then input a distance of miles to see how many gallons of gas that car requires for that distance.


# Initialize then display dictionary

carsMPG = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
print(f'\n{carsMPG.keys()}')


# Input car key, assign mpg var

userCar = str(input('\nEnter a vehicle to see its mpg: '))
userMPG = carsMPG[userCar]


# Print mpg key from input vehicle

print(f'\nThe {userCar} gets {userMPG} mpg.')


# Input miles, calculate gas result

miles = float(input(f'\nHow many miles will you drive the {userCar}? '))
gas = float(miles / userMPG)

# Print gas result

print(f'\n{gas:.2f} gallon(s) of gas are needed to drive the {userCar} {miles} miles.\n')