from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route("/")
def homePage():
    groupName= 'Group 7:'
    name = 'Axel Cortes, Israel Lopez, Eric Villa, Erick Montenegro'
    details = readDetails('static/details.txt')
    return render_template('project.html', name = name, aboutMe = details, groupName = groupName)
