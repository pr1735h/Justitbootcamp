import readMembers, addMembers, updateMembers, deleteMembers, searchReport
 
def read_file():
    try:
        with open("Week10/OneDrive_1_29-01-2024/Pt9_10DBOps/menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")
 
# Create the menu function
def members_menu():
    option = 0 # initialise the option variable with an integer value
    optionsList = ["1","2","3","4","5","6"]
 
    # Assign the  read_file() function to the menuChoices variable
    menuChoices =  read_file()
 
    # Create a while loop to repeat the code within the bod of while condition
    while option not in optionsList:
        print(menuChoices) # call/invoke read_file() function to the menuChoices variable
 
        # Re-assign the value of the option variable with the input function
        option = input("Enter an option from the Menu choice above: ")
 
        # Check if the input from the option variable match any of the options
        # In the optionsList(["1","2","3","4","5","6"])
        if option not in optionsList:
            # If the condition above is true execute the code below
            print(f"{option} is not a valid choice! ")
    return option
 
 
mainProgram = True # Boolean variabe to toggle True/False
 
while mainProgram: # While True
    # Assign the members_menu() function to the mainMenu variable
    mainMenu = members_menu()
   
    # Use match case
    match mainMenu:
        case "1": # If case value equals/matches the string value 1 then
            readMembers.read_members() # Call the read_members()  from the readMembers.py file imported at the top
        case "2":
            addMembers.insert_members()
        case "3":
            updateMembers.update_members()
        case "4":
            deleteMembers.delete_members()
        case "5":
            searchReport.search()
        case _:
            # Reassign the value of mainprogram to False
            mainProgram = False
input("Press Enter key to exit the program: ")