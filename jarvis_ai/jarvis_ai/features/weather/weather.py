import requests
import string
import spacy
import json

nlp = spacy.load('en_core_web_lg')


def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius


def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type


def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed


def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))


def main_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    weather_details = get_weather_data(json_data, city)
    return weather_details


def weather_app(inp):
    inp = string.capwords(inp)  # capitalize first letter of each word
    doc = nlp(f'u{inp}')  # doc is a simple string

    for ent in doc.ents:  # analyse the text
        if ent.label_ == "GPE":  # check if label is city
            city = ent.text
            weather_res = main_weather(city)
            return weather_res
        else:
            with open("configs/user_config.json", "r") as json_file:
                json_user_config = json.load(json_file)
            city = json_user_config["city"]
            weather_res = main_weather(city)
            return weather_res


if __name__ == '__main__':
    weather_details = weather_app("Temperature in Indore")
    print(weather_details)
