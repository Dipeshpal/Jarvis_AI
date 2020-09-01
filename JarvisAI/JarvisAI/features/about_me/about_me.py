

def about_me(data=None, model=None):
    user_config = data['user_config']
    name = user_config["user_name"]
    country = user_config["country"]
    city = user_config["city"]
    age = user_config['age']

    if name == 'Sir':
        response = f"You haven't provided much details to me, start setup to setup initial user configuration"
    else:
        response = f"Your name is {name}, you are {age} years old. You live in {country},{city}."
    return response
