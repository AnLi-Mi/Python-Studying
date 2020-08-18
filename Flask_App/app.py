from flask import Flask, render_template,url_for, request, json
from flaskext.mysql import MySQL

app=Flask(__name__)
mysql= MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '8G13rm3k'
app.config['MYSQL_DATABASE_DB'] = 'python_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def start():
    name = ''
    age =0
    fut =0
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        age = int(request.form.get('userage'))
        fut= (age+5)   
    return render_template('index.html', name=name, age=age, fut=fut)

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



@app.route('/data', methods=['GET','POST'])
def database():
    results=''
    user_choice=''
    order=''
    full_query = ''
    if request.method == 'POST' and 'userquery' in request.form:
        user_choice = request.form.get('userquery')
        #order = request.form.get('userorder')
        full_query = "UPDATE doctor SET Doctor_Name = '" + user_choice + "' WHERE Doctor_Name = 'David';"
        commit_executing_query(full_query)
    return render_template('data.html', results=results, full_query=full_query, user_choice=user_choice)




def connect_msql():
    conn = mysql.connect()
    if (conn):
    # Carry out normal procedure
        print ("Connection successful")
    else:
    # Terminate
        print ("Connection unsuccessful")


connect_msql()


    

def fetch_executing_query(query):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def commit_executing_query(query):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute(query)
    conn.commit()
    


    




    

if __name__ == '__main__':
   app.run(debug=True)

    





