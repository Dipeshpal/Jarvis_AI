import json


def setup_mode(inp=None):
    print("You are in Setup mode, let's setup few things")
    name = input("Enter your name: ")

    not_int = False
    while not not_int:
        try:
            age = int(input("Enter your age: "))
            not_int = True
        except Exception as e:
            print("Enter only numbers")

    city = input("Enter your city: ")

    dict_config = {
        "name": name,
        "age": age,
        "city": city
    }

    with open('configs/user_config.json', 'w') as json_file:
        json.dump(dict_config, json_file, indent=4)
    return "Setup Completed"
