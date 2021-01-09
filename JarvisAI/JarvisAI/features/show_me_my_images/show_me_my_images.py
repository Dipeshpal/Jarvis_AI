import subprocess
import getpass
import json


def show_me_my_images():
    """
    This method will open image directory
    :return: Bool
    """
    try:
        try:
            with open("config/config.json", "r") as f:
                config = json.load(f)
                path_user_defined = config['photos']
        except Exception as e:
            path_user_defined = []
            print("Opening Default Directory, Setup 'config/config.json' first to open custom directory.")

        if len(path_user_defined) == 0:
            path = r"C:\Users\{0}\Pictures".format((getpass.getuser()))
            subprocess.Popen(f'explorer "{path}"')
            return True
        else:
            try:
                for i in path_user_defined:
                    subprocess.Popen(f'explorer "{i}"')
                return True
            except Exception as e:
                print(f"Unable to locate {path_user_defined} directory, Exception- {e}")
                return False
    except Exception as e:
        print(f"Unable to locate default directory: {e}")
        return False
