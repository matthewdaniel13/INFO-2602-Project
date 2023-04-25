from App.models import User
from App.database import db

def create_user(username, password, first_name, last_name, address, city, state, country, email, zipcode):
    newuser = User(username=username, password=password, first_name=first_name, last_name=last_name,address=address,city=city, 
    state=state, country=country, email=email, zipcode=zipcode)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(username):
    return User.query.get(username)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(username):
    user = get_user(username)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    