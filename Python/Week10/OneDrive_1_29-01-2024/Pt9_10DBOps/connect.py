import sqlite3 as sql # Import the standard SQLite3 module

try:
    # To use the module, start by creating a database connection object (variable to hold the folder/file).
    # Using the connect method from the SQLite3 module.
    with sql.connect("Week10/OneDrive_1_29-01-2024/Pt9_10DBOps/dfe9w4.db") as dbCon:
        # Once the connection and/or dbfile is created,
        # Create a cursor object(variable) called dbCursor and call it cursor method.
        dbCursor = dbCon.cursor() # Used to execute SQL statements.

except sql.OperationalError as e: # Raise SQL error.
    # Handle the exception/error raised.
    print(f"Connection failed: {e}")