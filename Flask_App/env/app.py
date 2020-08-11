from flask import Flask, render_template,url_for

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

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)
