import os
import requests
import sqlite3
from datetime import datetime

AUTH2 = os.environ['AUTH2']

# Configuration
DATABASE = 'product_data.db'
BRIGHTDATA_URL = 'https://api.brightdata.com/dca/dataset?id=j_ltxdd2hgvjjbnsyua'
HEADERS = {
    'Authorization': f'{AUTH2}',
    'Content-Type': 'application/json'
}

# Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS product_prices (
            date TEXT,
            price REAL
        );
    ''')
    conn.commit()
    conn.close()

# Fetch product data from Bright Data
def fetch_product_data():
    response = requests.get(BRIGHTDATA_URL, headers=HEADERS)
    data = response.json()
    return data  # Assuming this returns a JSON with a 'price' field

# Log product data into the database
def log_product_data(price):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO product_prices (date, price) VALUES (?, ?)', (datetime.now().strftime("%Y-%m-%d"), price))
    conn.commit()
    conn.close()

# Check for price drops
def check_price_drop():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT date, price FROM product_prices ORDER BY date DESC LIMIT 2')
    prices = c.fetchall()
    conn.close()

    if len(prices) == 2:
        latest_price = prices[0][1]
        previous_price = prices[1][1]
        if latest_price < previous_price:
            print(f"Price drop detected! New price: ${latest_price} (was ${previous_price})")
            # Here you can add more actions, like sending a notification
        else:
            print("No price drop detected.")
    else:
        print("Not enough data for comparison.")

# Main routine
def main():
    init_db()  # Ensure the database and table exist
    product_data = fetch_product_data()
    if 'price' in product_data:
        log_product_data(product_data['price'])
        check_price_drop()
    else:
        print("No price data found in the response.")

if __name__ == "__main__":
    main()
    

# response = requests.get(F'{BRIGHTDATA_URL}', headers=headers)

# data = response.json()

# print(data)