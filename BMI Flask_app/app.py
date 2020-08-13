from flask import Flask, render_template, request, json


app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    name = ''
    bmi= ''
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        w = float(request.form.get('userw'))
        h = float(request.form.get('userh'))
        bmi = calc_bmi(w,h)
    return render_template('bmi.html',  name=name, bmi=bmi)

def calc_bmi(w,h):
    return round(w/(h**2),2)


@app.route('/test')
def test():
    return "testuje!"

if __name__ == "__main__":
    app.run(debug=True)
