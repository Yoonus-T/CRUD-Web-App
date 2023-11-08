from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class userModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String())
    gender = db.Column(db.String())
    age = db.Column(db.String())
    address = db.Column(db.String(250))


    def __init__(self, first_name, last_name, email, gender, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.age = age
        self.address = address

    def __repr__(self):
        return f"user(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
