# Selection is use to control the flow of the program
"""if condition is met:
    code block"""

score = 25
userNum = int(input("Enter a user number:"))
# check the condition that score(26) is greater than userNum(25)
# do something/execute the code block
if score < userNum:  
    print(f"Good score {userNum}")

###########################

someKey = "pass"
userKey = input("Enter the system key: ")

if someKey == userKey:
    print("You have provide a valid key.\nSystem unlocked!!!")
else:
    print("Incorrect password!")

# Selection is used to control the flow of the program
# int(input("Enter a number: "))

##########################
pStudy = input("Enter your study programme: ").title()
curProgramme = "Bootcamp"

if pStudy == curProgramme:
    print(f"Welcome to the {pStudy}")
else:
    print(f"{pStudy} is not one of our programmes, Please enquire within!")

"Predict, then Run, and then Investigate"
score2 = 26
userNum2 = 25
# check the condition that score is greater than userNum(25)
# do something/execute the line of code below, if the condition checked above is true/met
if score2 == userNum2:
    print("YOU WIN!!!")
# do something/execute the line of code below if the condition checked above is not true/ not met 
else:
    print("You didn't score enough points...")
"To Do: Q&A"
# What differs from writing if statement in JS and python?
"""
In Python the code block is defined by indents, 4 spaces or by pressing tab once and looks like this:
if condition:
    code to be executed if condition is true
In JS the code block is defined by curly braces {} and looks like this:
 if (condition) {
    code to be executed if condition is true
}
"""

"To Do: Task 1:"
"Modify the code above to use any one of the comparison operators below"

# """Comparison operator compare values
# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to"""
score3 = 25
userNum3 = 25

if score3 != userNum3:
    print("YOU WIN!!!")
else:
    print(f"{userNum3} isn't the right score...")


