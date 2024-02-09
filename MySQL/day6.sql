-- SQL String Functions.
-- substring:
SELECT * FROM members;
SELECT SUBSTRING("Today is Monday", 1);
SELECT SUBSTRING("Today is Monday", 3);
SELECT SUBSTRING("Today is Monday", 3, 10);
SELECT SUBSTRING(Email, 3) FROM members;
SELECT SUBSTRING(Email, 1, 19) FROM members;
-- Task:
SELECT * FROM songs;
SELECT SUBSTRING(Title, 3) FROM songs;
SELECT SUBSTRING(Title, 3, 18) FROM songs;
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Concat:
-- The CONCAT() function adds two or more expressions together.
SELECT * FROM members;
SELECT CONCAT(Firstname, " ", Lastname) FROM members;
SELECT CONCAT(Firstname, " ", Lastname) AS "Fullname" FROM members;
SELECT CONCAT(Firstname, " ", Email) AS "First name and Email" FROM members;
SELECT CONCAT(Firstname, " ", Lastname, " ", Email) FROM members;
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SELECT * FROM songs;
SELECT * FROM downloads;
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- SQL Aliases:
-- SQL aliases are used to give a table, or a column in a table, a temporary name.
-- Aliases are often used to make column names more readable, only exists for the duration of that query and is created with the AS keyword.
SELECT * FROM members;
SELECT * FROM members WHERE MemberID IN (SELECT MemberID FROM downloads);
SELECT  d.MemberID, d.Date, m.Firstname FROM members AS m, downloads AS d WHERE m.Firstname LIKE "%e" AND m.MemberID = d.MemberID;
SELECT m.Firstname, d.Date FROM members AS m, downloads AS d WHERE m.Firstname LIKE "%n" AND d.Date > '2020-12-12';
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- CASE Expression and CASE Statements:
-- The CASE expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement). If a condition is true, it will stop reading and return the result.
-- If no conditions are true, it returns the value in the ELSE clause. If there is no ELSE part and no conditions are true, it returns NULL.
UPDATE members SET Lastname = (CASE MemberID
WHEN 5 THEN "Eater"
WHEN 39 THEN "Full"
WHEN 43 THEN "E"
END) WHERE MemberID IN(5, 39, 43);
SELECT * FROM members WHERE MemberID IN(5, 39, 43);
-- Task:
UPDATE songs SET Artist = (CASE SongID
WHEN 5 THEN "Oasis"
WHEN 39 THEN "Nirvana"
WHEN 43 THEN "Led Zeppelin"
END) WHERE SongID IN(5, 39, 43);
SELECT * FROM songs WHERE SongID IN(5, 39, 43);
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- SQL SELECT DISTINCT:
-- Used to return only distinct (different) values.
SELECT DISTINCT SongID AS "Downloaded Once" FROM downloads;
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- GROUP CONCAT:
SELECT Artist, COUNT(SongID) AS "Total Songs", GROUP_CONCAT(SongID ORDER BY Artist DESC) AS "All Song ID's" FROM songs GROUP BY Artist;









