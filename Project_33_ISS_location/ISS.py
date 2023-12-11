import requests
from datetime import datetime
import time

import smtplib
MY_EMAIL = "pycodedemon@gmail.com"
PASSWORD = 'atlxhbcxjnbttzgo'

MY_LAT = 27.568780
MY_LNG = 80.684279


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]['longitude'])
    latitude = float(data["iss_position"]['latitude'])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if iss_overhead() and is_night():
    time.sleep(60)
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=MY_EMAIL, password=PASSWORD)
    mail.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="jatingupta261001@gmail.com",
        msg="Subject:Look Up\n\nThe ISS is overhead in the sky!"
    )
