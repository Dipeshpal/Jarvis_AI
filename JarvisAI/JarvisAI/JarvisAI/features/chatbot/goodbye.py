import random
import time


def goodbye(*args, **kwargs):
    ch = ['bye', 'good bye', 'see you later', 'see you', 'good bye']
    night = ['night', 'good night']
    morning = ['morning', 'good morning']
    afternoon = ['afternoon', 'good afternoon']
    evening = ['evening', 'good evening']
    day = ['day', 'good day']
    time_now = time.strftime("%H")
    if "00" <= time_now < "12":
        return random.choice(morning)
    elif "12" <= time_now < "18":
        return random.choice(afternoon)
    elif "18" <= time_now < "24":
        return random.choice(evening)
    elif "24" <= time_now < "06":
        return random.choice(night)
    elif "06" <= time_now < "12":
        return random.choice(day)
    else:
        return random.choice(ch)
