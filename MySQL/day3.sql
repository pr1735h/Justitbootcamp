CREATE SCHEMA `c9w4songs` ;

CREATE TABLE `c9w4songs`.`songs` (
  `SongID` INT NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(60) NOT NULL,
  `Artist` VARCHAR(60) NOT NULL,
  `Genre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`SongID`));
  
  CREATE TABLE `c9w4songs`.`members` (
  `MemberID` INT NOT NULL AUTO_INCREMENT,
  `Firstname` VARCHAR(60) NOT NULL,
  `Lastname` VARCHAR(60) NOT NULL,
  `Email` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`MemberID`));

CREATE TABLE `c9w4songs`.`downloads` (
  `DownloadID` INT NOT NULL AUTO_INCREMENT,
  `SongID` INT NULL,
  `MemberID` INT NULL,
  `Date` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DownloadID`),
  INDEX `SongID_idx` (`SongID` ASC) VISIBLE,
  INDEX `MemberID_idx` (`MemberID` ASC) VISIBLE,
  CONSTRAINT `SongID`
    FOREIGN KEY (`SongID`)
    REFERENCES `c9w4songs`.`songs` (`SongID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `MemberID`
    FOREIGN KEY (`MemberID`)
    REFERENCES `c9w4songs`.`members` (`MemberID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

select * from songs;
desc songs;