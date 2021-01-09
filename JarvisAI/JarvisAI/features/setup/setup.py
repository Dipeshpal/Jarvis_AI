import json
import os


def choose_option(configs):
    print("Choose what to setup-")
    index_list = []
    index_list.append(0)
    print("0 : Break Operation")
    try:
        for index, (key, value) in enumerate(configs.items()):
            index_list.append(index + 1)
            print(index + 1, ":", key)
    except:
        print("Some Errors in 'config/config.json', Unable to read file.")

    try:
        choice = int(input("Enter Choice: "))
    except Exception as e:
        print("Only Numeric value is allowed, TRY AGAIN")
        return 0
    if choice == 0:
        return choice
    if choice not in index_list:
        print("Invalid Choice, Try again")
        return 0
    return choice


def setup_photos_dir(configs):
    print("==========Photos Directory Setup==========")
    photos_dir_list = configs['photos']
    if len(photos_dir_list) == 0:
        print("No Existing Directory")
    else:
        print("Existing Directories of your photos are- ")
        for i, j in enumerate(photos_dir_list):
            print(i + 1, ": ", j)
    try:
        print("==========Choose Option==========")
        ch = int(input(
            "0: Break \n1: Add More Directories \n2: Remove Existing Directories and Add New Directories \n\nEnter Choice: "))
    except Exception as e:
        print("Only Numerical values allowed\n")
        ch = 0
        return 0
    if ch == 0:
        return False
    if ch not in [1, 2]:
        print("Invalid Choice, TRY AGAIN")
        return False
    else:
        if ch == 1:
            print("==========Choose Option==========")
            photos_dir = input(
                "Enter your photos directory, you can enter multiple directory by comma (,) separate. Example: D:\photos,D:photos2- \nEnter: ")
            configs["photos"] = photos_dir_list + photos_dir.split(',')
            print("Directories Updated- \n ", configs['photos'])
        if ch == 2:
            photos_dir = input(
                "Enter your photos directory, you can enter multiple directory by comma (,) separate. Example: D:\photos,D:photos2- \nEnter: ")
            configs["photos"] = photos_dir.split(',')
            print("Directories Added- \n ", configs['photos'])
    return configs


def setup():
    if not os.path.exists('config'):
        os.makedirs('config')
        configs = {
            "photos": []
        }
        with open("config/config.json", "w") as f:
            json.dump(configs, f)

    try:
        with open("config/config.json", "r") as f:
            configs = json.load(f)
    except:
        print("Some Errors in 'config/config.json', Unable to read file.")
        print("==========Choose Option==========")
        try:
            ch_ = int(input(
                "1. I'll check 'config/config.json' file manually \n2. Reset 'config/config.json' file (Delete all existing Settings) \nEnter: "))
            print("\n")
        except:
            print("Only Numerical values allowed\n")
            return False
        if ch_ not in [1, 2]:
            print("Invalid Choice")
            return False
        if ch_ == 1:
            print("Stopping... 'config/config.json' file manually")
            return False
        if ch_ == 2:
            print("Resetting 'config/config.json' file")
            configs = {
                "photos": []
            }
            with open("config/config.json", "w") as f:
                json.dump(configs, f)
            print("====================")
    try:
        try:
            with open("config/config.json", "r") as f:
                configs = json.load(f)
        except Exception as e:
            configs = dict()
            print(e)

        choice = choose_option(configs)
        if choice == 0:
            return False

        if choice == 1:
            configs = setup_photos_dir(configs)

        with open("config/config.json", "w") as f:
            json.dump(configs, f)
        return True
    except Exception as e:
        print("Exception Occur- ", e)
        return False
