import requests
from env import api_key

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
    if (weather_code) < 700:
        will_rain = True
        break

if will_rain:
    print("Bring Umbrella")
