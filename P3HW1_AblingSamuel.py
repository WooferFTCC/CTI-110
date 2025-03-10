# Samuel Abling
# 03/10/2025
# P3HW1
# This program takes an input of number grades, then determines the average of the input and displays letter grade for that average.


## Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


## Calculate lowest, highest, gross, and average for grades
low = min(grades)
high = max(grades)
gross = sum(grades)
avg = gross / len(grades)


## Determine letter grade for average
grd = 'Your grade is: '

# A
if avg >= 90:
    grd += 'A'
# B
elif avg >= 80:
    grd += 'B'
# C
elif avg >= 70:
    grd += 'C'
# D
elif avg >= 60:
    grd+= 'D'
# F
else:
    grd += 'F'


## Display results

print(
    '\n'
    '------------Results------------'
    f'\n{'Lowest Grade:':20} {round(low, 2)}'
    f'\n{'Highest Grade:':20} {round(high, 2)}'
    f'\n{'Sum of Grades:':20} {round(gross, 2)}'
    f'\n{'Average of Grades:':20} {round(avg, 2)}'
    '\n'
    '-------------------------------'
    f'\n{grd}'
    '\n'
)