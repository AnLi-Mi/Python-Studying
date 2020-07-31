import psycopg2
mypgdb=psycopg2.connect(user = "postgres", password = "8G13rm3k", host = "localhost",database="Postgers_my_DB")

p_cursor = mypgdb.cursor()

#test

con_test = mypgdb.get_dsn_parameters()
print(con_test)
