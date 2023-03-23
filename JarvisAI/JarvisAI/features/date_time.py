import datetime


def date_time(*args, **kwargs):
    query = kwargs['query']
    if 'time' in query:
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif 'date' in query:
        return datetime.datetime.now().strftime("%d/%m/%Y")
    else:
        return "Sorry, I don't know how to handle this intent."
