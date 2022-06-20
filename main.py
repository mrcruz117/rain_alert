import requests
from env import api_key

lat = 25.690142
lon = -80.269402
QWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(QWM_endpoint, params=weather_params)
print()
print(response.json())
