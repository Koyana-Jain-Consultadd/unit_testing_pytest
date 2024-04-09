
import requests

def get_weather(city):
    url = f'https://api.weather.com/{city}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

