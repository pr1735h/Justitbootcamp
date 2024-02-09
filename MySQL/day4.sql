-- CRUD Relational Table: Create Read Update Delete(Trainer Demo)
EXPLAIN songs;
-- More Basic Queries (Trainer Demo)
 
-- The SQL 'AND', 'OR' and 'NOT' Operators (Trainer Demo)
--  SQL AND operator:
-- Combines multiple conditions that must both be met for the query to be returned:
SELECT * FROM songs;
SELECT * FROM songs WHERE Artist = "Led Zeppelin" AND Genre = "blues";
SELECT * FROM songs WHERE Artist = "Drake" AND Title = "Sweet Child o' Mine";
SELECT * FROM songs WHERE Title = "Imagine" AND Artist = "Outkast";

-- SQL OR operator:
-- Combines multiple conditions that must be met for the query to be returned:
SELECT * FROM songs WHERE Artist = "Led Zeppelin" OR Genre = "blues";
SELECT * FROM songs WHERE Title = "Thriller" OR Genre = "rap";

-- SQL NOT operator:
-- Excludes what to exclude from a query:
SELECT * FROM songs WHERE NOT Artist = "Radiohead";

-- Combining multiple operators:
SELECT * FROM songs WHERE NOT Artist = "Radiohead" AND NOT Genre = "folk";
SELECT * FROM songs WHERE Artist = "Radiohead" AND (Genre = "rock" OR Genre = "punk");

-- Order by (ASC/DESC)
SELECT * FROM songs ORDER BY SongID DESC;
SELECT * FROM songs ORDER BY Artist ASC;
SELECT * FROM songs WHERE Artist = "Radiohead" ORDER BY Genre ASC;

-- Task 1:
SELECT * FROM members;
SELECT * FROM members WHERE Firstname = "Kristi" AND Lastname = "Batalle";
SELECT * FROM members WHERE Firstname = "Kristi" AND Lastname = "Batalle" OR MemberID = "7";
SELECT * FROM songs WHERE Artist = "Radiohead" AND (Genre = "rock" OR Genre = "punk" OR Genre = "hip hop") ORDER BY SongID ASC;

-- SQL MIN() and MAX() Functions:
SELECT * FROM downloads;
SELECT MIN(Date) FROM downloads;
SELECT MAX(Date) FROM downloads;
SELECT MAX(Date) AS LastDownload FROM downloads;

-- SQL COUNT functions:
-- You can ignore duplicates by using the DISTINCT keyword in the COUNT function.
-- If DISTINCT is specified, rows with the same value for the specified column will be counted as one.
SELECT Count(*) FROM songs;
SELECT COUNT(DownloadID) FROM downloads WHERE Date > '2021-04-06';
SELECT COUNT(DISTINCT SongID) FROM downloads;
SELECT COUNT(*) AS "Total blues and country songs" FROM songs WHERE Genre = "blues" OR Genre = "country";

-- SQL Sum function:
-- The SUM() function returns the total sum of a numeric column.
SELECT SUM(SongID) FROM songs;
-- You can add a WHERE clause to specify conditions:
SELECT SUM(SongID) FROM songs WHERE Genre = "punk";

-- SQL AVG() Function:
-- The AVG() function returns the average value of a numeric column.
SELECT AVG(SongID) FROM downloads;
-- You can add a WHERE clause to specify conditions:
SELECT AVG(MemberID) FROM downloads WHERE SongID = 29;
-- Give the AVG column a name by using the AS keyword.
SELECT AVG(SongID) AS AverageSongID from downloads;

-- The Limit syntax, fetch and display ,1,2,3,4..etc number of records.
-- Returns the top 5 records:
SELECT * FROM members LIMIT 5; 
-- Specify the record to start from:
SELECT * FROM members LIMIT 5, 10;
SELECT * FROM members WHERE MemberID > 22 LIMIT 20;
SELECT * FROM members WHERE MemberID > 22 AND NOT MemberID = "38" LIMIT 20;

-- ALIAS : Rename a column or table temporarily
SELECT Genre AS "Genre" FROM songs;
SELECT * FROM songs;

-- The SQL LIKE function:
-- Searches a field/column for pattern
-- % represents zero, one or multiple characters, underscore _ , represents a single character.
SELECT * FROM songs WHERE Artist LIKE 'm%';    -- Start with m
SELECT * FROM songs WHERE Artist LIKE '%z';    -- Ends with z
SELECT * FROM songs WHERE Artist LIKE '%e%';   -- Has e in any position
SELECT * FROM songs WHERE Genre LIKE 'c%' or Genre LIKE "%op";

-- Task 2:
SELECT * FROM members WHERE Lastname LIKE "b%";
SELECT * FROM members WHERE Lastname LIKE "%n";
SELECT * FROM members WHERE Firstname LIKE "a%a";
SELECT * FROM members WHERE Firstname LIKE "a%a" OR Lastname LIKE "a%";
SELECT * FROM members WHERE Firstname LIKE '%a%' AND Lastname LIKE "%a%";

-- Underscore wildcard:
SELECT * FROM songs WHERE Title LIKE "He_%";
SELECT * FROM songs WHERE Genre LIKE "__p";
SELECT * FROM songs WHERE Genre LIKE "r_p";
SELECT * FROM songs WHERE Genre LIKE "r_p" AND NOT Title LIKE "l%";
SELECT * FROM songs WHERE Genre LIKE "__p" AND Title LIKE "l%";
SELECT * FROM songs WHERE Genre LIKE "_l%";
SELECT * FROM songs WHERE Genre NOT LIKE "_l%" AND Genre NOT LIKE "%__p";



