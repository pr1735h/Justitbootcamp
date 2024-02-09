import mysql.connector

dbCon = mysql.connector.connect(host = "localhost", user = "root", database = "c9w4songs", password = "Fatpoop-123")



dbCursor = dbCon.cursor