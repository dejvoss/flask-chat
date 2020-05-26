import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    """Get all of the messages and seperate them with a br """
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

"""remember to change port for 'port=int(os.getenv('PORT'))'before you will deploy app in to heroku or you want to use it on the gitpod"""
app.run(host=os.getenv('IP'), port='6080', debug=True)