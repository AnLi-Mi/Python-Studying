import pymongo

connection=pymongo.MongoClient("mongodb://localhost:27017/")

db_list =connection.list_database_names()
print(db_list)

db=connection["ResturantsDB"]

col_list =db.list_collection_names()
print(col_list)

col=db["restaurants"]

print('----------------------------Q1-----------------------------------')

# Question 1: Write a MongoDB query
# to display all the documents in the collection restaurants. limit to 10 first results

all_doc=col.find().limit(10)

for res in all_doc:
    print(res)

print('----------------------------Q2-----------------------------------')

# Question 2: Write a MongoDB query to display the fields
#restaurant_id, name, borough and cuisine for all the documents. limit to 10 first results

all_doc=col.find().limit(10)

for res in all_doc:
   print(f'{res["restaurant_id"]}, {res[ "name"]}, {res[ "borough"]}, {res[ "cuisine"]}')


print('----------------------------Q3-----------------------------------')

#  Write a MongoDB query to display names of all the restaurant
# which is in the borough Bronx. limit to 10 first results

query={"borough":"Bronx"}

bronx_res = col.find(query).limit(10)

for res in bronx_res:
    print(res["name"])

print('----------------------------Q4-----------------------------------')

#Write a MongoDB query to display the next 5 restaurants
#after skipping first 5 which are in the borough Bronx

query={"borough":"Bronx"}

bronx_res = col.find(query).skip(5).limit(5)

for res in bronx_res:
    print(res["name"])

print('----------------------------Q5-----------------------------------')

# Write a MongoDB query to find the restaurants that achieved a score,
# more than 80 but less than 100

query = {"$and":[{"grades.score" : {"$gt":80}}, {"grades.score" : {"$lt":100}}]}
res_80_100 = col.find(query).limit(10)

for res in res_80_100:
    print(f'{res["name"]}')

query2= {"grades": { "$elemMatch":{"score":{"$gt" : 80 , "$lt" :100}}}}
res_80_100_v2 = db.restaurants.find(query2).limit(10)   

for res in res_80_100_v2:
    print(res)


