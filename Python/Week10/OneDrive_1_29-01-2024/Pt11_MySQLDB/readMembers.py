from connect import *

# Create a subroutine
def read_members():
    try:
        # Execute the SQL query
        dbCursor.execute("SELECT * FROM members")
        rows = dbCursor.fetchall()  # Fetch all records

        if not rows:
            print("No records exist.")
        else:
            for aRecord in rows:
                print(aRecord)
    except mysql.connector.OperationalError as e:
        print(f"Error fetching records: {e}")

if __name__ == "__main__":
    read_members()