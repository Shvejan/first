import os
import csv
import psycopg2
import random
from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


conn = psycopg2.connect(
    database="test",
    user="postgres",
    password = "@shivatejan1",
    host = "localhost",
    port="5432"
)
cur=conn.cursor()


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
        note = request.form.get("n")
        session["notes"].append(note)

    return render_template("ses.html", notes=session["notes"])


@app.route("/db")
def db():

    cur.execute("SELECT * FROM flights ")
    rows = cur.fetchall()
    return render_template("db.html" , rows = rows)

@app.route("/book", methods = ["POST" , "GET"])
def book():
    if request.method == "GET":
        return db()
    fly = request.form.get("fly")
    return render_template("book.html",fly=fly)

@app.route("/confirm", methods = ["POST"])
def confirm():
    name = request.form.get("nam")
    fly = int(request.form.get("fly"))
    cur.execute("INSERT INTO passengers(f_id , name) VALUES(%s,%s)",(fly,name))
    conn.commit()
    return render_template("confirm.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/added", methods = ["POST"])
def added():
    origin = request.form.get("origin")
    dest = request.form.get("dest")
    dur = request.form.get("dur")
    cur.execute("INSERT INTO flights(origin,destination,duration) VALUES(%s,%s,%s)",(origin, dest,dur))
    conn.commit()
    return render_template("added.html")


@app.route("/pass" , methods = ["POST" , "GET"])
def pas():
    if request.method == "GET":
        return db()
    else:
        error = ""
        n=[]
        fid = request.form.get("fid")
        try:
            cur.execute("SELECT id FROM flights WHERE id = %s ",(fid))
            f = cur.fetchone()
        except (Exception):
            error = "no flights  found"
        else:
                cur.execute("SELECT name FROM passengers WHERE f_id = %s ",(fid))
                names  = cur.fetchall()
                if len(names)==0:
                    error = "no passengers found"
                for na in names:
                    na = str(na)
                    n.append(na[2:-3])
                    print(na[2:-3])

        return render_template("pass.html",n = n,error = error)
