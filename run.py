import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there</h1>"
#remember to change port before you will deploy app in to heroku
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')) debug=True) 