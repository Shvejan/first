from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:@shivatejan1@localhost/test")
cur = scoped_session(sessionmaker(bind=engine))


def main():
    fli = cur.execute("SELECT id,origin,destination,duration FROM flights").fetchall()
    for i,o,d,t in fli:
        print(f"flight:  {i}:  {o},{d},{t} ")
    n = (input("enter a flight id: "))
    flight = cur.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
                        {"id": n}).fetchone()
    if flight is None:
        print("Error: No such flight.")
        return


    names= cur.execute("SELECT name FROM passengers WHERE f_id = :f_id ",{"f_id": n}).fetchall()
    if len(names)==0:
        print("no passengers found")
    else:
        for na in names:
            na = str(na)
            na = na[2:-3]
            print(na)

if __name__== "__main__":
    main()
