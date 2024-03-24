# Importing necessary libraries
import requests # For making HTTP requests
import os # For accessing environment variables
from plyer import notification # For sending desktop notifications
from apscheduler.schedulers.blocking import BlockingScheduler # For scheduling tasks
import pytz # For handling timezones


# Make sure your Flask app is created before importing models
from app import create_app
app = create_app()

# Now import your models
from app.models import Price  # Import the model directly

# Retrieving API authorization token stored as an environment variable
AUTH = os.environ['AUTH']

# Setting up the headers for the API request
headers = {
    'Authorization': f'Bearer {AUTH}',  # Ensure this matches the expected header format for Bearer tokens
    'Content-Type': 'application/json'
}

# Defining the main function to avoid running on imports
def main():
    with app.app_context():  # Ensures that the Flask app context is available
        response = requests.get('https://api.brightdata.com/dca/dataset?id=j_ltyvg6sapup27klqw', headers=headers)
        data = response.json()
        print(data)  # Printing the JSON response to the console

        # Assuming data is a list of dictionaries containing 'finalPrice' keys
        for obj in data:
            price_value = obj.get('finalPrice', {}).get('value')
            if price_value:
                # Save each price using your Price model method
                Price.save_price(price_value)

        scheduler = BlockingScheduler(timezone=pytz.timezone('UTC'))
        scheduler.add_job(send_notification, 'interval', minutes=1) # hours=24
        scheduler.start()

def send_notification():
    with app.app_context():
        prices = Price.get_all_prices()
        if len(prices) >= 2 and prices[-1].value < prices[-2].value:
            notification.notify(
                title='Price Alert',
                message=f'The price of the product has dropped to ${prices[-1].value}.',
                app_icon='icon.ico',  # Path to your icon
                timeout=10
            )

if __name__ == '__main__':
    main()