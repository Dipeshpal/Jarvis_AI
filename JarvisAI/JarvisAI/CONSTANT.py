BASE_URL = "https://jarvisai.in/"
USER_CONFIG_FOLDER = './user_configs/'
API_KEY_PATH = f'{USER_CONFIG_FOLDER}api_key.txt'
SPEECH_ENGINE_PATH = f'{USER_CONFIG_FOLDER}speech_engine.txt'
API_AUTH_URL = f"{BASE_URL}check_secret_key?secret_key="


class Constant:
    def __init__(self):
        self.BASE_URL = BASE_URL
        self.USER_CONFIG_FOLDER = USER_CONFIG_FOLDER
        self.API_KEY_PATH = API_KEY_PATH
        self.SPEECH_ENGINE_PATH = SPEECH_ENGINE_PATH
        self.API_AUTH_URL = API_AUTH_URL

