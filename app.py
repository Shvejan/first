import datetime
import random
from flask import Flask,render_template,request

app = Flask(__name__)

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

@app.route("/res" , methods = ["POST"])
def res():
    n = request.form.get("guess")
    x = random.randint(0,1)

    n=int(n)
    return render_template("res.html", n=n ,x=x)
