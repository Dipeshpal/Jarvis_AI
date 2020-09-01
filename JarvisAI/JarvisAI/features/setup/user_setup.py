import string


def setup_mode(data=None, model=None):
    print("You are in Setup mode, let's setup few things")
    user_name = input("Enter your name: ")
    country = input("Enter your country: ")
    country = string.capwords(country)
    not_int = False
    while not not_int:
        try:
            age = int(input("Enter your age: "))
            not_int = True
        except Exception as e:
            age = 0
            print("Enter only numbers")

    city = input("Enter your city: ")
    city = string.capwords(city)
    data['jarvis_obj'].update_user_config(user_name, country, city, age)
    print("New Configurations- \n", data['jarvis_obj'].user_config)
    return "Setup Completed"
