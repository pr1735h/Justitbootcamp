import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

"To DO: Read through the data types examples in your own time and reference or use it as a guide during your lesson"

# Data types are nothing but variables you use to reserve some space in memory.
# Python variables do not need an explicit declaration to reserve memory space. 
# The declaration happens automatically when you assign a value to a variable.

"To DO: Further reading on datatypes in python"
#https://www.w3docs.com/learn-python/python-data-types.html

# String data types
# String are identified as a contiguous set of characters represented in 
# the quotation marks. Python allows for either # pairs of single or double
#  quotes. Strings are immutable sequence data type, i.e each time one makes 
# any changes to a string, completely new string object is created.
"Objectives"
"" '' # Commenting your code
"" '' # Data types
"" '' # Integer, Boolean, Float, Strings

# use "" for single line string value assigment 
s1 = "I love python, with double quotes" 
# use '' for single line string value assigment 
s2 = 'Python is the in demand programming language, with single quote'
# use """""" for multi line string value assigment 
s3 = """
This is multiline, 
This is multiline, 
This is multiline, 
This is multiline, 
"""

# ~string comments
"This is a comment"

"""
This is a multiline comment 
This is a multiline comment 
This is a multiline comment 
"""
# Boolean data types
# Boolean is yes/no or true or false (0 = off and 1 = on)
bVal1 = True # declare and assign a boolean type variable with value True
bVal2 = False # declare and assign a boolean type variable with value False

# Numeric data types
num1 = 20.5 # float(decimal) variable declaration and assigment 
num2 = 20.001 # integer variable declaration and assigment

"To DO: type() function is used to ?"
print(type(bVal1)) # bool
print(type(bVal2))

print(type(s1)) # str
print(type(s2))
print(type(s3))

print(type(num1)) #float
print(type(num2)) #int

"Modify:"
"To DO:"
# Modify the data structures above by changing their values or oject names
print(type(bVal1))
print(type(bVal2))

print(type(s1))
print(type(s2))
print(type(s3))

print(type(num1))
print(type(num3))

"Make:"
"To DO:"
# Produce five examples of numeric datatypes
num3 = 2, 20, 200 # Tuples are used to store multiple items in a single variable
print(num3)
num4 = 10 # Integer, Int are whole base numbers (0-9)
print(num4)
num5 = 1.1 # Float datatype is used for decimal values.
print(num5)
t = 1 + 2j # Complex number made up of a real and imaginary part
u = 3 + 4j
print(t + u)
print(t * u)
print(u - t)
print(u / t)
# Produce five examples of string datatypes
str1 = "Pritesh"
str2 = "Hirani"
str3 = "17 Laburnum Grove"
str4 = "Kingsbury"
str5 = "London"
print(str1,str2,"\n",str3,"\n",str4,"\n",str5)
