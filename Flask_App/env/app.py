from flask import Flask, render_template,url_for, request, json
import mysql.connector
from mysql.connector import Error

app=Flask(__name__)

@app.route('/bucket_list')
def main():
    return render_template('bucket_list.html')

@app.route('/home')
def hello():
    return "<h1> Welcome on my page!<h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/method', methods= ['GET','POST'])
def met():
    if request.method == 'POST':
        return "I'm using POST method"
    else:
        return "I'm using GET method"

    
if __name__ == "__main__":
    app.run(debug=True)




