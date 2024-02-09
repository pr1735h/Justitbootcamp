from connect import *

# Create a subroutine:
def delete_members():
    try:
        # Use MemberID, which is a primary key and a unique field, to delete a record.
        # The ID of the record to be deleted.
        idField = input("Enter the MemberID to delete a record: ")

        # Select a record using a MemberID from the table.
        dbCursor.execute(f"SELECT * FROM members WHERE MemberID = {idField}")

        row = dbCursor.fetchone() # Use the fetchone() to fetch the selected record
        # None: A singleton object used to check/signal if a value is absent

        if row == None: # Row is the record returned based on the specified MemberID
            print(f"No record with the MemberID {idField} exists")

        else:
            dbCursor.execute(f"DELETE FROM members WHERE MemberID = {idField}")
            dbCon.commit()

    except mysql.connector.OperationalError as e:
        print(f"No Database or table found: {e}")

if __name__=="__main__":
    delete_members()