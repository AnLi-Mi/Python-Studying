from flask import Flask, render_template, request, json


app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    
    name = ''
    weight =0
    hight =0
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        w = int(request.form.get('userw'))
        h = int(request.form.get('userh'))
        bmi = w/(h**2)
    return render_template('bmi.html',  name=name, w=w, h=h, bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)
