from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Price

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    price_data = db.session.execute(db.select(Price).order_by(db.desc(Price.timestamp))).scalars().all()
    prices = Price.get_all_prices()
    return render_template('display.html', prices=prices, price_data=price_data) # 
    
@main.route('/update', methods=['GET', 'POST'])
def update_prices():
    data = request.get_json()
    print(data)
    if data:  # Check if there is data
        new_price = Price(value=data['finalPrice']['value'])
        Price.save_price(new_price)
        return jsonify({'message': 'Price updated successfully'}), 200
    return jsonify({'error': 'No data provided'}), 400


# @main.route('/update', methods=['POST'])
# def update_prices():
#     data = request.json
#     for price in data:
#         save_price(price['finalPrice']['value'])
#     return redirect(url_for('main.home'))



# from app import app
# from flask import render_template

# @app.route('/')
# def index():
#     # iPad data from sqlite3
#     return render_template('index.html')

