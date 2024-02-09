-- JOINS:
-- INNER JOIN two tables:
-- Members and downloads tables:
SELECT downloads.MemberID, downloads.Date, members.Firstname, members.Email FROM downloads INNER JOIN  members ON downloads.MemberID = members.MemberID;
-- Songs and downloads tables:
SELECT downloads.MemberID, downloads.Date, songs.Title, songs.Artist FROM downloads INNER JOIN songs ON downloads.SongID = songs.SongID;
-- Three tables:
SELECT downloads.MemberID, downloads.Date, members.Firstname,members.Email,members.Lastname, songs.Title, songs.Artist,songs.SongID 
FROM ((downloads INNER JOIN members ON downloads.MemberID = members.MemberID) INNER JOIN songs ON downloads.SongID = songs.SongID);

-- JOIN Two Tables:
-- members and downloads
SELECT downloads.MemberID, downloads.Date, members.Firstname,members.Email, members.Lastname FROM downloads JOIN members ON downloads.MemberID = members.MemberID;
-- Songs and downloads
SELECT downloads.MemberID, downloads.Date, songs.Title, songs.Artist, songs.SongID FROM downloads JOIN songs ON downloads.SongID = songs.SongID;
-- Members, Songs and Downloads
SELECT downloads.MemberID, downloads.Date, members.Firstname,members.Email,members.Lastname, songs.Title, songs.Artist,songs.SongID
FROM((downloads JOIN members ON downloads.MemberID = members.MemberID) JOIN songs ON downloads.SongID = songs.SongID);

-- LEFT JOIN:
-- members and downloads
SELECT * FROM downloads LEFT JOIN members ON downloads.MemberID = members.MemberID;
SELECT * FROM members LEFT JOIN downloads ON downloads.MemberID = members.MemberID;
-- Members, Songs and Downloads
SELECT * FROM ((downloads LEFT JOIN members ON downloads.MemberID = members.MemberID) LEFT JOIN songs ON downloads.SongID = songs.SongID);
SELECT * FROM ((members LEFT JOIN downloads ON downloads.MemberID = members.MemberID) LEFT JOIN songs ON downloads.SongID = songs.SongID);
-- RIGHT JOIN:
-- members and downloads
SELECT * FROM downloads RIGHT JOIN members ON downloads.MemberID = members.MemberID;
SELECT * FROM members RIGHT JOIN downloads ON downloads.MemberID = members.MemberID;
-- Members, Songs and Downloads
SELECT * FROM ((downloads RIGHT JOIN members ON downloads.MemberID = members.MemberID) RIGHT JOIN songs ON downloads.SongID = songs.SongID);
SELECT * FROM ((songs RIGHT JOIN downloads ON songs.SongID = downloads.DownloadID) RIGHT JOIN members ON downloads.SongID = songs.SongID);

-- MySQL UNION:
-- The UNION operator is used to combine the result-set of two or more SELECT statements.
-- Every SELECT statement within UNION must have the same number of columns
-- The columns must also have similar data types
-- The columns in every SELECT statement must also be in the same order
SELECT * FROM downloads;
SELECT * FROM songs;
SELECT * FROM members;
SELECT * FROM downloads UNION SELECT * FROM songs UNION SELECT * FROM members;
SELECT * FROM members JOIN downloads ON downloads.MemberID = members.MemberID UNION SELECT * FROM songs JOIN downloads ON downloads.SongID = songs.SongID;

-- USING Keyword is another method of writing the ON clause
SELECT m.Firstname, m.Email, s.Title, s.Artist, d.Date FROM members m JOIN downloads d USING(MemberID) JOIN songs s USING(SongID);

-- Functions/Stored Procedure (Variables, Parameters)
DELIMITER $$
CREATE PROCEDURE `findSong`(IN p_SongID int) BEGIN SELECT * FROM songs WHERE SongID = p_SongID;
END$$
DELIMITER $$
-- Call functions/stored Procedure 
call findSong(14);

-- stored procedure with two parameters
DELIMITER $$
CREATE PROCEDURE `updateArtist`(IN parameterS int, parameterArtist varchar(60)) BEGIN UPDATE songs SET Artist = parameterArtist WHERE SongID = parameterS;
END$$
DELIMITER $$
-- Call functions/stored Procedure 
call updateArtist(1, "Uvuvwevwe Osas");

-- CREATE VIEW: a Tempoary table with no relationship
CREATE VIEW Members_Downloads AS SELECT * FROM members JOIN downloads USING(MemberID);
-- Use/call the view:
SELECT * FROM members_downloads;







