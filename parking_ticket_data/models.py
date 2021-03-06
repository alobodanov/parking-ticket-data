# from .app import db
from .main_code import db


class ParkingTickets(db.Model):
    __tablename__ = 'parking_tickets'

    id = db.Column(db.Integer, primary_key=True)
    date_of_infraction = db.Column(db.Integer, nullable=True)
    infraction_code = db.Column(db.Integer, nullable=True)
    infraction_description = db.Column(db.String(1000), nullable=True)
    set_fine_amount = db.Column(db.Float, nullable=True)
    time_of_infraction = db.Column(db.Integer, nullable=True)
    location2 = db.Column(db.String(100), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<ParkingTickets %r>' % (self.location2)