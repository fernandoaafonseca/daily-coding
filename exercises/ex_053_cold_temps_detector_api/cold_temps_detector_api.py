import datetime
import requests
from urllib.parse import quote


OPEN_METEO_ENDPOINT = 'https://api.open-meteo.com/v1/forecast'
timezone = 'America/Sao_Paulo'
encoded_timezone = quote(timezone)
weather_params = {'latitude': -19.813150,
                  'longitude': -43.963380,
                  'current_weather': 'true',
                  'hourly': 'temperature_2m',
                  'timezone': encoded_timezone
                  }
response = requests.get(OPEN_METEO_ENDPOINT, params=weather_params)

response.raise_for_status()
print(f'RESPONSE: {response.status_code}')
print()

weather = response.json()
hourly_weather = weather['hourly']
cold_timestamps_indexes = []
cold_temps_detected = False
for hour in range(12):
    new_temp = hourly_weather["temperature_2m"][hour]
    if new_temp <= 17:
        cold_temps_detected = True
        cold_timestamps_indexes.append(hour)

if cold_temps_detected:
    print('Bring a cold sweater!')
    print()
    
    start_index = cold_timestamps_indexes[0]
    end_index = cold_timestamps_indexes[-1]

    min_temp = min(hourly_weather["temperature_2m"][
        start_index:end_index])
    max_temp = max(hourly_weather["temperature_2m"][
        start_index:end_index])
    
    weather_time = hourly_weather["time"]
    start_time = datetime.datetime.fromisoformat(
        weather_time[start_index])
    end_time = datetime.datetime.fromisoformat(
        weather_time[end_index])

    start_time_str = start_time.strftime('%d-%m-%Y at %H:%M')
    end_time_str = end_time.strftime('%d-%m-%Y at %H:%M')
    
    print(
        f'It will be cold in between {start_time_str} and {end_time_str}, with a minimum temperature of {min_temp}ºC and a maximum of {max_temp}ºC.')
else:
    print('It won\'t be cold for the next twelve hours')
