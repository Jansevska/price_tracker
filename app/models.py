from app import db
from datetime import datetime



class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)

    # def __repr__(self):
    #     return f'<Price {self.value}>'

    def get_all_prices():
        return Price.query.all()
    # def get_all_prices(cls):
    #     return cls.query.all()

    def save_price(price_obj):
        db.session.add(price_obj)
        db.session.commit()
