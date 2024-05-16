#View of manager's Fname,Lname,Office_Location,Start_date of each office
CREATE VIEW mgr_start_dates(First_Name,Last_Name,Office_Location,Start_Date)
AS SELECT e.Fname, e.Lname,o.Office_Location,o.MGR_Start_Date
FROM employee AS e, office AS o
WHERE e.ssn = o.MGR_SSN;

#View of employee's names and which office they work at
CREATE VIEW office_info(Fname,Lname,Location)
AS SELECT e.Fname, e.Lname, o.Office_Location
FROM office AS o, employee AS e
WHERE e.E_Office_ID = o.Office_ID;

#return payment method of customer
CREATE VIEW customer_payment(First_Name, Last_Name, Contract_ID, Payment_Method)
AS SELECT c.fname, c.lname, p.pm_contract_id, p.method
	FROM customer as c, payment_method as p
	WHERE c.customer_id = p.pm_customer_id;