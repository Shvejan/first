import os
from flask import Flask,session,render_template,request
from classs.class2 import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/",methods = ["POST","GET"])
def per():
    if request.method == "POST":
        n = request.form.get("na")
        a = request.form.get("ag")
        p = person(name = n, age = a)
        db.session.add(p)
        db.session.commit()
    ppl = person.query.all()
    return render_template("per.html", ppl=ppl)
