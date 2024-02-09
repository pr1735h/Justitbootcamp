-- To show databases
SHOW DATABASES;

-- CRUD: Create Read Update Delete
-- CREATE to create a database
-- CREATE DATABASE DBNAME;
-- CREATE DATABASE C9W4;


-- To use a database 
USE C9W4;
-- To check database in use
SELECT DATABASE();

-- To clear screen
-- Windows Users
-- \! cls;

-- Mac Users
-- CMD + ALT + L

-- TO CREATE A TABLE IN A DATABASE

CREATE TABLE courseTest (
CourseID INT NOT NULL,
CourseName VARCHAR(50) NOT NULL,
LearnerID INT NOT NULL,
LearnerName VARCHAR(50) NOT NULL,
TrainerID INT NOT NULL,
TrainerName VARCHAR(60) NOT NULL,
PRIMARY KEY(CourseID));


-- To see the table structure 
-- DESC COURSE;
EXPLAIN courseTest;

-- To Insert Data in a table
-- Method 1
courseINSERT INTO courseTest(CourseID,CourseName,LearnerID,
LearnerName,TrainerID,TrainerName)
VALUES(101,'MySQL',501,'Jane Doe',1001,'Tim Jones');

-- Method 2
INSERT INTO courseTest
VALUES(102,'NoSQL',502,'John Doe',1002,'Zak Perdis');

-- To Display all records in a table
SELECT * FROM courseTest;

-- To Display a specific record in a table
SELECT * FROM courseTest WHERE CourseID = 102;