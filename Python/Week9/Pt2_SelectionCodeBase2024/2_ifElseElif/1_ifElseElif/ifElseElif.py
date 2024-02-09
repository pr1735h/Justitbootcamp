import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
# Selection is used to control the flow of the program

score = int(input("Enter a number: "))
"Predict, then Run, and then Investigate"

# check the condition that score is greater than 100 or less than 0
if score > 100 or score < 0:
    # create a variable and assign it the value Invalid Entry
    grade = "Invalid Entry"
# check the condition that score is between 75 and 100
elif score >= 75 and score <= 100:
    # create avariable and assign it the value A
    grade = "A"
# check the condition that score is between 60 and 74
elif score >= 60 and score <= 74:
    # reassign the grade variable the value B
    grade = "B"
# check the condition that score is between 50 and 59
elif score >= 50 and score <= 59:
    # reassign the grade variable the value C
    grade = "C"
# reassign the grade variable the value F
else:
    grade = "F"
print(f"You have scored {score} and your grade is {grade}")

"To Do: Q&A"
"What do you think is the equivalent of JS else if in python?"


"Make"
"To Do: Task 1: Using if elif and else"
# Create a Menu program that allow user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice
while True:
    print("Menu\n1. Music\n2. Maths\n3. Science\n4. Exit")
    choice = input("Please enter your choice (1-4): ")
    if choice == '1':
        print(f"You selected Music.")
    elif choice == '2':
        print(f"You selected Maths.")
    elif choice == '3':
        print(f"You selected Science.")
    elif choice == '4':
        clear_console()
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

"To Do: Task 2:"
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]
numInput = int(input("Guess a number: "))
if numInput in numList:
    print(f"{numInput} is a correct number!")
else:
    print(f"{numInput} is not a correct answer!")