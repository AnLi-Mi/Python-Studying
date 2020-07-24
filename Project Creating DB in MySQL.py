from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
#from mysql.connector import errorcode

DB_NAME = 'Testuje'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ( `emp_no` int(11) NOT NULL,"
    "`salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_emp'] = (
    "CREATE TABLE `dept_emp` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_manager'] = (
    "  CREATE TABLE `dept_manager` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['titles'] = (
    "CREATE TABLE `titles` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `title` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user= 'root', password= '8G13rm3k', host= 'localhost')
cursor = cnx.cursor()

#cursor.execute("CREATE DATABASE Testuje")
#cursor.execute("USE Testuje")

#for table_name in TABLES:
 #   table_description = TABLES[table_name]
  #  print(f"Creating table: {table_name} \n".format(table_name), end='')
   # cursor.execute(table_description)

cursor.close()
cnx.close()

cnx = mysql.connector.connect(user= 'root', password= '8G13rm3k', host= 'localhost', database = 'testuje')
cursor = cnx.cursor()

#add_employee = ("INSERT INTO employees(first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)")
#data = [('tut1','tutek','1999-01-02', 'M', '1979-10-11' ), ('tut2','tutek','1999-01-02', 'M', '1979-10-11' ), ('tut3','tutek','1999-01-02', 'M', '1979-10-11' ), ('tut4','tutek','1999-01-02', 'M', '1979-10-11' )]

#for employee in data:
#    cursor.execute(add_employee,employee)
#    cnx.commit()

cursor.close()
cnx.close()

cnx = mysql.connector.connect(user= 'root', password= '8G13rm3k', host= 'localhost', database = 'testuje')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

start1 = '2000-01-01'
start2 = '2001-01-01'

cursor.execute(query, (start1, start2))

for (record, record2, record3) in cursor:
    print (f"{record} {record2} was hired on {record3}")

salary_update= ("UPDATE salaries as s JOIN  employees as e ON e.emp_no=s.emp_no SET salary = salary*1.15 WHERE e.hire_date BETWEEN '1998-01-01' AND '1999-01-01';")

cursor.execute (salary_update)
cnx.commit()






    

