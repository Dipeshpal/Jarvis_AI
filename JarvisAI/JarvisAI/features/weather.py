import requests


def get_weather(*args, **kwargs):
    print("Getting weather")
    query = kwargs.get("query")
    entities = kwargs.get("entities")
    city = "Indore"
    if len(entities) == 0:
        city = [entity[0] for entity in entities if entity[1] == "GPE"][0]
        if len(city) == 0:
            return "Unable to in which city you want to know weather"
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()
    lat = geo_data['results'][0]["latitude"]
    lon = geo_data['results'][0]["longitude"]
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    weather_data = requests.get(weather_url).json()
    temp = weather_data["hourly"]["temperature_2m"][-1]
    return f"The temperature in {city} is {temp} degrees Celsius."


if __name__ == "__main__":
    print(get_weather(entities=[("London", "GPE")]))
