import requests
import pycountry


def check_command_is_for_covid_cases(command):
    try:
        command = command.title()
        country = get_country(command)
        cases = get_covid_cases(country)
        return f"The current active cases in {country} are {cases}"
    except Exception as e:
        print("Error: ", e)
        return "Sorry, I couldn't find the country you are looking for. Or server is down."


def get_country(command):  # For getting only the country name for the whole query
    for country in pycountry.countries:
        if country.name in command:
            return country.name


def get_covid_cases(country):  # For getting current covid cases
    totalActiveCases = 0
    response = requests.get('https://api.covid19api.com/live/country/' + country + '/status/confirmed').json()
    for data in response:
        totalActiveCases += data.get('Active')
    return totalActiveCases


if __name__ == '__main__':
    print(check_command_is_for_covid_cases('active Covid India cases?'))  # Example
