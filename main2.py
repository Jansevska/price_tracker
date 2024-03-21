import requests
import os
from plyer import notification
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

AUTH2 = os.environ['AUTH2']

headers = {
    'Authorization': f'{AUTH2}',
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


def send_notification():
    for price in prices:
        if price < 349: 
            print(f'The price of the product has dropped to ${price}.')
            # Send notification using Plyer library
            notification.notify(
                title='Price Alert',
                message=f'The price of the product has dropped to ${price}.',
                app_icon='icon.ico',
                timeout=10
            )

scheduler.add_job(send_notification, 'interval', minutes=1 ) #hours=24

scheduler.start()