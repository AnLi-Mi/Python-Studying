from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, let's statr the app!"


app.run(port=5000)
