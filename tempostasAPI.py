import requests
from configparser import ConfigParser

weatherURL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
config_file = "configure.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(location):
    resultWeather = requests.get(weatherURL.format(location,api_key))
    if resultWeather:
        json = resultWeather.json()
        # we have a tuple of: location, temp in C,K,F
        # and weather (main,secondary) descriptions
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin-273.15)*9/5+32
        main_description = json['weather'][0]['main']
        secondary_description = json['weather'][0]['description']
        finalWeather=(city,country,temp_celsius,temp_kelvin,temp_fahrenheit,main_description,secondary_description)
        return finalWeather
    else:
        return None