from connect import *
 
# Create a subroutine
def read_films():
    try:  
        # Select all records from the table
        # Fetchall(): Fetches all the the selected records
        rows = dbCursor.execute("SELECT * FROM tblFilms").fetchall() # Row holds all fetched records       
 
        if not rows: # Row is the record returned based on the specific MemberID
            print(f"No record(s) exists")
        # Loop through all the records in the row variable
        else:
            for aRecord in rows:
                # Print all record
                print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    read_films()