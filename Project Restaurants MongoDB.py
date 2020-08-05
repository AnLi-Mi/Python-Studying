import pymongo

connection=pymongo.MongoClient("mongodb://localhost:27017/")

db_list =connection.list_database_names()
print(db_list)

db=connection["ResturantsDB"]

col_list =db.list_collection_names()
print(col_list)

col=db["restaurants"]

# Question 1: Write a MongoDB query
# to display all the documents in the collection restaurants.

print('----------------------------Q1-----------------------------------')

all_doc=col.find()

for res in all_doc:
   print(res)


  

