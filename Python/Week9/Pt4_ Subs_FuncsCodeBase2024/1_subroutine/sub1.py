"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, asubroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"
"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"
"def just defines the subroutine(function)"
"A subroutine(function) is not executed unless the subroutine is called."
"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"
"Custom built function"   # A function that you have created yourself and imported into other programs that you have created.
# Syntax:
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutineName/function()
"""

"To Do: Predict, then Run, and then Investigate"
# name is a global variable 
# name = "Emjay"
# print("Your name is: ", name)

# def define the subroutine/function user
def user():
    # body of subroutine(write your code here)
    name = "Emjay" # name is a now a local variable 
    print(f"Welcome {name}")

# call/invoke the subroutine/function
# user()
# print("hello", user)
# def define the subroutine userName
def userName():
    name = input("What is your name? ")
    return f"Your name is {name}"

# print("Welcome")
# userName()

"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"
# print(user()) # Create a print function and in the brackets call the subroutine "user()"
"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest"
def info():
    address = input("Please enter your address: ")
    interest = input("Tell us about your interests: ")
    return f"{address}, and your interests are:\n{interest}"

# print(f"{userName()}.\nYour address is {info()}")

'Task 3: Investigate  if __name__ == "__main__":'
'Copy and paste the code block above if __name__ == "__main__":  in the browser to investigate it use'
if __name__ == "__main__":
    # Add comment to explain why it can be used in your program in your own words"
    user()
    print(f"{userName()}.\nYour address is {info()}")

# call/invoke the subroutine
# call/invoke the subroutine
  
"Knowledge Check"
"Task 4: Linking existing knowledge with new knowledge"
# What do you think is the equivalent of the python 'def' keyword in JavaScript
# The JS equivalent of "def" is "function".

"Further reading on python functions"