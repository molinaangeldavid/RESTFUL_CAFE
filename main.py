from flask import Flask, jsonify, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hELLO'
db = SQLAlchemy(app)
Bootstrap(app)


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
    
    def to_dict(self):
        return {column.name: getattr(self,column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record

@app.route('/random')
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    a_cafe = random.choice(all_cafes)
    # random_id = Cafe.query.filter_by(id=number_id).first()
    return jsonify(id=a_cafe.id,
                    name=a_cafe.name, 
                    map_url=a_cafe.map_url,
                    img_url=a_cafe.img_url,
                    location=a_cafe.location,
                    seats=a_cafe.seats,
                    has_toilet=a_cafe.has_toilet,
                    has_wifi=a_cafe.has_wifi,
                    has_sockets=a_cafe.has_sockets,
                    can_take_calls=a_cafe.can_take_calls,
                    coffee_price=a_cafe.coffee_price
                    )
#First option
# @app.route('/all')
# def all_cafes():
#     all_cafes = db.session.query(Cafe).all()
#     return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
        
# Second option
@app.route('/all')
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafes = []
    for c in all_cafes:
        cafe = {
        'name':c.name, 
        'map_url':c.map_url,
        'img_url':c.img_url,
        'location':c.location,
        'seats':c.seats,
        'has_toilet':c.has_toilet,
        'has_wifi':c.has_wifi,
        'has_sockets':c.has_sockets,
        'can_take_calls':c.can_take_calls,
        'coffee_price':c.coffee_price
        }
        cafes.append(cafe)
    return jsonify(cafe=[c for c in cafes])    
        
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    if request.method == 'POST':
        cafe_name = request.form.get('cafe')
        map_url_request = request.form.get('map_url')
        img_url_request = request.form.get('img_url')
        location_request = request.form.get('location')
        seats = request.form.get('seats')
        has_toilet_request = bool(request.form.get('has_toilet'))
        has_wifi_request = bool(request.form.get('has_wifi'))
        has_sockets_request = bool(request.form.get('has_sockets'))
        can_take_calls_request = bool(request.form.get('can_take_calls'))
        coffee_price_request = request.form.get('coffee_price')
    add_file = Cafe(name=cafe_name,
                    map_url=map_url_request,
                    img_url=img_url_request,
                    location=location_request,
                    has_toilet=has_toilet_request,
                    seats=seats,
                    has_wifi=has_wifi_request,
                    has_sockets=has_sockets_request,
                    can_take_calls=can_take_calls_request,
                    coffee_price=coffee_price_request)
    db.session.add(add_file)
    db.session.commit()
    return jsonify(response = {
        'sucess': 'Succesfully add the new Cafe'     
    })
        

## HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:id_cafe>',methods=['PATCH'])
def update_price(id_cafe):
    cafe = db.session.query(Cafe).filter_by(id=id_cafe).first()
    new_price = request.args.get('new_price')
    if cafe:
        cafe.coffee_price = f'${new_price}'
        db.session.commit()
        return jsonify(Sucess='Succesfully updated the price'),200
    else:
        return jsonify(error={
            'Not Found': 'The id that you put is not the correct'
        }), 404


## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
