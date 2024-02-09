import logging
# objective
# Import and use the logging module/class
# Understand and use the severity levels
# Configure file path and use exception handling to write logs to file with different severity levels
"read for 2 minutes"

''' Python Exception is represented in class hierarchy using built in or user define exception types
object of the class exception will be created when an exception is raised.
 exception class inherits from the base exception class

 Both the StandardError and Warning inherits from the Exception class.
 
 Standard errors will terminate program if not handle correctly
 Standard error like EOFError results in trying to read beyond the end of a file at run time.
 ZeroDivisionError trying to divide by zero.
 Indentation error improper indentation of programming/code blocks.'''

# An exception is handled using the try and except block.

"To Do: Predict, then Run, and then Investigate"

#different logging methods and severity

logging.basicConfig(level=logging.DEBUG) #comment to see what logging level will be displayed in the terminal
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")

"To Do: Modify"
# Modify: 
# Task 1. Change the level from level=logging.DEBUG to logging.INFO, run the code and explain the output from the terminal
logging.basicConfig(level=logging.INFO)
# The output will show all levels apart from debug.
# Task 2. Remove the level=logging.DEBUG or level=logging.INFO, between the parenthesis of logging.basicConfig and run the code and explain the output from the terminal
logging.basicConfig()
# The output will show all levels