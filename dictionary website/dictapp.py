from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
import json

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    else:
        return "the word doesn't exist"


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:akshay22@localhost/definition_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="mydata"
    id=db.Column(db.Integer, primary_key=True)
    word_=db.Column(db.String(200))
    definition_=db.Column(db.String(2000))
    email_=db.Column(db.String(120))
    age_=db.Column(db.Integer)

    def __init__(self,word_,definition_,email_,age_):
        self.definition_=definition_
        self.email_=email_
        self.age_=age_
        self.word_=word_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        word=request.form["word_name"]
        age=request.form["age_name"]
        definition=translate(word)
        send_email(email, word, definition)
        data=Data(word,definition,email,age)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

if __name__=='__main__':
    app.debug=True
    app.run()
