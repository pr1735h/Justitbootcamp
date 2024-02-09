from connect import *

# Create a subroutine:
def update_members():
    # Use MemberID, which is a primary key and a unique field, to update a record.
    # The ID of the record to be updated.
    idField = input("Enter the MemberID to update a record: ")

    # Select all fields for update.
    fName = input("Enter Firstname: ").title()
    lName = input("Enter Lastname: ").title()
    email = input("Enter Email: ")

    # Add quotes to field value
    fName = "'" + fName + "'"
    lName = "'" + lName + "'"
    email = "'" + email + "'"

    try:
        # Check if the MemberID exists
        dbCursor.execute(f"SELECT MemberID FROM members WHERE MemberID = {idField}")
        existing_member = dbCursor.fetchone()

        if existing_member:
            # MemberID exists, proceed with the update
            dbCursor.execute(f"UPDATE members SET Firstname = {fName}, Lastname = {lName}, Email = {email} WHERE MemberID = {idField}")
            dbCon.commit()
            print(f"{idField} updated in the members table")
        else:
            print(f"Error: MemberID {idField} does not exist.")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_members()
