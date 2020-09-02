from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os


class Jarvis:
    def __init__(self, features_config, user_name="Sir",
                 country='India', city='Pune', age=0, email=None):
        self.features_config = features_config
        self.user_config = {
            'user_name': user_name,
            'country': country,
            'city': city,
            'age': age,
            'email': email,
        }

    def txt2speech(self, mytext):
        try:
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
        except Exception:
            mytext = "Sorry I couldn't understand, or not implemented to handle this input"
            print(mytext)
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")

    def mic_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            self.txt2speech("Say Something!")
            audio = r.listen(source)
        try:
            print("You: ", r.recognize_google(audio))
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            self.txt2speech("Sorry I couldn't understand, please try again")
            # print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            self.txt2speech("Sorry I couldn't understand, please try again")
            # print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def txt_input(self):
        inp = input("Enter Anything: " or "Nothing")
        if inp == "Nothing":
            self.txt2speech("Sorry I couldn't understand, please try again")
        else:
            return inp

    def get_user_input(self, inp_src):
        if inp_src == "mic":
            inp = self.mic_input()
        if inp_src == "txt":
            inp = self.txt_input()
        inp = inp.lower()
        return inp

    def check_input(self, inp_txt):
        output = "Output from Jarvis"
        self.txt2speech(output)

    def update_user_config(self, user_name, country, city, age, email):
        self.user_config = {
            'user_name': user_name,
            'country': country,
            'city': city,
            'age': age,
            'email': email
        }


def start(features_config, action, models, MIC_MODE, DEV_MODE):
    if MIC_MODE:
        inp_src = 'mic'
    else:
        inp_src = 'txt'

    jarvis_obj = Jarvis(features_config)
    action_obj = action.Action()
    while True:
        try:
            inp = jarvis_obj.get_user_input(inp_src)
            data = {
                'user_input': inp,
                'features_config': jarvis_obj.features_config,
                'user_config': jarvis_obj.user_config,
                'DEV_MODE': DEV_MODE,
                'jarvis_obj': jarvis_obj
            }
            output = action_obj.take_action(data, models)
            print(output)
            jarvis_obj.txt2speech(output)
        except Exception as e:
            print("Exception occur, please report to solve your issue. \n Exception- \n ", e)
