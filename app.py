import datetime
import random
from flask import Flask,render_template,request,session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("home.html" )

@app.route("/index")
def next():
    head = "hezup"
    return render_template("index.html", head = head )


@app.route("/isitnewyr")
def chk():
    now = datetime.datetime.now()
    yr = now.month==1 and now.date==1
    return render_template("chk.html", yr=yr)


@app.route("/link")
def link():
    return render_template("link.html")

@app.route("/game")
def game():
    return render_template("game.html" )

@app.route("/res" , methods = ["POST" , "GET"])
def res():

    if request.method == "GET":
        return "Please Submit The form"
    else:
        n = request.form.get("guess")
        x = random.randint(0,1)
        n=int(n)
        return render_template("res.html", n=n ,x=x)


@app.route("/session", methods=["GET", "POST"])
def ses():
    if session.get("notes") == None:
        session["notes"] = []
    if request.method == "POST":
        session["notes"] = []


    if request.method == "POST":
        note = request.form.get("n")
        session["notes"].append(note)

    return render_template("ses.html", notes=session["notes"])
