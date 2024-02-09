import sqlite3 as sql # Import the standard SQLite3 module

try:
    # To use the module, start by creating a database connection object (variable to hold the folder/file).
    # Using the connect method from the SQLite3 module.
    with sql.connect("PyProject/filmflix.db") as dbCon:
        # Once the connection and/or dbfile is created,
        # Create a cursor object(variable) called dbCursor and call it cursor method.
        dbCursor = dbCon.cursor() # Used to execute SQL statements.

except sql.OperationalError as e: # Raise SQL error.
    # Handle the exception/error raised.
    print(f"Connection failed: {e}")