from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OrderPassenger(db.Model):
    __tablename__ = 'orders_irish'

    id = db.Column(db.Integer, primary_key=True)
    from_place = db.Column(db.ForeignKey("places_irish.id"))
    to_place = db.Column(db.ForeignKey("places_irish.id"))
    passenger_id = db.Column(db.ForeignKey("users_irish.id"))
    date_order = db.Column(db.Date)
    period_order = db.Column(db.Numeric, nullable=False)
    everyday = db.Column(db.Boolean)
    created_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return self.id


class TripDriver(db.Model):
    __tablename__ = 'trips_irish'

    id = db.Column(db.Integer, primary_key=True)
    from_place = db.Column(db.ForeignKey("places_irish.id"))
    to_place = db.Column(db.ForeignKey("places_irish.id"))
    driver_id = db.Column(db.ForeignKey("users_irish.id"))
    seat = db.Column(db.Numeric, nullable=False)
    pay = db.Column(db.Numeric, nullable=False)
    date_order = db.Column(db.String(300))
    period_order = db.Column(db.Numeric, nullable=False)
    everyday = db.Column(db.Boolean)
    comment = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.id


class User(db.Model):
    __tablename__ = 'users_irish'

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(32), nullable=False, unique=True)
    key = db.Column(db.String(32), nullable=False, unique=True)
    contact = db.Column(db.String(32), nullable=False, unique=True)
    created_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # block = db.Column(db.Boolean)

    @staticmethod
    def getkey(userid: int) -> str:
        print(userid)
        userkey = User.query.get(userid)

        if userkey is not None:
            return userkey.key

class Place(db.Model):
    __tablename__ = 'places_irish'

    id = db.Column(db.Integer, primary_key=True)
    name_place = db.Column(db.String(64), nullable=False, unique=True, index=True)

    @staticmethod
    def getidtown(town: str) -> int:
        townid = Place.query.filter_by(name_place=town.title()).first()
        if townid is not None:
            return townid.id
