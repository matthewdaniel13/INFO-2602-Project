from App.models import Route
from App.database import db

def add_route(name, route_description, destination_location_id, source_location_id):
    newroute = Route(name=name, route_description=route_description,source_location_id=source_location_id, destination_location_id=destination_location_id)
    db.session.add(newroute)
    db.session.commit
    return newroute

def search_route(source_location_id, destination_location_id):
    return Route.query.filter_by(source=source_location_id, dest=destination_location_id).all()

