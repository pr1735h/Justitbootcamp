-- SQL IN and NOT IN operators:
-- The IN operator:
-- Used when you want to select more than one value or query.
SELECT * FROM songs WHERE Genre IN("rock", "blues");
SELECT * FROM songs WHERE Artist IN("Drake", "Jay-Z", "Coldplay");
SELECT * FROM songs WHERE Genre IN("rock", "blues") OR Artist IN("Drake", "Jay-Z", "Coldplay");
-- The NOT IN operator:
SELECT * FROM songs WHERE Genre NOT IN("rock", "blues");
SELECT * FROM songs WHERE Genre NOT IN("rock", "blues") AND Artist NOT IN("Drake", "Jay-Z", "Coldplay");

-- The SQL Between Operator:
-- Used when you want to select values in or out of a specified range or ranges.
SELECT * FROM songs WHERE SongID BETWEEN 10 AND 20;
-- BETWEEN and IN operators:
SELECT * FROM songs WHERE SongID BETWEEN 10 AND 30 AND Genre IN("rock", "blues", "rap");
-- BETWEEN and NOT operators:
SELECT * FROM songs WHERE SongID NOT BETWEEN 10 AND 20;

-- Task 1d:
SELECT * FROM downloads WHERE DownloadID BETWEEN 3 AND 9;

-- Nested queries:
SELECT * FROM members;
SELECT * FROM downloads;
SELECT * FROM members WHERE MemberID IN(SELECT MemberID FROM downloads);
SELECT * FROM downloads WHERE SongID IN(SELECT SongID FROM songs);

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CREATE TABLE test(
userid INT NOT NULL,
fullname VARCHAR(60) NOT NULL,
address VARCHAR(100) NOT NULL
);
INSERT INTO test VALUES(1, "aa", "bb"), (2, "ab", "bc"), (3, "dd", "ee");
CREATE TABLE test1(
userid INT NOT NULL,
fullname VARCHAR(60) NOT NULL,
address VARCHAR(100) NOT NULL
);
INSERT INTO test1 VALUES(1, "aa", "bb"), (2, "ab", "bc"), (3, "dd", "ee");
-- Alter command:
-- Used to permanantly modify tables in various ways.
ALTER TABLE test RENAME COLUMN address TO userdata;
ALTER TABLE test 

-- Truncate:
-- Permanantly deletes all data from table but keeps it's structure.
TRUNCATE TABLE test;

-- Drop:
-- Deletes the entire table from the database.
DROP TABLE test;

-- Delete:
-- Used to delete one or more rows from a table. Can be rolled back.
DELETE FROM test;

-- Group by:
SELECT * FROM songs;
SELECT Artist, COUNT(Genre) FROM songs GROUP BY Artist;





