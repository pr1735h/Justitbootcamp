import logging

"To Do: Predict, then Run, and then Investigate"
#different logging methods and severity
logging.basicConfig(filename=r"Week10/OneDrive_1_29-01-2024/Pt8_ExceptionsCodeBase2024/1_Exceptions/file2.log", level=logging.DEBUG)

try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")

except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user see
    print("You can't divide a number by zero")
    logging.warning("User attempted to divide by zero")

finally:
    print("Closing....")


"To Do: Task 1: Modify"
# Make:
# 1. Use any one of the logging methods to log error to the Exceptions folder in a file called myFilelog1.log

logging.basicConfig(filename=r"Week10/OneDrive_1_29-01-2024/Pt8_ExceptionsCodeBase2024/1_Exceptions/myFilelog1.log", level=logging.DEBUG)

try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")

except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user see
    print("You can't divide a number by zero")
    logging.warning(f"ON {time.asctime()}User attempted to divide by zero")

else:
    # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")

finally:
    print("Closing....")