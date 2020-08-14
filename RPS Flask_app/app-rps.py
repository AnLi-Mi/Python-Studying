#ROCK PAPER SCISORS

from flask import Flask, request, render_template
import random
from anna_module import greeting, srp_pull, rps_comparing, random_selection

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def game():
    name=''
    #choice=''
    #comp=''
    #result=''
    if request.method=='POST' and 'username' in request.form:
        name=request.form.get('username')
      #  choice=request.form.get('userchoice')
       # comp=random_selection(srp_pull)
        #result=rps_comparing(comp, choice)
    return render_template('index.html', name=name)
    
app.run()


#name=input('Enter your name')

#greeting(name)

#choice=input('What are you choosing - rock, paper or scisors?: ')

#comp = random_selection(srp_pull)

#rps_comparing(comp, choice)







