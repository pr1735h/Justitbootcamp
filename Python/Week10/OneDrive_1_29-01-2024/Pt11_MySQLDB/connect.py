import mysql.connector

dbCon = mysql.connector.connect(host = "localhost", user = "root", database = "c9w4songs", password = "Fatpoop-123")


# Report whether the connection to MySQL server is available/successful
if dbCon.is_connected():
    print("Connected to MySQL")
else: 
    print("Connection failed!")

dbCursor = dbCon.cursor(prepared=True)