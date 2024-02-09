# Selection is used to control the flow of the program
pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"

"Predict, then Run, and then Investigate"
# check the condition that pStudy value is same as the value held in curProgram
# do something/execute the line of code below if the condition is checked above true/met
# The block(else) of code will be executed if the condition in the if block is not true/not met
if pStudy == curProgram:
    print(f"{pStudy} will start on 27/03/2024")
else:
    print(f"{pStudy} is not a valid course.")

"Modify"
"To Do: Exercise"
# Modify the code above to use the "!=" operator, or the "not" operator
if pStudy != curProgram:
    print(f"{pStudy} is not a valid course.")
else:
    print(f"{pStudy} will start on 27/03/2024")

"Your Turn to: Apply and Build"
"Task 1: Using if and else"
# 1. Create a program that find the minimum value between two numbers using if else
import math
import random
num1 = random.randint(1, 50)
num2 = random.randint(2, 51)
if num1 > num2:
    print(f"The first number ({num1}) is greater than the second number({num2})")
elif num1 == num2:
    print(f"The first number ({num1}) is equal to the second number ({num2})")
else:
    print(f"The first number ({num1}) is lower than the second number({num2})")
"Task 2"
# 2.Create a python program to check user's password and print "Logged In" if successful
# else "Not Logged In“ when unsuccessful.
passWord = "abc123"
passIn = input("Type your password here: ")
if passWord == passIn:
    print("Logged In")
else:
    print("Not Logged In")