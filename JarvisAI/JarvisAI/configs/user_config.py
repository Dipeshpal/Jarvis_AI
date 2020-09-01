import json


user_config = {
    "name": "Sir",
    "age": 22,
    "city": "Indore"
}

with open("configs/user_config.json", "w") as outfile:
    json.dump(user_config, outfile)
