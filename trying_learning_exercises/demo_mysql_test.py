import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8G13rm3k",
        database ="mydataase"
    )

    if mydb.is_connected():

        print(f'You are connected to a server: {mydb.get_server_info()}')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT database()")
        result = mycursor.fetchone()
        print (f'You are connected to a database: {result}')
    
except Error:
    print('An error has apeared: ', Error)
