"Parameter(s): used in a subroutine/function to allow values to be passed into them/used as a place holder(s)"

"To Do: Predict, then Run, and then Investigate"

# define the subroutine/function addition with parameters par1 and para2
"In the subroutine definition, you pass in the parameter(s)(placeholder(s))"
def addition(num1, num2):
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")

"in the subroutine call, you pass in the argument(s)"
addition(11, 22)

"Make/Modify"
"To Do: Task 1 : Modify the subroutine call below to pass in you own name as an argument "
addition("Pritesh ", "Hirani")
def info(pname, paddress, pinterests):
    print(f"Your name is {pname} and you live at {paddress} and you like {pinterests}")
info("Pritesh Hirani", "17 Laburnum Grove", "Games, Music, Food")

# if __name__ == "__main__":
#     # Method 1
#     # in the subroutine call we pass in the integer values(1,2) within the braces as an argument to be passed
#     # into the parameters par1 and para2
#     addition(10,20) # 10 will passed into paraNum1, 20 will be passed into paraNum1
#     addition(11.6,202.67)
#     addition(["a","b"], ["c", "d"])
#     addition("Abdul", "Malik")
  
   
#     # Method 2
#     # in the subrotuine call we pass in the variable name  within the braces as an argument to be passed
#     # into the parameter paraUname
#     #in the subroutine call we pass in the num1 and num2  within the braces as an argument to be passed
#     #into the parameters par1 and para2
#     argNum1 = int(input("Enter your first number: "))
#     argNum2 = int(input("Enter your second number: "))
#     addition(argNum1, argNum2)
  

#     argNum1 = input("Enter your first name: ")
#     argNum2 = input("Enter your last name: ")
#     addition(argNum1, argNum2)

#     argNum1 = ["e", "f"]
#     argNum2 = ["g", "h"]
#     addition(argNum1, argNum2)


#     # userData 
#     name = input("What is your name? ")
#     address = input("What is your address? ")
#     interest = input("What is your interest? ")

#     user_data(name, address, interest)