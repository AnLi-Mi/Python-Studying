import mysql.connector

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


print(f"I'm using {version_check()} version of MySQL")  
