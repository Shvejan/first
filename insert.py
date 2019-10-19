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


def main():
    f=open('flights.csv')
    reader = csv.reader(f)
    for o,d,t in reader:
        cur.execute("INSERT INTO flights (origin,destination,duration) VALUES (%s, %s, %s)", (o, d, t))
        print(o,d,t)
    p=open('pass.csv')
    reader = csv.reader(p)
    for i,n in reader:
        cur.execute("INSERT INTO passengers(f_id , name) VALUES(%s,%s)",(i,n))
        print(i,n)
    conn.commit()

if __name__== "__main__":
    main()
