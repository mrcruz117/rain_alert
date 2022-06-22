import requests
from twilio.rest import Client
from env import api_key, twilio_SID, twilio_number, twilio_auth_token

lat = 25.690142
lon = -80.269402
QWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(QWM_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False

for i in range(12):
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]
    print(weather_code)
    if (weather_code) < 900:
        will_rain = True
        break

if will_rain:
    client = Client(twilio_SID, twilio_auth_token)

    message = client.messages.create(
        body="Remember to bring an umbrella! ☔",
        from_=twilio_number,
        to='+17862014285'
    )

print(message.status)
