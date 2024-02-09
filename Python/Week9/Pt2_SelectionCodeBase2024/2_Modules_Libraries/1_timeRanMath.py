# What is a library or module?
# A Python module is a ".py" file that contains definitions and statements, a module can define functions, classes variables and runnable code.
# A Python library is a collection of modules which provide functionality for various tasks.

# This module provides various functions to manipulate time values.
import time

"Predict, then Run, and then Investigate"
name = "John"
print(name)

# invoke the sleep method from the time module
"To Do: Can you explain what the 'time.sleep(3)' line of code does?"
# time.sleep(3) makes the programme pause for the specified time (3 seconds).
time.sleep(5)
print(f"Printed \n{name}")
print(f"The directory\n{dir()}")
print(f"The builtins\n{dir(__builtins__)}")
print(f"The directory with the time module\n{dir(time)}")

 # import (module) random
import random
"syntax : variable = method(start and end values)"
# Return random integer in range [a, b], including both end points.
randNum = random.randint(1, 50)
print(f"The random value is: {randNum}")

"Modify "
"To Do: Task 1: Use randint from random module to generate random numbers"
# Modify the code above to generate ramdom numbers between 25 to 50
randNum = random.randint(25, 50)
print(f"The random value is: {randNum}")

# import (module) math
# This module provides access to the mathematical functions defined by the C standard
"Predict, then Run, and then Investigate"
import math
radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print(f"The area is {area}")

# Method 1
# Round (round) a number to a given precision in decimal digits.
print(f"The area displayed is rounded to 2 decimal places {round(area, 2)}")

# Method 2
print(f"The area displayed is rounded to 2 decimal places {area:.3f}")
  
# Method 3 from the math module
roundDown = math.floor(area) 
print(f"The area displayed is rounded to 2 decimal places {roundDown}") 
roundUp = math.ceil(area)
print(f"The area displayed is rounded to 2 decimal places {roundUp}")