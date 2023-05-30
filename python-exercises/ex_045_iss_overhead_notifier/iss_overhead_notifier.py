import datetime
import requests
import smtplib
import time


URL_SUN = 'https://api.sunrise-sunset.org/json'
URL_ISS = 'https://api.open-notify.org/iss-now.json'
MY_LATITUDE = -19.7932859
MY_LONGITUDE = -43.9727293
# Belo Horizonte
GMAIL_SMTP = 'smtp.gmail.com'
MY_EMAIL = 'smtpyapptest@gmail.com'
PASSWORD = 'xgkqvlapyfnhqowj'
#abcd1234()


def is_iss_overhead():
    iss_response = requests.get(url=URL_ISS)
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_location']['longitude'])

    # Checks if ISS is close to my position
    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5:
        return True


def is_night():
    parameters = {
        'lat': MY_LATITUDE,
        'lng': MY_LONGITUDE
    }
    sun_response = requests.get(url=URL_SUN, params=parameters)
    sun_response.raise_for_status()
    data = sun_response.json()
    sunrise = int(data['results']['sunrise'])
    sunset = int(data['results']['sunset'])
    
    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(GMAIL_SMTP, 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='fernando.aaf@hotmail.com', msg='Subject: ISS Notifier \n\n ISS is above you!')
        connection.close

        time.sleep(60)