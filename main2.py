import requests
import os
from plyer import notification
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

AUTH = os.environ['AUTH']

headers = {
    'Authorization': f'{AUTH}',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.brightdata.com/dca/dataset?id=j_ltyvg6sapup27klqw', headers=headers)

data = response.json()
print(data)

prices = []
for obj in response.json():
    prices.append(obj['finalPrice']['value'])

print(prices)

scheduler = BlockingScheduler(timezone=pytz.timezone('UTC'))

yesterdays_price = prices[-2]

def send_notification():
    for price in prices:
        if price < yesterdays_price: 
            print(f'The price of the product has dropped to ${price}.')
            # Send notification using Plyer library
            notification.notify(
                title='Price Alert',
                message=f'The price of the product has dropped to ${price}.',
                app_icon='icon.ico',
                timeout=10
            )

scheduler.add_job(send_notification, 'interval', hours=24) #hours=24

scheduler.start()