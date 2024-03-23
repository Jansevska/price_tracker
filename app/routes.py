from flask import Blueprint, render_template, request, redirect, url_for
from .models import save_price, get_all_prices

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    prices = get_all_prices()
    return render_template('display.html', prices=prices)

@main.route('/update', methods=['POST'])
def update_prices():
    data = request.json
    for price in data:
        save_price(price['finalPrice']['value'])
    return redirect(url_for('main.home'))



# from app import app
# from flask import render_template

# @app.route('/')
# def index():
#     # iPad data from sqlite3
#     return render_template('index.html')

