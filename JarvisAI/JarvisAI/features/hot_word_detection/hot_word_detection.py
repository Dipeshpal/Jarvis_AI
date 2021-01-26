import speech_recognition as sr
import configparser
import re


class Error(Exception):
    """Base class for other exceptions"""
    pass


class DefaultFileNotFound(Error):
    """Raised when the Default File Not Found"""
    pass


def hot_word_detection(lang='en'):
    """
    Hot word (wake word / background listen) detection
    What is Hot word detection?
    ANSWER: Hot word listens for specific key words chosen to activate the “OK Google” voice interface. ...
    Voice interfaces use speech recognition technologies to allow user input through spoken commands.
    You can set your custom HOT WORD just by calling setup(). Your bot_name is your Hot word
    :param lang: str
        default 'en'
    :return: Bool, str
        status, command
    """
    try:
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        bot_name = config['default']['bot_name']
    except Exception as e:
        raise DefaultFileNotFound

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Background listening")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            command = r.recognize_google(audio, language=lang).lower()

            if re.search(bot_name, command):
                print("Waking up...")
                return True, command
            else:
                return False, False
    except Exception:
        return False, None


if __name__ == '__main__':
    hot_word_detection()
