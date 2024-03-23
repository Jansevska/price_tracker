# Importing necessary libraries
import requests # For making HTTP requests
import os # For accessing environment variables
from plyer import notification # For sending desktop notifications
from apscheduler.schedulers.blocking import BlockingScheduler # For scheduling tasks
import pytz # For handling timezones
from app.models import get_all_prices


# Retrieving API authorization token stored as an enviroment variable
AUTH = os.environ['AUTH']

# Setting up the headers for the API request
headers = {
    'Authorization': f'{AUTH}', # Authorization header with the token
    'Content-Type': 'application/json' # Content type set to JSON
}

# Sending a GET request to the specified URL with the defined headers
response = requests.get('https://api.brightdata.com/dca/dataset?id=j_ltyvg6sapup27klqw', headers=headers)

# Parsing the JSON response
data = response.json()
print(data) # Printing the JSON response to the console

# Initializing a list to store prices
prices = []
# Iterating through the JSON response (object) and appending prices to the list (extracting price)
for obj in response.json():
    prices.append(obj['finalPrice']['value']) # adding the price value to the prices list

print(prices)

# Creating a scheduler to run the notification task every 24 hours (in UTC) using the BlockingScheduler class from the apscheduler library.
scheduler = BlockingScheduler(timezone=pytz.timezone('UTC'))

# Getting yesterday's price by accessing the second-to-last element in the prices list.
yesterdays_price = prices[-2]

# Creating a function to send desktop notifications when the price drops.
def send_notification():
    prices = get_all_prices()
    if len(prices) >= 2 and prices[-1].value < prices[-2].value:
        notification.notify(
            title='Price Alert',
            message=f'The price of the product has dropped to ${prices[-1].value}.',
            app_icon='icon.ico',  # Path to your icon
            timeout=10
        )

# Adding a job to the scheduler: executing send_notification function every 24 hours
scheduler.add_job(send_notification, 'interval', hours=24) #hours=24

# Starting the scheduler to execute the scheduled jobs
scheduler.start()