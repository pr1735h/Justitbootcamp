from datetime import date

ticketPrice = [20, 12, 11]
ticketSelection = [0, 0, 0]
parkingRequired = False

def message():
    print("Welcome to Adventure Park!")
    print(f"Ticket prices are Adults: £{ticketPrice[0]}, Children: £{ticketPrice[1]}, Seniors: £{ticketPrice[2]}")
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    return firstName, lastName

def tickets():
    while True:
        try:
            adults = int(input("How many Adult tickets do you require? "))
            if 0 <= adults <=30:
                ticketSelection[0] = adults
            else:
                print("You can buy up to 30 tickets of each type. Please enter a valid number.")
                continue

            child = int(input("How many Child tickets do you require? "))
            if 0 <= child <=30:
                ticketSelection[1] = child
            else:
                print("You can buy up to 30 tickets of each type. Please enter a valid number.")
                continue

            senior = int(input("How many Senior tickets do you require? "))
            if 0 <= senior <=30:
                ticketSelection[2] = senior
            else:
                print("You can buy up to 30 tickets of each type. Please enter a valid number.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def parking():
    global parkingRequired
    userInput = input("Do you require a parking pass? ")
    parkingRequired = userInput.lower() in ['true', '1', 't', 'y', 'yes']

def totalTickets():
    result = [ticketPrice[i]*ticketSelection[i] for i in range(len(ticketPrice))]
    total = sum(result)
    return total

def finalTicket():
    global firstName, lastName
    firstName, lastName = message()
    tickets()
    parking()
    if parkingRequired == True:
        print(f"Parking Ticket for Adventure Park")
    print(f"Ticket valid for {lastName}")
    total = totalTickets()
    print(f"The total cost is: £{total}")
    today = date.today()
    print(today)

def thanks():
    print(f"Thank you for your purchase, {firstName} {lastName}!")

finalTicket()
thanks()