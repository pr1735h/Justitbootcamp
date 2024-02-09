from connect import *

# Create a subroutine;
def insert_members():
    # Create an empty list:
    members = []
    # Ask for user input (MemberID, Firstname, Lastname and Email)
    # MemberID is an auto increment field and does not require an input.
    fName = input("Enter Firstname: ")
    lName = input("Enter Lastname: ")
    email = input("Enter Email: ")
    print(f"Data: {fName, lName, email}")
    # Append data Firstname, Lastname and Email:
    members.append(fName)
    members.append(lName)
    members.append(email)
    print(f"The members list {members}")

    "INSERT INTO members VALUES(NULL, 'A', 'B', 'C')"
    "INSERT INTO members (Firstname, Lastname, Email) VALUES(NULL, 'A', 'B', 'C')"

    try:
        # dbCursor.execute("INSERT INTO members VALUES(NULL, ?,?,?)", members) # Values from the list
        # Or values directly from variables.
        # dbCursor.execute("INSERT INTO members VALUES(NULL, ?,?,?)", (fName, lName, email))
        dbCursor.execute("INSERT INTO members (Firstname, Lastname, Email) VALUES(?,?,?)", (fName, lName, email))
        dbCon.commit() # Make the changes permanent
        print(f"{fName} inserted in the table")
    except sql.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed {e}")

if __name__== "__main__":
    insert_members()