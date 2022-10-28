import requests


def get_me_suggestion(*args, **kwargs):
    url = 'http://www.boredapi.com/api/activity'
    response = requests.get(url)
    return response.json()['activity']
