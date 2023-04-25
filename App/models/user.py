from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    username =  db.Column(db.String(255), unique=True, primary_key = True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    first_name = db.Column(db.String(120), nullable = False)
    last_name = db.Column(db.String(120), nullable = False)
    address = db.Column(db.String(120), nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120))
    zipcode = db.Column(db.Integer)
    country = db.Column(db.String, nullable = False)


    def __init__(self, username, password, email, first_name, last_name, address, city, state, zipcode, country):
        self.username = username
        self.set_password(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

    def get_json(self):
        return{
            'username': self.username,
            'email':self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode,
            'country': self.country
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Location(db.Model):
    location_id = db.Column(db.String(120), unique = True, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    latitude = db.Column(db.String(255), nullable = False)
    longtitude = db.Column(db.String(255), nullable = False)

    def __init__(self, name, latitude, longtitude):
        self.name = name
        self.latitude = latitude
        self.longtitude = longtitude

    def get_json(self):
        return{
            'location_id': self.location_id,
            'name': self.name,
            'latitude': self.latitude,
            'longtitude': self.longtitude
        }

class Route(db.Model):
    route_id = db.Column(db.String(120), unique = True, primary_key = True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.username') )
    source_location_id = db.Column(db.String(255), db.ForeignKey('location.location_id'))
    destination_location_id = db.Column(db.String(255), db.ForeignKey('location.location_id'))
    name = db.Column(db.String(255), unique = True, nullable = False)
    route_description = db.Column(db.String(255), nullable = False)

    def __init__(self, route_description, name, user_id, source_location_id, destination_location_id):
        self.route_description = route_description
        self.name = name
        self.user_id = user_id
        self.source_location_id = source_location_id
        self.destination_location_id = destination_location_id

    def get_json(self):
        return{
        'route_id': self.route_id,
        'user_id': self.user_id,
        'source_location_id': self.source_location_id,
        'destination_location_id': self.destination_location_id,
        'name': self.name,
        'route_description': self.route_description
    }


