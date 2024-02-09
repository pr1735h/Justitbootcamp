# The default data type for the input function is string
# The input function allow the program to take user input
"Objectives"
"" '' # Input() funtion in python
"" '' # Obtain input from the keyboard in a program

print("What is your name? ")  # display what is your name

# dynamically asking for user input instead of hardcoded values
"To DO: Task1: Debug the two lines of code below"
name = input()  # invoke the input funtion and assign to name variable
print("Your name is: ", name)

"After you have fix the bug above, answer the question below"
"To DO: Why is the code block below could be considered more efficient than the code block above? Ignore any commented code"
# invoke the input funtion and assign to name variable to dynamically ask for user input instead of hardcoded values
name1 = input(("What is your name? "))
print("Your name is: ", name1)
#This code is more efficient because it declares the question in the input value which reduces the block by one line.

"To DO: Knowledge Check: Why use type function as shown below?"
print(type(name))
#To check if the variable's value is a string or other data type.

"For further reading and independent learning refer to the link below"
# https://docs.python.org/3/library/functions.html#input


# The default data type for the input function is string
# The input function allow the program to take user input
"Objectives"
"" '' # Casting and/or conversion

userAge = int(input(("Please enter your age: ")))
print(type(userAge))
print("Your age is: ", userAge)

"To DO: Exercise: Provide screenshot to the anwers to the questions below in the chat"

# To DO:
# what is the equivalent of input in JavaScript?
# The equivalent of input in JS is prompt()

# what is the equivalent of converting a string to integer inJavaScript?
# The equivalent of converting a string to integer in JS is parseInt()

# Format the print statment using f-string
userAge = int(input("Please enter your age: "))
print(f"The type of userAge is: {type(userAge)}")
print(f"Your age is: {userAge}")

"To DO: Task 2: Working with the input function and datatypes"

num1 = input("Enter your first number: ")
# To complete the code block above
# Use a variable and invoke the input function ask for a second number
num2 = input("Enter your second number: ")
num1 = int(num1)
num2 = int(num2)
# Add the two numbers
sum1 = num1 + num2
# print out the total of the two numbers
print(sum1)
# Format your print statement to read, The answer to num1Value + num2Value is TotalValue
print(f"The answer to {num1} + {num2} is {sum1}")

"To DO: Task 3: Working with the input function and datatypes"
# Modify you solution above to take in decimal values instead of whole numbers
num3 = input("Enter your first number: ")
num4 = input("Enter your second number: ")
num3 = float(num3)
num4 = float(num4)
sum2 = num3 + num4
print(sum2)
print(f"The answer to {num3} + {num4} is {sum2}")