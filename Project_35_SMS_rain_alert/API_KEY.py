import requests

lat, lng = 27.569050, 80.684875
API_KEY = "f404149f037da0886961c157562fead1"
exclude = "current,minutely,daily"
API_Endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&exclude={exclude}&appid={API_KEY}"

print(API_Endpoint)
response = requests.get(url=API_Endpoint)


weather_data_id = response.json()['weather'][0]['id']

if weather_data_id < 700:
    pass
    # send an email
    # use twilio API to send sms








