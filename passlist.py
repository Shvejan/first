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
    cur.execute("SELECT id,origin,destination,duration FROM flights")
    fli = cur.fetchall()
    for i,o,d,t in fli:
        print(f"flight:  {i}:  {o},{d},{t} ")
    n = (input("enter a flight id: "))
    try:
        cur.execute("SELECT id FROM flights WHERE id = %s ",(n))
        f = cur.fetchone()
    except (Exception):
        print("no flights  found")
    else:
            cur.execute("SELECT name FROM passengers WHERE f_id = %s ",(n))
            names  = cur.fetchall()
            if len(names)==0:
                print("no passengers found")
            for na in names:
                na = str(na)
                na = na[2:-3]
                print(na)

if __name__== "__main__":
    main()
