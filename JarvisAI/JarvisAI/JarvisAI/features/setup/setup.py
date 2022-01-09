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

        with open('configs/config.ini', 'w') as configfile:
            config.write(configfile)

        print("Setup Done")
        return True

    def setup_assistant(self):
        if not os.path.exists('configs'):
            os.makedirs('configs')
        config = configparser.ConfigParser()

        if not os.path.exists('configs/config.ini'):
            sure = str(input("No Config Found. Create New (y/n): ") or "n")
            if sure == "n":
                print("No changes done")
                return False
            else:
                return self.start_sconfig(config)
        else:
            return self.start_sconfig(config)
