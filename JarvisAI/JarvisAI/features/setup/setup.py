import os
import configparser


class Setup:
    def start_sconfig(self, config):
        default = 'default'
        config.add_section('default')

        bot_name = str(input("Enter Bot name (default=jarvis): ") or "jarvis")
        user_name = str(input("Enter User name (default=dipesh): ") or "Dipesh")
        photos_dir = str(input("Enter Photos Directories separated by comma ',' (default=None): ") or "None")

        config[default]['bot_name'] = bot_name
        config[default]['user_name'] = user_name
        config[default]['photos'] = photos_dir

        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)

        print("Setup Done")
        return True

    def setup_assistant(self):
        if not os.path.exists('config'):
            os.makedirs('config')
        config = configparser.ConfigParser()

        if os.path.exists('config'):
            sure = str(input("Your current configuration will be deleted, are you sure (y/n): ") or "n")
            if sure == "n":
                print("No changes done")
                return False
            else:
                return self.start_sconfig(config)
        else:
            return self.start_sconfig(config)
