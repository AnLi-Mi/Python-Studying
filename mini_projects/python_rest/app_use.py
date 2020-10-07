from flask import Flask, render_template, request, json
import requests
from pexels_api import API


app_use=Flask(__name__)

def calc_bmi(w,h):
    return round(w/(h**2),2)

def rec(bmi):
    if bmi<18.5:
        return "You're too skinny"
    elif bmi>25:
        return "You need to loose some weight"
    else:
        return "You have correct weight"

def dog_api_no_key():

    url = 'https://random.dog/woof.json'
    parameters = {'format':'json'} 
    dog = requests.get(url, params=parameters)
    return dog.json()['url']

def dog_api_key():
    url='https://api.pexels.com/v1'
    MY_API_KEY = '563492ad6f917000010000014a3f9bf8a7724c9daabaf113ac5bd748'
    #headers = {'Authorization': MY_API_KEY}
  #  parameters = {'format':'json', 'page': 1, 'per_page':10}
    dog = API(MY_API_KEY)
    dog.search('dog', page=1, results_per_page=1)
    dog_photo = dog.get_entries()[0].small
    return dog_photo

def my_api_no_key():

    url = 'http://127.0.0.1:5000/employees/2'
    parameters = {'format':'json'} 
    my_api = requests.get(url, params=parameters)
    return my_api.status_code

@app.route('/', methods=['GET', 'POST'])
def bmi():
    name = ''
    bmi= ''
    re=''
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        w = float(request.form.get('userw'))
        h = float(request.form.get('userh'))
        bmi = calc_bmi(w,h)
        re = rec(bmi)
    return render_template('bmi.html',  name=name, bmi=bmi, re=re)


@app.route('/test', methods=['GET','POST'])
def test():
    dog_pic = dog_api_no_key()
    return render_template('dogspics.html', dog_pic=dog_pic)


@app.route('/test2', methods = ['GET', 'POST'])
def test2():
    dog_pic = dog_api_key()
    return render_template('dogspics2.html', dog_pic=dog_pic)

@app.route('/my_api', methods=['GET','POST'])
def my_api():
    my_api = my_api_no_key()
    return render_template('my_api.html', my_api=my_api)




if __name__ == "__main__":
    app.run(debug=True)
