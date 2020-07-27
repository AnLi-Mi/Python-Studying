import mysql.connector

# Question 1: Connect to your database server and print its version
def connection_start():
    database = mysql.connector.connect(user= 'root', password= '8G13rm3k', host= 'localhost', database='python_db')
    return database

def connection_stop(database):
    if database:
        database.close()
    

def version_check():
    database=connection_start()
    cursor=database.cursor()
    dbs_version=('SELECT version();')
    cursor.execute(dbs_version)
    result = cursor.fetchall()
    return result
    connection_stop(database)


print(f"Qeestion 1: I'm using {version_check()} version of MySQL")

# Question 2: Fetch Hospital and Doctor Information
#using hospital Id and doctor Id

def doctor_info(doctor_id):
    database=connection_start()
    cursor=database.cursor()
    doctor_details=("select * from Doctor where Doctor_Id = %s")
    cursor.execute(doctor_details, (doctor_id,))
    result = cursor.fetchall()
   # return print (result)
    for info in result:
        print(f'Name: {info[1]}')
        print(f'Hospital_ID: {info[2]}')
        print(f'Joined the hospital on: {info[3]}')
        print(f'Speciality: {info[4]}')
        print(f'Salary: {info[5]}')
    connection_stop(database)

def hospital_info(hospital_id):
    database=connection_start()
    cursor=database.cursor()
    doctor_details=("select * from hospital where Hospital_Id = %s")
    cursor.execute(doctor_details, (hospital_id,))
    result = cursor.fetchall()
    for info in result:
        print(f'Name: {info[1]}')
        print(f'Number of beds: {info[2]}')
    connection_stop(database) 

doc=input('Enter in ID number of a doctor: ')
doctor_info(doc)
hos=input('Enter in ID number of a hospital: ')
hospital_info(hos)


# Questions 3: Get the list Of doctors as per the given specialty and salary

def doc_list(speciality, salary):
    database=connection_start()
    cursor=database.cursor()
    query=('SELECT d.doctor_name, h.hospital_name FROM doctor d JOIN hospital h on d.hospital_id = h.hospital_id WHERE speciality = %s and salary > %s;')
    cursor.execute(query, (speciality, salary,))
    result = cursor.fetchall()
    print (f'The {speciality}s with salary above {salary} are: ')
    for record in result:
        print (f' Doctor {record[0]} from hospital {record[1]}')
    connection_stop(database)

spec=input('Enter speciality: ')
sal=input('Enter salary : ')
doc_list(spec,sal)

#Question 4: Get a list of doctors from a given hospital

def doc_hos_list(hos_name):
    database=connection_start()
    cursor=database.cursor()
    query = ("SELECT d.doctor_id, d.doctor_name FROM doctor d JOIN hospital h ON d.hospital_id=h.hospital_id WHERE hospital_name= %s;")
    cursor.execute(query, (hos_name,))
    result=cursor.fetchall()
    print (f'Doctors working in the hospital {hos_name} are: ')
    for record in result:
        print (f'{record[0]} - {record[1]}')
    connection_stop(database)

hos=input('Enter the name of the hospital: ')
doc_hos_list(hos)

# Operation 5: Update doctor experience in years

import datetime
from dateutil.relativedelta import relativedelta

def exp_update(doc):
    database=connection_start()
    cursor=database.cursor()
    query = ("SELECT joining_date FROM doctor WHERE doctor_id= %s;")
    cursor.execute(query,(doc,))
    result = cursor.fetchone()
    joining_date= datetime.datetime.strptime(''.join(map(str, result)), '%Y-%m-%d')
    today_date = datetime.datetime.now()
    exp_yr = relativedelta(today_date, joining_date).years
    query2 = ("UPDATE doctor SET experience = %s WHERE doctor_id= %s;")
    cursor.execute(query2,(exp_yr,doc,))
    database.commit()

doc=input("Enter doctor's Id number: ") 
exp_update(doc)
            


