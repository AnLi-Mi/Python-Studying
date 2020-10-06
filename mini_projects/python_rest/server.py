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
 print(json_ids)
 return json_ids
 

get_employees() 
    
