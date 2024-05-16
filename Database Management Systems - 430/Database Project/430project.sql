-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`CUSTOMER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CUSTOMER` (
  `Address` VARCHAR(45) NULL,
  `Sex` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `FName` VARCHAR(45) NULL,
  `LName` VARCHAR(45) NULL,
  `Customer_ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Customer_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`EMPLOYEE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`EMPLOYEE` (
  `Address` VARCHAR(45) NULL,
  `Ssn` VARCHAR(9) NOT NULL,
  `BDate` DATE NULL,
  `Sex` VARCHAR(45) NULL,
  `FName` VARCHAR(45) NULL,
  `MName` VARCHAR(45) NULL,
  `LName` VARCHAR(45) NULL,
  `Age` INT NULL,
  `Super_Ssn` VARCHAR(9) NULL,
  `Salary` VARCHAR(45) NULL,
  `E_Office_ID` VARCHAR(45) NULL,
  PRIMARY KEY (`Ssn`),
  INDEX `Super_Ssn_idx` (`Super_Ssn` ASC) VISIBLE,
  INDEX `E_Office_ID_idx` (`E_Office_ID` ASC) VISIBLE,
  CONSTRAINT `Super_Ssn`
    FOREIGN KEY (`Super_Ssn`)
    REFERENCES `mydb`.`EMPLOYEE` (`Ssn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `E_Office_ID`
    FOREIGN KEY (`E_Office_ID`)
    REFERENCES `mydb`.`OFFICE` (`Office_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`OFFICE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`OFFICE` (
  `Office_ID` VARCHAR(45) NOT NULL,
  `Office_Name` VARCHAR(45) NULL,
  `MGR_SSN` VARCHAR(9) NULL,
  `MGR_Start_Date` DATE NULL,
  `Office_Location` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `Hours` INT NULL,
  PRIMARY KEY (`Office_ID`),
  INDEX `MGR_SSN_idx` (`MGR_SSN` ASC) VISIBLE,
  CONSTRAINT `MGR_SSN`
    FOREIGN KEY (`MGR_SSN`)
    REFERENCES `mydb`.`EMPLOYEE` (`Super_Ssn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`INSURANCE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`INSURANCE` (
  `Insurance_Number` VARCHAR(45) NOT NULL,
  `Full_Coverage` VARCHAR(45) NULL,
  `Liability` VARCHAR(45) NULL,
  PRIMARY KEY (`Insurance_Number`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`VEHICLE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`VEHICLE` (
  `Vin` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NULL,
  `Color` VARCHAR(45) NULL,
  `Rental_Price` VARCHAR(45) NULL,
  `V_Insurance_Number` VARCHAR(45) NULL,
  PRIMARY KEY (`Vin`),
  INDEX `V_Insurance_Number_idx` (`V_Insurance_Number` ASC) VISIBLE,
  CONSTRAINT `V_Insurance_Number`
    FOREIGN KEY (`V_Insurance_Number`)
    REFERENCES `mydb`.`INSURANCE` (`Insurance_Number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CONTRACT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CONTRACT` (
  `Contract_ID` VARCHAR(45) NOT NULL,
  `Start_date` DATE NULL,
  `End_Date` DATE NULL,
  `C_Office_ID` VARCHAR(45) NULL,
  `C_Customer_ID` VARCHAR(45) NULL,
  `C_Vin` VARCHAR(45) NULL,
  PRIMARY KEY (`Contract_ID`),
  INDEX `C_Office_ID_idx` (`C_Office_ID` ASC) VISIBLE,
  INDEX `C_Customer_ID_idx` (`C_Customer_ID` ASC) VISIBLE,
  INDEX `C_Vin_idx` (`C_Vin` ASC) VISIBLE,
  CONSTRAINT `C_Office_ID`
    FOREIGN KEY (`C_Office_ID`)
    REFERENCES `mydb`.`OFFICE` (`Office_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `C_Customer_ID`
    FOREIGN KEY (`C_Customer_ID`)
    REFERENCES `mydb`.`CUSTOMER` (`Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `C_Vin`
    FOREIGN KEY (`C_Vin`)
    REFERENCES `mydb`.`VEHICLE` (`Vin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CAR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CAR` (
  `CAR_Vin` VARCHAR(45) NOT NULL,
  `No_seats` VARCHAR(45) NULL,
  `Engine_size` VARCHAR(45) NULL,
  PRIMARY KEY (`CAR_Vin`),
  CONSTRAINT `CAR_Vin`
    FOREIGN KEY (`CAR_Vin`)
    REFERENCES `mydb`.`VEHICLE` (`Vin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TRUCK`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TRUCK` (
  `TRUCK_Vin` VARCHAR(45) NOT NULL,
  `Tonnage` FLOAT NULL,
  `Cab_Size` VARCHAR(45) NULL,
  PRIMARY KEY (`TRUCK_Vin`),
  CONSTRAINT `TRUCK_Vin`
    FOREIGN KEY (`TRUCK_Vin`)
    REFERENCES `mydb`.`VEHICLE` (`Vin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`REQUIRES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`REQUIRES` (
  `R_Contract_ID` VARCHAR(45) NOT NULL,
  `R_Customer_ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`R_Contract_ID`, `R_Customer_ID`),
  INDEX `R_Customer_ID_idx` (`R_Customer_ID` ASC) VISIBLE,
  CONSTRAINT `R_Contract_ID`
    FOREIGN KEY (`R_Contract_ID`)
    REFERENCES `mydb`.`CONTRACT` (`Contract_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `R_Customer_ID`
    FOREIGN KEY (`R_Customer_ID`)
    REFERENCES `mydb`.`CUSTOMER` (`Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PAYMENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PAYMENT` (
  `P_Customer_ID` VARCHAR(45) NOT NULL,
  `P_Contract_ID` VARCHAR(45) NOT NULL,
  `Total_Price` INT NULL,
  PRIMARY KEY (`P_Customer_ID`, `P_Contract_ID`),
  INDEX `P_Contract_ID_idx` (`P_Contract_ID` ASC) VISIBLE,
  CONSTRAINT `P_Customer_ID`
    FOREIGN KEY (`P_Customer_ID`)
    REFERENCES `mydb`.`REQUIRES` (`R_Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `P_Contract_ID`
    FOREIGN KEY (`P_Contract_ID`)
    REFERENCES `mydb`.`REQUIRES` (`R_Contract_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DEALS_WITH`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DEALS_WITH` (
  `DW_Customer_ID` VARCHAR(45) NOT NULL,
  `DW_Office_ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DW_Customer_ID`, `DW_Office_ID`),
  INDEX `DW_Office_ID_idx` (`DW_Office_ID` ASC) VISIBLE,
  CONSTRAINT `DW_Customer_ID`
    FOREIGN KEY (`DW_Customer_ID`)
    REFERENCES `mydb`.`CUSTOMER` (`Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DW_Office_ID`
    FOREIGN KEY (`DW_Office_ID`)
    REFERENCES `mydb`.`OFFICE` (`Office_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PAYMENT_METHOD`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PAYMENT_METHOD` (
  `PM_Customer_ID` VARCHAR(45) NOT NULL,
  `PM_Contract_ID` VARCHAR(45) NOT NULL,
  `Method` VARCHAR(45) NULL,
  PRIMARY KEY (`PM_Customer_ID`, `PM_Contract_ID`),
  INDEX `P_Contract_ID0_idx` (`PM_Contract_ID` ASC) VISIBLE,
  CONSTRAINT `P_Customer_ID0`
    FOREIGN KEY (`PM_Customer_ID`)
    REFERENCES `mydb`.`PAYMENT` (`P_Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `P_Contract_ID0`
    FOREIGN KEY (`PM_Contract_ID`)
    REFERENCES `mydb`.`PAYMENT` (`P_Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
