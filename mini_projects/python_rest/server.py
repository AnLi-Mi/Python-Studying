from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


def get_employees():
    conn = db_connect.connect() # connecting to the db
    query = conn.execute("select * from employees") # selecting all employees
    employees = query.cursor.fetchall() # fetching the results
    IDs = [e[0] for e in employees] #creating a list of employees' IDs
    json_ids = {'employees' : IDs}
    return json_ids

def get_tracks():
    conn = db_connect.connect()
    query = conn.execute("select trackid, name, composer, unitprice from tracks LIMIT 20;")
    dict_list = []
    for q in query:
        pair = dict(zip(q.keys(),q))
        dict_list.append(pair)
    result = {'data':dict_list}
    return (result)
        
        
    #query_keys=
    #tracks = query.cursor.fetchall()
    #for t in tracks:
     #   print (t)
    #result = [dict(zip(tuple (query.keys()), t)) for t in tracks]
    #print (result)
    #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    #return jsonify(result)
 

get_employees() 
get_tracks()
