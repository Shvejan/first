from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
