USE leisurecentre;

-- course table:
CREATE TABLE `leisurecentre`.`course` (
  `courseID` INT NOT NULL AUTO_INCREMENT,
  `level` VARCHAR(45) NOT NULL,
  `sessions` VARCHAR(45) NOT NULL,
  `instructor` VARCHAR(45) NOT NULL,
  `startDate` DATE NOT NULL,
  `lessonTime` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`courseID`));
DESC course;
SELECT * FROM course;

insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Evening', 'Charlotte', '2022-11-06', '14:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Mia', '2023-04-26', '11:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Afternoon', 'Ava', '2024-03-19', '16:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Amelia', '2023-05-10', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Evening', 'Charlotte', '2023-06-04', '15:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Sophia', '2023-12-15', '11:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Isabella', '2024-01-10', '13:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Evening', 'Ava', '2023-07-20', '14:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Isabella', '2024-04-01', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Charlotte', '2023-05-10', '11:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Ava', '2023-05-28', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Sophia', '2023-12-23', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Liam', '2023-09-27', '15:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Afternoon', 'Mia', '2024-03-19', '16:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Mia', '2023-12-09', '10:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Morning', 'Noah', '2023-12-01', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Liam', '2024-03-19', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Liam', '2023-04-19', '14:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Evening', 'Isabella', '2023-10-21', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Emma', '2023-10-11', '14:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Isabella', '2022-12-05', '10:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Isabella', '2023-12-17', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Sophia', '2023-06-11', '14:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Olivia', '2023-08-05', '16:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Morning', 'Mia', '2023-12-05', '10:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Noah', '2022-11-18', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Liam', '2023-01-08', '14:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Morning', 'Isabella', '2023-03-31', '11:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Morning', 'Charlotte', '2023-03-07', '15:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Morning', 'Olivia', '2023-01-01', '10:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Olivia', '2024-02-24', '11:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Sophia', '2023-02-22', '10:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Evening', 'Isabella', '2024-01-16', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Olivia', '2024-03-16', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Morning', 'Sophia', '2023-05-05', '14:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Afternoon', 'Liam', '2023-01-26', '13:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Emma', '2024-01-24', '14:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Evening', 'Mia', '2023-04-29', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Amelia', '2023-12-18', '15:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Olivia', '2023-11-30', '16:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Afternoon', 'Sophia', '2023-01-07', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Evening', 'Noah', '2023-04-26', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Morning', 'Noah', '2023-08-31', '14:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Morning', 'Sophia', '2023-06-01', '13:30');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Afternoon', 'Ava', '2022-12-03', '10:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Evening', 'Isabella', '2023-11-28', '15:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Evening', 'Olivia', '2023-03-26', '11:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Intermediate', 'Morning', 'Sophia', '2022-12-16', '13:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Advance', 'Evening', 'Charlotte', '2024-02-11', '10:00');
insert into course (level, sessions, instructor, startDate, lessonTime) values ('Beginner', 'Evening', 'Olivia', '2024-04-20', '15:00');
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- members table:
CREATE TABLE `leisurecentre`.`members` (
  `memberID` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(50) NOT NULL,
  `dob` DATE NOT NULL,
  `address` VARCHAR(50) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`memberID`));
DESC members;
SELECT * FROM members;

