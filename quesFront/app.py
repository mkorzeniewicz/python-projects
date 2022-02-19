from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from searchVisualizer import myLovelyDef
import json
app = Flask(__name__)

@app.route("/")
def home():
    return "hi"
@app.route("/index")

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        print(request)
        datafromjs = request.form['mydata']
        result = json.dumps(myLovelyDef(datafromjs))
        resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        #return render_template('login.html', message='')
    if request.method == 'GET':
        return "huj"

if __name__ == "__main__":
    app.run(debug = True)