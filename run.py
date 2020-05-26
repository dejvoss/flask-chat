import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    return "Hi" + username


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

"""remember to change port for 'port=int(os.getenv('PORT'))'before you will deploy app in to heroku or you want to use it on the gitpod"""
app.run(host=os.getenv('IP'), port='6080', debug=True)