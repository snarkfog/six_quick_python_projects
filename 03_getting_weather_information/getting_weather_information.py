import requests
from pprint import pprint

API_key = "87cc9b57d03c8f6c9ef12304f779516a"
city = input("Enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city
weather_data = requests.get(base_url).json()
pprint(weather_data)
