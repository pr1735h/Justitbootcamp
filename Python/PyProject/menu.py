import readFilms
import addFilm
import updateFilm
import deleteFilm
import searchReport

def read_file():
    try:
        with open("PyProject/menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")

# Create the menu function
def films_menu():
    option = 0  # Initialize the option variable with an integer value
    optionsList = ["1", "2", "3", "4", "5", "6"]

    # Assign the read_file() function to the menuChoices variable
    menuChoices = read_file()

    # Create a while loop to repeat the code within the body of the while condition
    while option not in optionsList:
        print(menuChoices)  # Call/invoke read_file() function to the menuChoices variable

        # Re-assign the value of the option variable with the input function
        option = input("Enter an option from the Menu choice above: ")

        # Check if the input from the option variable matches any of the options
        # In the optionsList(["1", "2", "3", "4", "5", "6"])
        if option not in optionsList:
            # If the condition above is true, execute the code below
            print(f"{option} is not a valid choice!")

    return option

mainProgram = True  # Boolean variable to toggle True/False

while mainProgram:  # While True
    # Assign the films_menu() function to the mainMenu variable
    mainMenu = films_menu()

    # Use match case
    match mainMenu:
        case "1":
            readFilms.read_films()
        case "2":
            addFilm.insert_films()
        case "3":
            updateFilm.update_films()
        case "4":
            deleteFilm.delete_film()
        case "5":
            searchReport.search()
        case _:
            mainProgram = False  # Reassign the value of mainProgram to False

input("Press Enter key to exit the program: ")
