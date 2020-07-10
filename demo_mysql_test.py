import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8G13rm3k",
    database ="mydatabase"
)

print(f'you are connected to: {mydb.get_server_info()}')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

result = mycursor.fetchall()

print (result)

