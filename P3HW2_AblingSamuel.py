# Samuel Abling
# 03/10/2025
# P3HW2
# This program generates a table of an employee's pay, including any potential overtime, after the user inputs the employee's name, hours worked that week, and their rate of pay.


# Config
columnWidth = 15


## Input name of employee, hours worked that week, and pay rate
print('\n')
name = str(input('Enter employee\'s name: '))
hours = round(float(input('Enter number of hours worked: ')), 2)
hours2 = hours
rate = round(float(input('Enter employee\'s pay rate: ')), 2)
overtime = 0


## If the employee worked overtime (40 hours), then Overtime hours = Hours - 40; Overtime Pay = Overtime hours * (Payrate * 1.5); Hours -= Overtime Hours
if hours > 40:
    OThours = hours - 40
    OTrate = rate * 1.5
    OTpay = (OThours * OTrate)
    hours2 -= OThours
    overtime = 1
else:
    overtime = 0


## Calculate the regular pay: Pay = Hours * Payrate
pay = round((hours2 * rate), 2)


## If overtime is 1, then Gross pay = Pay + Overtime Pay
# Else: Gross pay = Pay
if overtime == 1:
    gross = pay + OTpay

else:
    gross = pay


## Table

# Build row of headers
headerRow = f'{'Hours Worked':<{columnWidth}}{'Pay Rate':<{columnWidth}}'
if overtime == 1:
    headerRow += f'{'OverTime':<{columnWidth}}{'OverTime Pay':<{columnWidth}}{'RegHour Pay':<{columnWidth}}'
headerRow += f'{'Gross Pay':<{columnWidth}}'

# Build row of content
contentRow = f'{hours:<{columnWidth}}{rate:<{columnWidth}}'
if overtime == 1:
    contentRow += f'{OThours:<{columnWidth}}{OTpay:<{columnWidth}.2f}${pay:<{columnWidth}.2f}'
contentRow += f'${gross:<{columnWidth}.2f}'

# Display table
print(
    '-------------------------------------'
    f'\nEmployee name: {name}'
    '\n'
    f'\n{headerRow}'
    f'\n{'-' * len(headerRow)}'
    f'\n{contentRow}'
    '\n'
)