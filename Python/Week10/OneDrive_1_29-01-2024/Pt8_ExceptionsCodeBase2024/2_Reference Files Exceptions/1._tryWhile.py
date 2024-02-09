checkNum = True  # allows to toggle bewetween True/False

while checkNum: # while True
    try:
        num1 = int(input(("Enter  a number: ")))
    # break out of the loop 
        checkNum = False  # reassign the value of checkNum to False
    except ValueError:
        print("You must enter a number")

    finally:
        print("closing.....")
print("You entered an integer value")