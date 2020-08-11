from flask import Flask, render_template,url_for

app=Flask(__name__)

@app.route('/home')
def hello():
    return "<h1> Welcome on my page!<h1>"

@app.route('/about')
def main():
    return render_template('index.html')

@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
