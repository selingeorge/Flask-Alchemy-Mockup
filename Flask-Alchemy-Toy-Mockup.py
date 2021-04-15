from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toy_db.sqlite3'

db = SQLAlchemy(app)


# Table for Raw Materials
class RawMaterials(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now)


# Table for Production Screen if any
class Production(db.Model):
    slno = db.Column(db.Integer, primary_key=True)


# Table for Dispatch Screen if any
class Dispatch(db.Model):
    slno = db.Column(db.Integer, primary_key=True)


@app.route('/<id>/<qty>')
def index(id, qty):
    raw_material = RawMaterials(id=id, qty=qty)
    db.session.add(raw_material)
    db.session.commit()
    return '<h1>Added input raw materials.</h1>'


if __name__ == '__main__':
    app.run(debug=True)