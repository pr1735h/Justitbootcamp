import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

"Read through the commented code examples and reference or use it as a guide during lesson"

"Objectives"
"" '' # Understand and write code using the sequence programming construct in python
"" '' # Syntax
"" '' # Syntax vs Logic error  
# https://www.w3docs.com/learn-python/python-comments.html
# https://www.w3docs.com/snippets/python/print-multiple-arguments-in-python.html

# This is a single line comment using hashtag

"This is a single line comment in either single or double quotes"
'This is a single quote'

"""
This is a multiline comments
This is a multiline comments
This is a multiline comments
It has to be wrapped in 3 double quotes
"""


# Sequence in programming is a set of instructions performed in order,
# with each executed in turn

"Predict, then Run, and Investigate and modify"

# To DO:
print(2 * 2)   # Predict then Run, and Investigate
print(2 + 4)   # Modify to use a different operator
print(8 % 88)   # Modify to use a different operator
print(3 ** 3)  # Make : Use a different number and/or operator

# \n = newline

print("Refactored code\n")
"Predict, then Run, and Investigate"
#To DO: What is different in the terminal when the code below is executed?
print(2 * 3, "\n", 2 + 3, "\n", 2 / 3, "\n", 21 - 3)

# The python interpreter prints anything as it is, if placed between speech marks/ quotations
print("My name is Pritesh\nWelcome to python programming")

print("\nThis is Python Bootcamp")

# format print output
print("x = x * 3 \n", 6 * 3)


#To DO: Exercise: use the print statement to print
# Your name
print("My name is Pritesh")
# Your address
print("17 Laburnum Grove, Kingsbury, London")
# Your interests
print("Games, Eating, Cooking, Travelling")
# format your print function to print your details above in three separate lines
print("My name is Pritesh\n17 Laburnum Grove, Kingsbury, London\nGames, Eating, Cooking, Travelling")
# Perform either addition or calculation with two numbers
print(1110011 + 1100)
# Use text (format your output) in your addition"
print("1110011 + 1100 =\n", 1110011 + 1100)
"Share your solution as screenshot in nearpod collaboration board"

"Note: If stuck with formating print statement , refer to the printFuncsFormats.py file"

"To DO:Extension: Research"
#What is variable in python
#Modify your program to use variables instead of hard coded values 
a = "Pritesh"
b = "Hirani"
print("My name is", a, b)
c = 7
d = 9
print(c+d-1)

"Objectives"
"" '' #Variables and Variable naming convention
"" '' #Use meaningful identifiers
"" '' #Determine the need for variables
"" '' #Distinguish between declaration, initialisation, and assignment of variables 
"" '' #Demonstrate appropriate use of naming conventions
"" '' #Output data (e.g. print (myVvar))


"Research"
# What is variable in python
# Answer: A variable ........ ​is a container for storing data values.

"Characteristics or features of variables"
# A variable .........does not need to be declared before use, the type also does not need to be declared.
# A Python variable name must start with a letter or the underscore character. It cannot start with a number.
# It can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ). Variable names are case-sensitive2.

"Object references 1"
var_num = "an_object"  #  var_num is now a name referencing the object "an_object"
num1 = 10  
num2 = 2.0 
bVal1 = True 
bVal2 = False

"Refer to datatypes1.py and variables.py for further reading on variables and datatypes."