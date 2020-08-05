#---downloading necessary module, connecting to server and checking connection---

import pymongo
connect = pymongo.MongoClient("mongodb://localhost:27017/")
print(pymongo.server_description)


#---checking existing databases and creating a new one--------

db_list =connect.list_database_names()
print(db_list)

if "python_db" in db_list:
    print('The database already exists')

first_db =connect["python_db"]

#---creating a collection in a new db-------------

db_col =first_db.list_collection_names()
print(db_col)

if "clients" in db_col:
    print('The collection already exists')

first_col =first_db["clients"]


#---creating a dictionary with information/documents' content I want to include in the collection

mydocs= [{ "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}]

#----inserting the list of dictionaries as documents to my collection-----

# # insert = first_col.insert_many(mydocs)
# #print(insert)

# ---extracting all data from database-------------------

for doc in first_col.find():
    print(doc)

# ---excluting 'address' from extraction------------------------

for doc in first_col.find({},{"address":0}):
    print(doc)

# ---extracting one/fisrt document from database-----------------------

ext_one = first_col.find_one()
print(ext_one)


# ---extracting filtered documents form the colelction (using a query)-----

query1 = {"name":"Betty"}
query2 = {"address": "/Valley/" }
query3 = {"name": {"$gt":"R"}}

print ('----------Q1----------\n')
for doc in first_col.find(query1):
    print(doc)

print ('----------Q2----------\n')
for doc in first_col.find(query2):
    print(doc)

print ('----------Q3----------\n')
for doc in first_col.find(query3):
    print(doc)


# -----------sorting results dsc--------------------

for doc in first_col.find(query3).sort("name",-1):
    print(doc)


# ----------deleting duplicated documents-------------
# choosing a doc

query={"first_name":"Antol"}

# counting how many times the doc is repeated
doc_count = first_col.find(query).count()
print(doc_count)

#looping a deleting function until only one doc is left
i=1
y=int(doc_count)

while i<y:
    first_col.delete_one(query)
    i+=1

for doc in first_col.find().sort("name",-1):
    print(doc)
    
# ----------updating documents-------------

# changing/updating values of filtered documents
query1 = {"first_name":"Anatol"}
new_value1 = {"$set": {"first_name":"Anatoll"}}

first_col.update_one(query1,new_value1)

query2 = {"address" : {"$regex":"^M"}}
new_value2 = {"$set": {"name":"Koko"}}

up= first_col.update_many(query2,new_value2)

print(f'{up.modified_count} documets were updated')

for x in first_col.find():
    print(x)
    
# adding new info (the same) to all documents

query = {"name": { "$gt": "A" } }

new_value = {"$set":{"age":30}}

first_col.update_many(query,new_value)

for x in first_col.find():
    print(x)

# chaging/incrementing numerical values of filtered documents
    
query = {"name": "Ben" }

new_value = {"$inc":{"age":6}}

first_col.update_many(query,new_value)

for x in first_col.find():
    print(x)

# changing/updating fied names of filtered documents

query = {"first_name": "Anatoll" }

new_value = {"$rename":{"first_name":"name"}}

first_col.update_one(query,new_value)

for x in first_col.find():
    print(x)

# removing field form filtered documets

query = {"first_name": "Anatoll" }

new_value = {"$unset":{"last_name":1}}

first_col.update_one(query,new_value)

for x in first_col.find():
    print(x)

# adding new document in case it's not found

query = {"name": "Mary" }

new_value = {"$set":{"name":"Mary", "age":28}}

first_col.update_one(query,new_value,upsert=True)

for x in first_col.find():
    print(x)







    
