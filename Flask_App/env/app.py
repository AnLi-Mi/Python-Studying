from flask import Flask

app=Flask(__name__)

@app.route('/<a>')
def index(a):
    return"<h1> I'm Anna {}!</h1>".format(a)
