import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:@shivatejan1@localhost/test")
cur = scoped_session(sessionmaker(bind=engine))

def main():
    f=open('csv/flights.csv')
    reader = csv.reader(f)
    for o,d,t in reader:
        cur.execute("INSERT INTO flights (origin,destination,duration) VALUES (:origin, :destination, :duration)",
        {"origin": o, "destination": d, "duration": t})
        print(o,d,t)
    p=open('csv/pass.csv')
    reader = csv.reader(p)
    for i,n in reader:
        cur.execute("INSERT INTO passengers(f_id , name) VALUES(:f_id, :name)",{"f_id":i, "name":n })
        print(i,n)
    cur.commit()

if __name__== "__main__":
    main()
