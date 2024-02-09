from connect import *
import logging
import time

filename = __file__

logging.basicConfig(filename=r"PyProject\DbOpsFile.log", level=logging.DEBUG)

# create a subroutine
def search():
    try:
        field = input("Would you like to search by filmID, title, yearReleased, rating, duration, or genre? ")
        if field == "filmID":
            idInput = input("Enter filmID: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}")
            row = dbCursor.fetchone()
            if row is None:
                print(f"No record with {idInput} exists in the table.")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {idInput} as {field}")
            else:
                for aRecord in row:
                    print(aRecord)
        elif field in ["title", "yearReleased", "rating", "duration", "genre"]:
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if not rows:  # Check if the list is empty
                print(f"No record with field {field} matching '{searchInput}' in the table.")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search field: {field}")
    except sql.OperationalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search()