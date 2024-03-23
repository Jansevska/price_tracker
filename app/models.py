from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import current_app as app

db = SQLAlchemy()

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Price {self.value}>'

def init_app(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()

def save_price(price_value):
    new_price = Price(value=price_value)
    db.session.add(new_price)
    db.session.commit()

def get_all_prices():
    return Price.query.all()
