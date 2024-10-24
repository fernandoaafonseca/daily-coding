import requests


URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = -19.7932859
MY_LNG = -43.9727293
# Belo Horizonte


parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG
}
response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(f'Sunrise: {sunrise}')
print(f'Sunset: {sunset}')