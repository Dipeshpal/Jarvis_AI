import os
from gtts import gTTS
import pyttsx3
from playsound import playsound
from lazyme.string import color_print as cprint

USER_CONFIG_FOLDER = './user_configs/'
SPEECH_ENGINE_PATH = f'{USER_CONFIG_FOLDER}speech_engine.txt'


def text_to_speech(text, lang='en'):
    """
    Convert any text to speech
    You can use GTTS or PYTTSX3 as backend for Text to Speech.
    PYTTSX3 may support different voices (male/female) depends upon your system.
    You can set backend of tts while creating object of JarvisAI class. Default is PYTTSX3.
    :param text: str
        text (String)
    :param lang: str
        default 'en'
    :return: Bool
        True / False (Play sound if True otherwise write exception to log and return False)
    """
    with open(SPEECH_ENGINE_PATH, 'r') as f:
        backend_tts_api = f.read()
    if backend_tts_api == 'gtts':
        # for gtts Backend
        try:
            myobj = gTTS(text=text, lang=lang, slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            return True
        except Exception as e:
            print(e)
            print("or You may reached free limit of 'gtts' API. Use 'pyttsx3' as backend for unlimited use.")
            return False
    else:
        # for pyttsx3 Backend
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        try:
            if not os.path.exists("configs"):
                os.mkdir("configs")

            voice_file_name = "configs/Edith-Voice.txt"
            if not os.path.exists(voice_file_name):
                cprint("You can try different voices. This is one time setup. You can reset your voice by deleting"
                       "'configs/Edith-Voice.txt' file in your working directory.",
                       color='blue')
                cprint("Your System Support Following Voices- ",
                       color='blue')
                voices_dict = {}
                for index, voice in enumerate(voices):
                    print(f"{index}: ", voice.id)
                    voices_dict[str(index)] = voice.id
                option = input(f"Choose any- {list(voices_dict.keys())}: ")
                with open(voice_file_name, 'w') as f:
                    f.write(voices_dict.get(option, voices[0].id))
                with open(voice_file_name, 'r') as f:
                    voice_property = f.read()
            else:
                with open(voice_file_name, 'r') as f:
                    voice_property = f.read()
        except Exception as e:
            print(e)
            print("Error occurred while creating config file for voices in pyttsx3 in 'text2speech'.",
                  "Contact maintainer/developer of JarvisAI")
        try:
            engine.setProperty('voice', voice_property)
            engine.say(text)
            engine.runAndWait()
            return True
        except Exception as e:
            print(e)
            print("Error occurred while using pyttsx3 in 'text2speech'.",
                  "or Your system may not support pyttsx3 backend. Use 'gtts' as backend.",
                  "Contact maintainer/developer of JarvisAI.")
            return False
