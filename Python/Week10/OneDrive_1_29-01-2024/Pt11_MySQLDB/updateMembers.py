from connect import *

# Create a subroutine:
def update_members():
    # Use MemberID, which is a primary key and a unique field, to update a record.
    # The ID of the record to be updated.
    idField = input("Enter the MemberID to update a record: ")

    # The field selected for the update.
    fieldName = input("Enter the field (Firstname or Lastname or Email) to update: ").title()

    # The value to be entered in the field.
    fieldValue = input(f"Enter the value for the {fieldName}: ")

    # Add quotes to field value
    fieldValue = f"'{fieldValue}'"

    try:
        # Check if the MemberID exists
        dbCursor.execute(f"SELECT MemberID FROM members WHERE MemberID = {idField}")
        existing_member = dbCursor.fetchone()

        if existing_member:
            # MemberID exists, proceed with the update
            dbCursor.execute(f"UPDATE members SET {fieldName} = {fieldValue} WHERE MemberID = {idField}")
            dbCon.commit()
            print(f"{idField} updated in the members table")
        else:
            print(f"Error: MemberID {idField} does not exist.")
    except mysql.connector.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_members()