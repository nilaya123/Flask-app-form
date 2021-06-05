Setting up a Flask and MySQL Database Connection
=================================================

We are setting up a flask with Web Form, which populates the data into MySQL Database


How to use this project?
========================
1. Get MySQL Database setup with two tables:
 Employee and Department
 Employee (id, email, name, department_id)
 Department (id, name)
 
 mysql> DESCRIBE employee;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| employee_id    | int         | NO   | PRI | NULL    |       |
| employee_name  | varchar(45) | NO   |     | NULL    |       |
| employee_email | varchar(90) | NO   |     | NULL    |       |
| departmet_id   | int         | NO   |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
4 rows in set (0.05 sec)

mysql> DESCRIBE department;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| department_id   | int          | NO   | PRI | NULL    |       |
| department_name | varchar(100) | NO   |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
2 rows in set (0.01 sec)
 
2. Fork or Clone this repository.

3. Create Virtual Enviornment, and activate the same.

4. Run requirements.txt/.

5. On your local repository, run "python app.py".

6. On Browser, open http://127.0.0.1:5000/ to open app.

7. Enter the details into the form, with submit, data should get updated in database as below:

mysql> SELECT * FROM employee;
+-------------+------------------+----------------------------+---------------+
| employee_id | employee_name    | employee_email             | department_id |
+-------------+------------------+----------------------------+---------------+
|           5 | asit             | asit@gmail.com             |             0 |
|           6 | Shirish Indurkar | shirish.indurkar@gmail.com |             0 |
|           7 | Nilaya Indurkar  | nilaya.indurkar@gmail.com  |             0 |
|           8 | Asit Indurkar    | asit@gmail.com             |             0 |
+-------------+------------------+----------------------------+---------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM department;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             5 | IT              |
|             6 | QA              |
|             7 | HR              |
|             8 | IT              |
+---------------+-----------------+
4 rows in set (0.00 sec) 
