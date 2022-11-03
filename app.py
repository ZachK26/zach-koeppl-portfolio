from flask import (Flask,
render_template,
request,
session,
redirect,
url_for)
from flask_frozen import Freezer

app = Flask(__name__)
app.secret_key = 'keylol'

#freezer = Freezer(app)
#
#if __name__ == '__main__':
#    freezer.freeze()

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template('index.html')