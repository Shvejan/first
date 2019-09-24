import datetime
from flask import Flask,render_template\

app = Flask(__name__)

@app.route("/")
def index():
    return "hola wrld!"

@app.route("/ht")
def next():
    head = "hezup"
    return render_template("index.html", head = head )


@app.route("/isitnewyr")
def chk():
    now = datetime.datetime.now()
    yr = now.month==1 and now.date==1
    return render_template("chk.html", yr=yr)
