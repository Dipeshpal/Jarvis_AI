import requests
import spacy

try:
    nlp = spacy.load('en_core_web_sm')
except Exception as e:
    print(e)
    print(str(e).split('.')[0] + ". Please wait while we download the model")
    import os

    os.system('python -m spacy download en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')


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
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + (
        "The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(
            city, weather_type, temperature, wind_speed))


def main_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_address = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    if json_data['cod'] == 200:
        return get_weather_data(json_data, city)
    else:
        return "I am sorry, I could not find the weather for {}".format(city) + ".\nError code: {}".format(
            json_data['message'])


def weather_app(city):
    weather_res = main_weather(city)
    return weather_res


def get_weather(inp_command, *args, **kwargs):
    doc = nlp(inp_command)
    city = None
    for ent in doc.ents:
        city = ent.text

    if city is not None:
        return weather_app(city)
    else:
        url = 'http://ipinfo.io/json'
        response = requests.get(url)
        data = response.json()
        city = data.get('city')
        return weather_app(city)


if __name__ == "__main__":
    print(get_weather('what is the temperature in Tokyo?'))
