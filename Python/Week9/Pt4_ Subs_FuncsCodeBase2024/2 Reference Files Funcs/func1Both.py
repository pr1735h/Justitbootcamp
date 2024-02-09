"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"

# create function use return statement without parameters and arguments
"To Do: Predict, then Run, and then Investigate"
def user():  # define the subroutine/function user
    name = "Emjay"
    return name

print(user())
print(f"Your name is {user()}")

# or

aName = user()
print(aName)
print(f"Your name is {aName}")


def anotherUser():  # define the subroutine/function user
    name = "yajmE Emjay"
    return f"This user is called: {name}"
print(anotherUser())
# or
secondUser = anotherUser()
print(secondUser)

def userName():  # define the subroutine userName
    name = input("What is your name? ")
    address = input("What is your address? ")
    interest = input("What is your interest? ")
    return name, address, interest

print(userName())
print(userName()[0])
print(userName()[1])
print(userName()[2])
print(f"{userName()[1]} is where {userName()[0]} host the {userName()[2]} bootcamp")
# or
userDetails = userName()
print(userDetails[0])
print(userDetails[1])
print(userDetails[2])
print(f"The {userDetails[2]} bootcamp organised by {userDetails[0]} is at {userDetails[1]}")
# create function use return statement with parameters and arguments
def addition():  # defines the addition function
    # variables inside a  surbroutine/function have local scope

# prevents the automatic running of the subroutine when it is imported
# in to another python file/application

#If this file is run directly it will automatically call and run the respective subroutines
# if __name__ == "__main__":
#     # call/invoke the subroutine

#     # call/invoke the subroutine
#     print(f"Method 2\nYour username is {}")

#     # call/invoke the functioneName
#     "Method 1"

#     print(f"Method 2\nThe answer is {}")

#     "Method 2"
#     num1 = 10#int(input("Enter your first number: "))
#     num2 = 20#int(input("Enter your second number: "))

#     # Assigned the function to the variable myAddition
#     print(f"Method 2\nThe answer is {}")


#     print(f"Your answer to {} + {} is {}")