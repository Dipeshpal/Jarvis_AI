import speech_recognition as sr
import configparser
import re


def hot_word_detection(lang='en'):
    """
    Hot word (wake word / background listen) detection
    :param lang: str
        default 'en'
    :return: Bool, str
        status, command
    """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    bot_name = config['default']['bot_name']
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            command = r.recognize_google(audio, language=lang).lower()
            if re.search(bot_name, command):
                return True, command
    except Exception as e:
        print(e)
        return False, None


if __name__ == '__main__':
    hot_word_detection()