insert into members (firstname, surname, dob, address, city) values ('Lionello', 'Felder', '2023-08-05', 'Apt 1440', 'Yawata');
insert into members (firstname, surname, dob, address, city) values ('Alyda', 'Mahony', '2023-03-22', '2nd Floor', 'Qinggis Han');
insert into members (firstname, surname, dob, address, city) values ('Blisse', 'MacGorley', '2023-03-23', 'Suite 93', 'Ditsaan');
insert into members (firstname, surname, dob, address, city) values ('Benedikta', 'Exley', '2023-01-01', 'Suite 27', 'Būsh');
insert into members (firstname, surname, dob, address, city) values ('Dennie', 'Spencley', '2024-02-01', 'Room 699', 'Jiabei');
insert into members (firstname, surname, dob, address, city) values ('Jessalin', 'Mowne', '2023-06-12', '19th Floor', 'Obong');
insert into members (firstname, surname, dob, address, city) values ('Benny', 'Scoffham', '2022-12-30', 'PO Box 46930', 'Qiucun');
insert into members (firstname, surname, dob, address, city) values ('Barbra', 'Pook', '2023-12-08', 'Room 365', 'Všeruby');
insert into members (firstname, surname, dob, address, city) values ('Krysta', 'Crack', '2022-12-15', 'Room 200', 'Zharkovskiy');
insert into members (firstname, surname, dob, address, city) values ('Grenville', 'Feige', '2022-11-07', '15th Floor', 'Trondheim');
insert into members (firstname, surname, dob, address, city) values ('Neil', 'Gibbeson', '2023-08-17', '3rd Floor', 'Skillingaryd');
insert into members (firstname, surname, dob, address, city) values ('Aymer', 'Beeson', '2024-01-27', 'PO Box 29601', 'Dabagou');
insert into members (firstname, surname, dob, address, city) values ('Stern', 'Worts', '2023-02-14', '1st Floor', 'Rāiwind');
insert into members (firstname, surname, dob, address, city) values ('Conan', 'Blaxley', '2023-07-19', 'Suite 80', 'Kapsan-ŭp');
insert into members (firstname, surname, dob, address, city) values ('Ronnica', 'Ourry', '2024-03-17', 'Apt 1209', 'Yonglong');
insert into members (firstname, surname, dob, address, city) values ('Keen', 'Saket', '2023-07-02', 'PO Box 95408', 'Pingyang');
insert into members (firstname, surname, dob, address, city) values ('Datha', 'Dominik', '2023-02-08', 'Suite 27', 'Chishtiān Mandi');
insert into members (firstname, surname, dob, address, city) values ('Dorey', 'Bottjer', '2023-06-30', 'Room 523', 'Silago');
insert into members (firstname, surname, dob, address, city) values ('James', 'Terlinden', '2023-05-18', 'Room 1564', 'Garden Grove');
insert into members (firstname, surname, dob, address, city) values ('Brynna', 'Langstone', '2023-09-01', 'PO Box 7911', 'Longwan');
insert into members (firstname, surname, dob, address, city) values ('Teodoro', 'Seleway', '2022-11-03', 'Suite 25', 'San José');
insert into members (firstname, surname, dob, address, city) values ('Leontine', 'Duckhouse', '2022-11-04', 'Apt 1530', 'Dingyan');
insert into members (firstname, surname, dob, address, city) values ('Leo', 'Hyslop', '2023-09-08', 'PO Box 25628', 'Chama');
insert into members (firstname, surname, dob, address, city) values ('Rachael', 'Woollends', '2022-12-10', 'Suite 49', 'Yelizavetinskaya');
insert into members (firstname, surname, dob, address, city) values ('Scarlett', 'Stoddard', '2023-07-10', 'Suite 49', 'Marisgama');
insert into members (firstname, surname, dob, address, city) values ('Sissy', 'Godbert', '2024-01-26', 'PO Box 6983', 'Shuangxi');
insert into members (firstname, surname, dob, address, city) values ('Alexei', 'Mauger', '2023-01-24', '19th Floor', 'Klenica');
insert into members (firstname, surname, dob, address, city) values ('Desiri', 'Pick', '2023-04-24', 'PO Box 27223', 'Gaotieling');
insert into members (firstname, surname, dob, address, city) values ('Kalle', 'Augie', '2022-12-07', 'Room 942', 'Higashimurayama-shi');
insert into members (firstname, surname, dob, address, city) values ('Claudianus', 'Vivian', '2023-04-17', '17th Floor', 'Bajiazi');
insert into members (firstname, surname, dob, address, city) values ('Isabella', 'Bellino', '2024-01-02', 'Room 1679', 'Orizari');
insert into members (firstname, surname, dob, address, city) values ('Lina', 'Mattedi', '2023-08-26', 'Room 831', 'Lukhovka');
insert into members (firstname, surname, dob, address, city) values ('Kassey', 'Howlett', '2023-10-12', 'Suite 80', 'Thạnh Mỹ');
insert into members (firstname, surname, dob, address, city) values ('Jessi', 'O''Kynsillaghe', '2024-03-01', 'Suite 1', 'Ruda-Huta');
insert into members (firstname, surname, dob, address, city) values ('Con', 'Renad', '2023-12-01', 'Room 988', 'Besançon');
insert into members (firstname, surname, dob, address, city) values ('Fernande', 'Stigers', '2023-09-12', 'PO Box 94499', 'Laba Goumen');
insert into members (firstname, surname, dob, address, city) values ('Leilah', 'Steedman', '2024-02-17', 'Suite 7', 'Replot');
insert into members (firstname, surname, dob, address, city) values ('Francklin', 'Birtle', '2024-03-15', 'Suite 42', 'Tinabogan');
insert into members (firstname, surname, dob, address, city) values ('Tann', 'Dedon', '2023-07-26', 'Suite 88', 'Strellc i Epërm');
insert into members (firstname, surname, dob, address, city) values ('Kirbee', 'Tolfrey', '2023-05-24', 'Apt 407', 'Rendeng');
insert into members (firstname, surname, dob, address, city) values ('Giustino', 'Bims', '2022-12-09', 'Room 48', 'Bigaan');
insert into members (firstname, surname, dob, address, city) values ('Kirsti', 'Olenin', '2022-11-29', 'Suite 18', 'Skerries');
insert into members (firstname, surname, dob, address, city) values ('Winifred', 'Syrie', '2023-01-01', '15th Floor', 'Zhen’an');
insert into members (firstname, surname, dob, address, city) values ('Skipper', 'Dinjes', '2023-10-01', '14th Floor', 'Qianjia');
insert into members (firstname, surname, dob, address, city) values ('Marianna', 'Mostin', '2023-04-22', '4th Floor', 'Echarate');
insert into members (firstname, surname, dob, address, city) values ('Brendan', 'Ivanin', '2023-02-07', 'PO Box 81763', 'Goght’');
insert into members (firstname, surname, dob, address, city) values ('Drona', 'Tarbath', '2023-04-04', 'Apt 297', 'Kotovsk');
insert into members (firstname, surname, dob, address, city) values ('Tades', 'Blooman', '2023-12-05', '17th Floor', 'Kaulon');
insert into members (firstname, surname, dob, address, city) values ('Beverlie', 'Leafe', '2023-08-16', 'Suite 3', 'Duki');
insert into members (firstname, surname, dob, address, city) values ('Jennilee', 'Di Lucia', '2023-08-04', '11th Floor', 'Kostinbrod');
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- lessons table:
CREATE TABLE `leisurecentre`.`lessons` (
  `lessonID` INT NOT NULL AUTO_INCREMENT,
  `courseID` INT NULL DEFAULT NULL,
  `memberID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`lessonID`),
  INDEX `courseID_idx` (`courseID` ASC) VISIBLE,
  INDEX `memberID_idx` (`memberID` ASC) VISIBLE,
  CONSTRAINT `courseID`
    FOREIGN KEY (`courseID`)
    REFERENCES `leisurecentre`.`course` (`courseID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `memberID`
    FOREIGN KEY (`memberID`)
    REFERENCES `leisurecentre`.`members` (`memberID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
DESC lessons;
SELECT * FROM lessons;

insert into lessons (courseID, memberID) values (42, 23);
insert into lessons (courseID, memberID) values (5, 28);
insert into lessons (courseID, memberID) values (10, 42);
insert into lessons (courseID, memberID) values (5, 46);
insert into lessons (courseID, memberID) values (5, 7);
insert into lessons (courseID, memberID) values (18, 23);
insert into lessons (courseID, memberID) values (48, 28);
insert into lessons (courseID, memberID) values (5, 23);
insert into lessons (courseID, memberID) values (23, 23);
insert into lessons (courseID, memberID) values (12, 46);
insert into lessons (courseID, memberID) values (3, 19);
insert into lessons (courseID, memberID) values (39, 42);
insert into lessons (courseID, memberID) values (31, 15);
insert into lessons (courseID, memberID) values (18, 42);
insert into lessons (courseID, memberID) values (16, 28);
insert into lessons (courseID, memberID) values (39, 7);
insert into lessons (courseID, memberID) values (16, 15);
insert into lessons (courseID, memberID) values (14, 31);
insert into lessons (courseID, memberID) values (5, 46);
insert into lessons (courseID, memberID) values (14, 19);
insert into lessons (courseID, memberID) values (27, 19);
insert into lessons (courseID, memberID) values (3, 10);
insert into lessons (courseID, memberID) values (12, 37);
insert into lessons (courseID, memberID) values (23, 19);
insert into lessons (courseID, memberID) values (14, 31);
insert into lessons (courseID, memberID) values (29, 10);
insert into lessons (courseID, memberID) values (12, 31);
insert into lessons (courseID, memberID) values (7, 10);
insert into lessons (courseID, memberID) values (12, 2);
insert into lessons (courseID, memberID) values (7, 15);
insert into lessons (courseID, memberID) values (18, 19);
insert into lessons (courseID, memberID) values (29, 28);
insert into lessons (courseID, memberID) values (36, 42);
insert into lessons (courseID, memberID) values (31, 23);
insert into lessons (courseID, memberID) values (3, 7);
insert into lessons (courseID, memberID) values (5, 5);
insert into lessons (courseID, memberID) values (23, 2);
insert into lessons (courseID, memberID) values (12, 7);
insert into lessons (courseID, memberID) values (5, 19);
insert into lessons (courseID, memberID) values (18, 46);
insert into lessons (courseID, memberID) values (14, 2);
insert into lessons (courseID, memberID) values (18, 42);
insert into lessons (courseID, memberID) values (48, 42);
insert into lessons (courseID, memberID) values (27, 10);
insert into lessons (courseID, memberID) values (16, 23);
insert into lessons (courseID, memberID) values (16, 37);
insert into lessons (courseID, memberID) values (23, 10);
insert into lessons (courseID, memberID) values (20, 15);
insert into lessons (courseID, memberID) values (18, 42);
insert into lessons (courseID, memberID) values (9, 42);