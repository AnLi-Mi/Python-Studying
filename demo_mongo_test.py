import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(pymongo.server_description)

fist_db =myclient["fist_db"]
