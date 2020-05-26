import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello there</h1>"


# remember to change port for 'port=int(os.getenv('PORT'))'before you will deploy app in to heroku or you want to use it on the gitpod
app.run(host=os.getenv('IP'), port='6080', debug=True)