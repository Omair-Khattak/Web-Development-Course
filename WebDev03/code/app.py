from flask import Flask, flash
from flask import request, render_template,redirect,url_for 


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/data', methods = ['POST', 'GET'])
def submit_data():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username=='' or password == '':
            return {'status': 'Wrong credentials'}
        else:
            return {'status': 'ok'}
    return render_template("index.html",error=error)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

if __name__ == '__main__':
   app.run(debug = True)
