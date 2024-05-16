#INSERT Example
INSERT INTO customer
VALUES ("98 Oak Forest", "M", "wdc@gmail.com", "6546135544", "Mark", "Brown", 0000000001);

#UPDATE Example
UPDATE customer 
SET Phone = 5048675309
WHERE Lname = "Brown";

#DELETE Example
DELETE FROM customer
WHERE Lname = 'Brown';

#displays address of female customers
SELECT address
FROM customer
WHERE sex = 'F';

#Returns Engine_Size of specified CAR_Vin
SELECT Engine_size
FROM car
WHERE CAR_Vin = '1234567890ABCCAR1';

#Returns table of employee's Fname,LName,MName where their age > 20
SELECT FName, MName, LName 
FROM employee
WHERE Age > 20; 

#Returns Office_Name and Office_Location where the customer is Female
SELECT o.Office_Name, o.Office_Location
FROM office as o
WHERE o.Office_ID IN
		( SELECT d.C_Office_ID
		FROM contract as d
		WHERE d.C_Customer_ID IN
		( SELECT c.Customer_ID
				FROM customer as c
				WHERE c.Sex = 'F' )
		);

#Returns Max,Min,Avg salary of all employees
SELECT MAX(Salary) AS Highest_Sal, MIN(Salary) AS Lowest_Sal, AVG(Salary) AS Average_Sal
FROM employee;