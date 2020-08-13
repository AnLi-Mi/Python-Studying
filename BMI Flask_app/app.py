from flask import Flask, render_template, request, json


app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    
    name = ''
    weight =0
    #hight =0
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        weight = int(request.form.get('userw'))
      #  hight= int(request.form.get('userh'))
       # BMI = weight/(hight**2)
    return render_template('bmi.html',  name=name, weight=weight)

if __name__ == "__main__":
    app.run(debug=True)
