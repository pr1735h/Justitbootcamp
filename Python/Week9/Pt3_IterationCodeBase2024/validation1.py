"Task 1: In the terminal Enter numeric values for the first and second number to perform addition and take note of the output "
"Task 2: In the terminal Enter a numeric value  for the first number and string value(ten/one/two) for the second number to perform addition and take note of the output"

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
answer = num1 + num2
print(f"The answer to {num1} + {num2} = {answer}")
print("Executing...some code and processes")

try: # Attempts/runs the code if it fails it runs the except block.
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")
    
except ValueError: # This block will execute only if the code in the try block fails!
    print("Only use integer values!")

finally: # This block always executes.
    print("Executing...some code and processes")


"Task 3: Explain why did the program break, when you followed the instructions in task 2 but not in task 1"
# num2 is defined as an integer but I entered a string as the input value.

# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception

# name = input("What is your name? ")