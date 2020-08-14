#ROCK PAPER SCISORS

from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def game():
    return "It will be a rock-paper-scisores game"
    


app.run()




