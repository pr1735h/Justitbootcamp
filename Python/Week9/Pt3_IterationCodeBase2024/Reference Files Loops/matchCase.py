# Read though the code below:

# 1. Identify any programming language that uses similar syntax
"JavaScript uses the 'switch(expression), case, statement, break' syntax, which is very similar to match-case in Python."
"The main differences are in how the code blocks are displayed in each language and the keywords used to describe statements."
# 2. Explain and comment as many lines to demonstrate understanding
# 3. Use the example below to write your own days in the week program

import random # Imports the "random" library.

weeks = ["wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8", "wk9", "wk10", "wk11", "wk12"] # The "weeks" variable has an index list.
aWeek = random.choice(weeks) # This variable uses the imported random function to get one index from "weeks".
print(aWeek) # Prints the random value.

match aWeek: # Looks for a match from the variable "aWeek" in the statement:
    case "wk1": # If this case is a match (if aWeek is equal to "wk1") then:
        print("Welcome to SDLC.") # Print this message, if not then look at the next case for a match.
    case "wk2":
        print("Welcome HTML.")
    case "wk3":
        print("Welcome to CSS.")
    case "wk4":
        print("Still CSS week.")
    case "wk5":
        print("Welcome to JavaScript.")
    case "wk6":
        print("Welcome JavaScript project.")
    case "wk7":
        print("Welcome to Database.")
    case "wk8":
        print("Still database week.")
    case "wk9":
        print("Welcome Python .")
    case "wk10":
        print("Still Python week.")
    case "wk11":
        print("Welcome Python Project week.")
    case "wk12":
        cohortName = input("Enter cohort name: ")
        if cohortName == "Man":
            print("Microsoft Azure week.")
        else:
            print("Portfolio week.")
    # In the last case block, we defined case _, where the variable 
    # name _ acts as a wildcard and it will never fail to match.
    # If no case matches in the upper code then the last case block is executed.
    case _:
        print("Matches anything.")

        # https://geekpython.in/match-case-in-python

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ranDay = random.choice(days)
print(ranDay)
match ranDay:
    case "Monday":
        print(f"Today is {ranDay}")
    case "Tuesday":
        print(f"Today is {ranDay}")
    case "Wednesday":
        print(f"Today is {ranDay}")
    case "Thursday":
        print(f"Today is {ranDay}")
    case "Friday":
        print(f"Today is {ranDay}")
    case "Saturday":
        print(f"Today is {ranDay}")
    case "Sunday":
        print(f"Today is {ranDay}")