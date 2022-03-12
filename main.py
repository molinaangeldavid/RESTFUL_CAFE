from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record

@app.route('/random')
def random_cafe():
    number_id = random.randint(1,21)
    random_id = Cafe.query.filter_by(id=number_id).first()
    return jsonify(id=random_id.id,
                    name=random_id.name, 
                    map_url=random_id.map_url,
                    img_url=random_id.img_url,
                    location=random_id.location,
                    seats=random_id.seats,
                    has_toilet=random_id.has_toilet,
                    has_wifi=random_id.has_wifi,
                    has_sockets=random_id.has_sockets,
                    can_take_calls=random_id.can_take_calls,
                    coffee_price=random_id.coffee_price
                    )
    
@app.route('/all')
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    print(c.name for c in all_cafes)
    

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
