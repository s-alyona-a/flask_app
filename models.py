from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servey.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)
    education = db.Column(db.Text)
    linguistics = db.Column(db.String)


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)


'''with app.app_context():
    db.create_all()
    data = [(1, 'Я случайно упал со стула'), (2, 'Я нечаянно упал со стула'),
        (3, 'Ваза случайно разбилась'), (4, 'Ваза нечаянно разбилась'),
        (5, 'Мы случайно встретились'), (6, 'Мы нечаянно встретились'),
        (7, 'Он позвонил не случайно'), (8, 'Он позвонил не нечаянно'),
        (9, 'Петя случайно попал в хор'), (10, 'Петя нечаянно попал в хор')]
    for tup in data:
        tup1 = Questions(id = tup[0], text = tup[1])
        db.session.add(tup1)
    db.session.commit()'''