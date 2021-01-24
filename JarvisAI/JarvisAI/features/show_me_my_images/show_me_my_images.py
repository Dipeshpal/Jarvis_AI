import subprocess
import configparser


def show_me_my_images():
    """
    This method will open image directory
    :return: Bool
    """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    try:
        path = config['default']['photos']
        path = path.split(",")
        for i in path:
            subprocess.Popen(f'explorer "{i}"')
        return True
    except Exception as e:
        print(f"Unable to locate default directory: {e}")
        return False
