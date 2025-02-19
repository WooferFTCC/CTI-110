# Samuel Abling
# 02/19/2025
# P2HW2
# Program for calculating statistics of the user's input grades from 6 modules


# Initialize dict from input grades

moduleGrades = (
    float(input('\nEnter grade for Module 1: ')),
    float(input('Enter grade for Module 2: ')),
    float(input('Enter grade for Module 3: ')),
    float(input('Enter grade for Module 4: ')),
    float(input('Enter grade for Module 5: ')),
    float(input('Enter grade for Module 6: '))
)


# Calculate results

gLow = min(moduleGrades)
gHigh = max(moduleGrades)
gSum = sum(moduleGrades)
gAvg = gSum / len(moduleGrades)


# Display

print(
    f'\n------------Results------------'
    f'\n{"Lowest Grade:":20}{gLow:.1f}'
    f'\n{"Highest Grade:":20}{gHigh:.1f}'
    f'\n{"Sum of Grades:":20}{gSum:.1f}'
    f'\n{"Average:":20}{gAvg:.2f}'
    f'\n-------------------------------\n'
)