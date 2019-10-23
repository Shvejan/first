import os
from class2 import *
from flask import Flask,session
import csv
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    per = open("csv/person.csv")
    reader = csv.reader(per)
    for n,a in reader:
        x = person(name = n, age = a)
        db.session.add(x)
        db.session.commit()
if __name__ == '__main__':
    with app.app_context():
        main()
