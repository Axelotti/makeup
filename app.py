from flask import Flask
from flask import render_template, request


app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

def readQuestion(filepath):
    questionCol = []
    with open(filepath, 'r') as f:
        for column in range(5):
            questions = []
            for i in range(5):
                questions.append(f.readline())
            print(questions)
            questionCol.append(questions)
        return questionCol


@app.route("/")
def homePage():
    name = 'Welcome to Soccer Jeopardy'
    return render_template('base.html', name = name)

@app.route("/Questions/<row>/<column>")
def Questions(row,column):
    Qnum = '1'
    questions = readQuestion('static/questions.txt')
    return render_template('questions.html', Qnum = Qnum, questions = questions, row= int(row), column =int(column))

@app.route("/Questions",methods=['POST','GET']) 
def submission(): 
    if request.method=="POST":
        user = request.form["answer"]
        print(user)

        return redirect(url_for("base.html", usr=user))
    else:
        return render_template("base.html")
    

