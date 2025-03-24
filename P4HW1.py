# Samuel Abling
# 03/24/2025
# P4HW1
# Calculates an average and associated letter grade from a list of input scores


# Initialize vars
scoreList = []
scoreCount = 1


# Ask for amount of scores to input
scoresAmount = input('\nHow many scores do you want to enter?: ')


# Check if scoresAmount is an integer, then convert to INT when valid
while scoresAmount.isnumeric() == False or scoresAmount == 0:
    scoresAmount = input(
        '\nINVALID amount entered'
        '\nAmount of scores should be an integer greater than 0'
        '\nHow many scores do you want to enter?: '
        )
scoresAmount = int(scoresAmount)


# Ask for each score until scoreList is populated with the amount of scores in scoresAmount.
print('\n')
while scoreCount <= (scoresAmount):
    enterScore = input(f'Enter score #{scoreCount}: ')

    # Score check loop
    validScore = 0
    while validScore == 0:
    # Check if input is a positive number
        while enterScore.isnumeric() == False:
            enterScore = input(
            '\nINVALID Score entered!!!!'
            '\nScore should be between 0 and 100'
            f'\nEnter score #{scoreCount} again: '
            )
        else:
            enterScore = float(enterScore)
        
        # Now that input is guaranteed to be an int, check if between 1-100. If not within that range, reset loop.
        if 0 < enterScore <= 100:
            validScore = 1
        else:
            enterScore = ''

    # Input passes checks, gets added to scoreList. Increment counter.
    scoreList.append(enterScore)
    scoreCount += 1 # the pain of wanting to modify the global of this var but I'm fairly sure that would go against the rules established in this class :(


# Calculate lowest, highest, sum, and avg from grades. Drop lowest from scoreList.
gLow = min(scoreList)
scoreList.remove(gLow)

gHigh = max(scoreList)
gSum = sum(scoreList)
gAvg = gSum / len(scoreList)
grade = ''

# Calculate letter grade from average
# A
if gAvg >= 90:
    grade += 'A'
# B
elif gAvg >= 80:
    grade += 'B'
# C
elif gAvg >= 70:
    grade += 'C'
# D
elif gAvg >= 60:
    grade+= 'D'
# F
else:
    grade += 'F'


# Setup modified list to be displayed, along with a variable for the upper display seperator
modListDisplay = f'{"Modified List":15}{":":5}{[score for score in scoreList]}'
seperatorHalf = '-' * (len(modListDisplay) // 2 - 4)

# Display
print('\n'
    f'\n{seperatorHalf}Results{seperatorHalf}'
    f'\n{"Lowest Score":15}{":":5}{gLow:.1f}'
    f'\n{modListDisplay}'
    f'\n{"Scores Average":15}{":":5}{gAvg:.2f}'
    f'\n{"Grade":15}{":":5}{grade}'
    f'\n{'-' * (len(modListDisplay) - 1)}\n'
)