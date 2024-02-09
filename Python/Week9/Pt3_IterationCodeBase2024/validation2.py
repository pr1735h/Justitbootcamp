"Task 1: In the terminal Enter numeric values for the first and second number to perform addition and take note of the output "

"""Task 2: In the terminal Enter a numeric value  for the first number and string value(ten/one/two)
for the second number to perform addition and take note of the output"""

# create a boolean variable 
checkNum = True # allows to toggle bewtween true and false

while checkNum: # while True
    try:
        # attempts/runs the code
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        answer = num1 + num2
        print(f"The answer to {num1} + {num2} = {answer}")
        checkNum = False
    except ValueError: # the exception block will execute only if the code in the try block fails
        print("Only use integer values")


    finally:
        print("Executing...some code and processes")


"Task 3: Explain why did the program break, when you followed the instructions in task 2 but not in task 1"



# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception



# name = input("What is your name? ")