import datetime


def greet(*args, **kwargs):
    time = datetime.datetime.now().hour
    if time < 12:
        return "Hi, Good Morning"
    elif 12 <= time < 18:
        return "Hi, Good Afternoon"
    else:
        return "Hi, Good Evening"


def goodbye(*args, **kwargs):
    return "Goodbye"