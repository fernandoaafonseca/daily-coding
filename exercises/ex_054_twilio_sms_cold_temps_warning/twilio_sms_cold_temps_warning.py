import datetime
import requests
from urllib.parse import quote

from twilio.rest import Client

from data.twilio_account import MY_PHONE_NUMBER
from data.twilio_account import MY_TWILIO_PHONE_NUMBER
from data.twilio_account import TWILIO_ACCOUNT_SID
from data.twilio_account import TWILIO_AUTH_TOKEN


OPEN_METEO_ENDPOINT = 'https://api.open-meteo.com/v1/forecast'
timezone = 'America/Sao_Paulo'
encoded_timezone = quote(timezone)
BH_lat = -19.813150
BH_long = -43.963380


def get_weather():
    weather_params = {'latitude': BH_lat,
                      'longitude': BH_long,
                      'current_weather': 'true',
                      'hourly': 'temperature_2m',
                      'timezone': encoded_timezone
                      }
    response = requests.get(OPEN_METEO_ENDPOINT, params=weather_params)

    response.raise_for_status()
    print(f'RESPONSE: {response.status_code}')
    print()

    return response


def detect_cold_temps():
    cold_timestamps_indexes = []
    cold_temps_detected = False
    for hour in range(12):
        new_temp = hourly_weather["temperature_2m"][hour]
        if new_temp <= 17:
            cold_temps_detected = True
            cold_timestamps_indexes.append(hour)

    return cold_temps_detected, cold_timestamps_indexes


def generate_msg():
    if cold_temps_detected:
        start_index = cold_timestamps_indexes[0]
        end_index = cold_timestamps_indexes[-1]

        min_temp = min(hourly_weather['temperature_2m'][
            start_index:end_index])
        max_temp = max(hourly_weather['temperature_2m'][
            start_index:end_index])

        weather_time = hourly_weather['time']
        start_time = datetime.datetime.fromisoformat(
            weather_time[start_index])
        end_time = datetime.datetime.fromisoformat(
            weather_time[end_index])

        start_time_str = start_time.strftime('%d-%m-%Y at %H:%M')
        end_time_str = end_time.strftime('%d-%m-%Y at %H:%M')

        message = f'It will be cold in between {start_time_str} and {end_time_str}, with a minimum temperature of {min_temp}ºC and a maximum of {max_temp}ºC.'

    else:
        message = 'It won\'t be cold for the next twelve hours.'

    return message


def twilio_send_sms(sms_msg):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    twilio_phone_num = MY_TWILIO_PHONE_NUMBER
    contact_num = MY_PHONE_NUMBER

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_msg,
        from_=twilio_phone_num,
        to=contact_num
    )
    print(f'Twilio SMS SID: {message.sid}')
    print(f'Twilio status: {message.status}')


response = get_weather()
weather = response.json()
hourly_weather = weather['hourly']
cold_temps_detected, cold_timestamps_indexes = detect_cold_temps()
sms_msg = generate_msg()
twilio_send_sms(sms_msg)
