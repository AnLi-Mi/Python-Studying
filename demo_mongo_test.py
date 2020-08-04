#downloading necessary module, connecting to server and checking connection

import pymongo
connect = pymongo.MongoClient("mongodb://localhost:27017/")
print(pymongo.server_description)


#checking existing databases and creating a new one

db_list =connect.list_database_names()
print(db_list)

if "python_db" in db_list:
    print('The database already exists')
else:
    fist_db =connect["python_db"]
