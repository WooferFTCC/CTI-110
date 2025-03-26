# Samuel Abling
# 03/26/2025
# P4HW2
# Generates a table of an employee's pay, including any potential overtime, after the user inputs the employee's name, hours worked that week, and their rate of pay.
# Once terminated, the program displays the total amount of employees entered and the total wages paid out to them.


## Config
columnWidth = 15
# OTPay = 1.5
OTbonus = 1.5
# overtimeLimit = 40
overtimeLimit = 40
listEmployees = []
listPay = []
listOTPay = []
listGross = []
anyOvertime = False
fakeBreak = 0

## Dictionary
# Rate = Employee's rate of pay in hourly wages
# Pay = Actual $ value from (payrate * hours worked)
# OT = Overtime


## Enclose function in a while loop managed by the 'fakeBreak' sentienel
while fakeBreak == 0:
    # Input name of employee, hours worked that week, and pay rate
    print('\n')
    nameInput = str(input('Enter employee\'s name, or "Done" to terminate program: '))

    # Check if user requested to terminate program
    if nameInput.lower() == 'done':
        fakeBreak = 1

    # If program wasn't terminated, run program
    if fakeBreak == 0:
        # User inputs employee's hours then rate
        hoursInput = round(float(input(f'How many hours did {nameInput} work?: ')), 2)
        hours = hoursInput
        rateInput = round(float(input(f'What is {nameInput}\'s pay rate?: ')), 2)
        overtime = 0


        ## If the employee worked overtime (> 40 hours), then Overtime hours = Input hours - 40; Overtime Pay = Overtime hours * (Payrate * OTPay); Hours -= Overtime Hours
        if hoursInput > overtimeLimit:
            OThours = hoursInput - overtimeLimit
            OTrate = rateInput * OTbonus
            OTpay = (OThours * OTrate)
            hours -= OThours
            overtime = 1
        else:
            overtime = 0


        ## Calculate the regular pay: Pay = Hours * Payrate
        pay = round((hours * rateInput), 2)


        # If overtime is 1, then Gross pay = Pay + Overtime Pay
        # Else: Gross pay = Pay
        if overtime == 1:
            gross = pay + OTpay

        else:
            gross = pay

        # Populate lists
        listEmployees.append(nameInput)
        listPay.append(pay)
        listGross.append(gross)
        if overtime == 1:
            listOTPay.append(OTpay)
            anyOvertime = True


        ## Table
        # Build row of headers
        headerRow = f'{'Hours Worked':<{columnWidth}}{'Pay Rate':<{columnWidth}}'
        headerRow += f'{'OverTime':<{columnWidth}}{'OverTime Pay':<{columnWidth}}{'RegHour Pay':<{columnWidth}}'
        headerRow += f'{'Gross Pay':<{columnWidth}}'

        # Build row of content
        contentRow = f'{hoursInput:<{columnWidth}}{rateInput:<{columnWidth}}'
        contentRow += f'{OThours:<{columnWidth}}{OTpay:<{columnWidth}.2f}${pay:<{columnWidth}.2f}'
        contentRow += f'${gross:<{columnWidth}.2f}'

        seperatorLen = len(headerRow) - 5

        # Display table
        print(
            f'{'~' * seperatorLen}'
            '\n'
            f'\nEmployee name: {nameInput}'
            '\n'
            f'\n{headerRow}'
            f'\n{'-' * seperatorLen}'
            f'\n{contentRow}'
            '\n\n'
            f'{'~' * seperatorLen}'
        )
    
    ## Program is terminated, display final results
    else:
        print(
            '\n'
            f'\n{'Total number of employees entered':<40}{':':<5}{len(listEmployees)}'
            f'\n{'Total amount paid for overtime hours':<40}{':':<5}${sum(listOTPay):.2f}'
            f'\n{'Total amount paid for regular hours':<40}{':':<5}${sum(listPay):.2f}'
            f'\n{'Total amount paid in gross':<40}{':':<5}${sum(listGross):.2f}'
            '\n'
            )
        












# >:(