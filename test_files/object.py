import os
from class2 import *
from classes import *
from flask import Flask, render_template, request

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    p = person(name = "jp", age=21)
    db.session.add(p)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
