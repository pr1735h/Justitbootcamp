USE leisurecentre;
SELECT * FROM course;
SELECT * FROM members;
SELECT * FROM lessons;
-- Use the SQL AND, OR and NOT Operators in your query (The WHERE clause can be combined with AND, OR, and NOT operators)
-- Where courseID is equals to a number below 5 and the first name of any of the instructors
SELECT * FROM course WHERE courseID < 5 AND instructor = "Amelia";
-- Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.
SELECT * FROM course WHERE courseID > 5 AND NOT sessions = "Evening";
-- Order by the above results by:
-- startDate in “course” table
SELECT * FROM course ORDER BY startDate;
SELECT * FROM course ORDER BY startDate DESC;
-- MemberID in “members” table 
SELECT * FROM members ORDER BY memberID;
SELECT * FROM members ORDER BY memberID DESC;

-- UPDATE the following:
-- Members table, change the addresses of any three members.
UPDATE members SET address = "64 Zoo Lane" WHERE memberID = "4";
UPDATE members SET address = "10 Downing Street" WHERE memberID = "7";
UPDATE members SET address = "St. Clare House 30-33 Minories" WHERE memberID = "9";
-- Course table, change the startDate and lesson time for three of the sessions.
UPDATE course SET startDate = "2023-05-11", lessonTime = "13:00" WHERE courseID = "4";
UPDATE course SET startDate = "2023-01-11", lessonTime = "13:30" WHERE courseID = "7";
UPDATE course SET startDate = "2023-09-27", lessonTime = "14:00" WHERE courseID = "13";

-- Use the SQL MIN () and MAX () Functions to return the smallest and largest value
-- Of the LessonID column in the “lesson” table
SELECT MIN(lessonID) FROM lessons;
SELECT MAX(lessonID) FROM lessons;
-- Of the membersID column in the “members” table
SELECT MIN(memberID) FROM members;
SELECT MAX(memberID) FROM members;
-- Use the SQL COUNT (), AVG () and SUM () Functions for these:
-- Count the total number of members in the “members” table
SELECT COUNT(*) FROM members;
-- Count the total number of sessions in the” members” table
SELECT SUM(lessonID) FROM lessons;
-- Find the average session time for all “sessions” in course table
SELECT AVG(lessonTime) FROM course;

-- WILDCARD queries (like operator)
-- Find all the people from the “members” table whose last name starts with A.
SELECT * FROM members WHERE surname LIKE "A%";
-- Find all the people from the “members” table whose last name ends with A.
SELECT * FROM members WHERE surname LIKE "%A";
-- Find all the people from the “members” table that have "ab" in any position in the last name.
SELECT * FROM members WHERE surname LIKE "%ab%";
SELECT * FROM members WHERE surname LIKE "%ll%";
-- Find all the people from the “members” table that that have "b" in the second position in their first name.
SELECT * FROM members WHERE firstname LIKE "_b%";
SELECT * FROM members WHERE firstname LIKE "_l%";
-- Find all the people from the “members” table whose last name starts with "a" and are at least 3 characters in length:
SELECT * FROM members WHERE surname LIKE "a__%";
SELECT * FROM members WHERE surname LIKE "m__%";
-- Find all the people from the “members” table whose last name starts with "a" and ends with "y"
SELECT * FROM members WHERE surname LIKE "a%y";
SELECT * FROM members WHERE surname LIKE "m%y";
-- Find all the people from the “members” table whose last name does not starts with "a" and ends with "y" 
SELECT * FROM members WHERE surname NOT LIKE "a%y";
SELECT * FROM members WHERE surname NOT LIKE "m%y";

-- What do you understand by LEFT and RIGHT join? Explain with an example.
-- Joins are used two combine rows from multiple tables with a related column from all tables used.
-- This is useful when multiple tables have data for one entity like a customer and you want to compare, analyse or export specific fields.
-- LEFT and RIGHT JOIN take specified columns from one table and combine them with the specified columns from other tables.
-- If there are no matches the result will be displayed as "NULL".
SELECT course.level, course.sessions, members.firstname FROM course LEFT JOIN members ON course.courseID = members.memberID;
SELECT c.level, c.sessions, m.firstname FROM course AS c LEFT JOIN members AS m ON c.courseID = m.memberID;
SELECT course.level, course.sessions, lessons.lessonID FROM course RIGHT JOIN lessons ON course.courseID = lessons.courseID;
SELECT c.level, c.sessions, l.lessonID FROM course AS c RIGHT JOIN lessons AS l ON c.courseID = l.courseID;


