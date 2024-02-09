-- CRUD: Create, Read, Update, Delete.
-- use c9w4;
-- show tables;
-- INSERT INTO COURSE
-- VALUES(103,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (104,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (105,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (106,'NoSQL',502,'John Doe',1002,'Zak Perdis');

-- How to update the table and ignore duplicate entries
-- The script won't update without "ignore" if there are duplicate entries!
-- insert ignore into course
-- values(102,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (103,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (104,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (107,'NoSQL',502,'John Doe',1002,'Zak Perdis');

-- How to update a record:
-- update course set TrainerName = "Chris Perry" where CourseID = 106;
-- update course set CourseName = "MySQL";
-- update course set TrainerID = "1003" where TrainerName = "Chris Perry";

-- How to delete a record
-- DELETE FROM COURSE WHERE CourseID = 107;



-- Task 1:

-- INSERT ignore INTO COURSE
-- VALUES(110,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (111,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (112,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (113,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (114,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (115,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (116,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (117,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (118,'NoSQL',502,'John Doe',1002,'Zak Perdis'),
-- (119,'NoSQL',502,'John Doe',1002,'Zak Perdis');

-- UPDATE course SET TrainerName = "Chris Perry" WHERE CourseID IN (111,112,113,114);
-- UPDATE course SET LearnerName = "Pritesh Hirani" WHERE CourseID = 111;
-- select * from course;

alter table course rename column LearnerName to StudentName;