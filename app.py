from flask import Flask
from flask import render_template, request

class Question:
    def __init__(self, question = 0, answer= 0, row= 0, col= 0, marked= 0):
        self.question = question
        self.answer = answer
        self.row = row 
        point = [100,200,300]
        self.rowpoints = point[self.row]
        self.col = col 
        cat = ["player", "world cup 2022", "leagues", "clubs", "icons"]
        self.category = cat[self.col]
        self.mark = marked


            
myQuestion = Question()


app = Flask(__name__)

P1 = 7

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
    return render_template('homepage.html', name = name)

@app.route("/gamePage")
def gamePage():
    global P1 
    P1 += 100
    print(P1)
    name = 'Soccer Jeopardy'
    return render_template('base.html', name = name)

@app.route("/Questions/<row>/<column>", methods=['POST','GET'])
def Questions(row,column, answer=None):
    Qnum = '1'
    questions = readQuestion('static/questions.txt')
    if request.method=="POST":
        answer = request.form["answer"]
        print(answer)
    return render_template('questions.html', Qnum = Qnum, questions = questions, row= int(row), column =int(column), answer=answer)