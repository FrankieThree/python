#Sets employee's salary to 25000 if their salary is NULL
DELIMITER $$
CREATE TRIGGER EMP_SALARY
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
	IF (NEW.salary = '' OR NEW.salary IS NULL) 
    THEN 
	SET NEW.salary = ('25000');
	END IF;
END$$
DELIMITER ;

#Example for Trigger
INSERT INTO employee
VALUES("109 Pine Way","756345877","19700501", "M", "Jim", "Bo", "Harris","50", "999999999",NULL,"159159159");