import psycopg2
mypgdb=psycopg2.connect(user = "postgres", password = "8G13rm3k", host = "localhost",database="Postgers_my_DB")

p_cursor = mypgdb.cursor()

    #connection test

con_test = mypgdb.get_dsn_parameters()
print(con_test)

    #craeting a new table - testing changing/updating commands

#new_table = ("CREATE TABLE Students (Student_ID int, Name varchar(50), Surname varchar(50), Faculty varchar(50));")

#p_cursor.execute(new_table)
#mypgdb.commit()

    #populating 'customer' table with new records

add_customers = ("INSERT INTO customers (customer_id, customer_name, email) VALUES (6, 'Matt Smith', 'matt@smith.com');")
p_cursor.execute(add_customers)
mypgdb.commit()
