import random

"Modify "
"You have been provided with an incomplete diceRoll.py program with bugs "
"To Do: Task 1: Review, debug and fix the code below, by repacing the '?s' with the code syntax "
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"Dice: {dice1} | Dice: {dice2}")

dice = dice1 + dice2  # The values of both dice

if dice == 12:  # Check if both dice equals 12
    dice = dice * 2  # Double the total from both dice
    print(f"You threw a: {dice}")
else:
    if dice1 == dice2:
        dice = dice  # 10 = 10
        print(f"You threw {dice}")
print(f"You threw a total of: {dice}")

"To Do: Task 2: Add notes below to explain the application in your own words"

"""
There are 3 variables, the first 2 declare a random number between 1 and 6. Those variables are printed with f-strings to show the results.
The third variable adds the first 2 variables together.
The if statement checks if the value of the 3rd variable is equal to 12, if it is then the value of the 3rd variable is multiplied by 2 and then printed.
The else statement checks if the value of the 1st variable is equal to the value of the 2nd variable, if it is then the value of the 3rd variable stays the same and is printed.
If none of those conditions are met then the result is printed out in the last statement.
"""