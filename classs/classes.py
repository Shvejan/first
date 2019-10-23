from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class flights(db.Model):
    __tablename__="flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class passengers(db.Model):
    __tablename__="passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    f_id =db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
