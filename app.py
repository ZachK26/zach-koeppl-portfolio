from flask import (Flask,
render_template,
request,
session,
redirect,
url_for)

app = Flask(__name__)
app.secret_key = 'keylol'

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template('index.html')