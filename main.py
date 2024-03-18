import requests
from plyer import notification

headers = {
    'Authorization': 'Bearer b033bf89-f0b3-44cf-885c-9332de54a45c',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.brightdata.com/dca/dataset?id=j_ltxdd2hgvjjbnsyua', headers=headers)

data = response.json()

print(data)