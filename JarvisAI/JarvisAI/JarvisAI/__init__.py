import speech_recognition as sr
import os
from gtts import gTTS
import pyttsx3
from playsound import playsound
import sys
import configparser
import random
from lazyme.string import color_print as cprint

try:
    import pyaudio
except Exception as e:
    try:
        os.system("pipwin install pyaudio")
    except Exception as e:
        try:
            os.system("pip install pyaudio")
        except Exception as e:
            print("Exception occur ", e)
            print("Install pyaudio manually")
        import pyaudio

# import custom features
try:
    import features.weather.weather as wea
    import features.website_open.website_open
    import features.send_mail.send_mail
    import features.date_time.date_time
    import features.launch_app.launch_app
    import features.news.news as nw
    import features.tell_me_about.tell_me_about as tma
    import features.face_recognition.dataset_create as dc
    import features.face_recognition.train as train
    import features.face_recognition.predict as predict
    import features.face_recognition.face_reco as fr
    import features.show_me_my_images.show_me_my_images as my_photos
    import features.setup.setup as setup_assistant
    import features.google_photos.google_photos as gp
    import features.joke.joke
    import features.hot_word_detection.hot_word_detection as wake_word
    import features.mic_input_ai.mic_input_ai.SpeechRecognition as SpeechRecognitionAI
    import features.jarvisai_api.jarvisai_api.JarvisAIAPI
    import features.detection.detection.Detections
    import features.chatbot.chatbot.start_chatbot_large as chatbot_lrg
    import features.chatbot.chatbot.start_chatbot_small as chatbot_sml
    import features.chatbot.chatbot.load_chatbot_models as load_ch_model
    import features.chatbot.todo.make_todo
    import features.chatbot.todo.read_notes_if_exist
    import features.chatbot.todo.delete_todo
    import features.chatbot.jarvis_ai_neural_engine.neural_engine

    # import features.utilities.utilities

except Exception as e:
    from JarvisAI.features.weather import weather as wea
    from JarvisAI.features.website_open import website_open
    from JarvisAI.features.send_mail import send_mail
    from JarvisAI.features.date_time import date_time
    from JarvisAI.features.launch_app import launch_app
    from JarvisAI.features.news import news as nw
    from JarvisAI.features.tell_me_about import tell_me_about as tma
    from JarvisAI.features.face_recognition import dataset_create as dc
    from JarvisAI.features.face_recognition import train as train
    from JarvisAI.features.face_recognition import predict as predict
    from JarvisAI.features.face_recognition import face_reco as fr
    from JarvisAI.features.show_me_my_images import show_me_my_images as my_photos
    from JarvisAI.features.setup import setup as setup_assistant
    from JarvisAI.features.google_photos import google_photos as gp
    from JarvisAI.features.joke import joke
    from JarvisAI.features.hot_word_detection import hot_word_detection as wake_word
    from JarvisAI.features.mic_input_ai.mic_input_ai import SpeechRecognition as SpeechRecognitionAI
    from JarvisAI.features.jarvisai_api.jarvisai_api import JarvisAIAPI
    from JarvisAI.features.detection.detection import Detections
    from JarvisAI.features.chatbot.chatbot import start_chatbot_large as chatbot_lrg
    from JarvisAI.features.chatbot.chatbot import start_chatbot_small as chatbot_sml
    from JarvisAI.features.chatbot.chatbot import load_chatbot_models as load_ch_model
    from JarvisAI.features.chatbot.todo import make_todo, read_notes_if_exist, delete_todo
    from JarvisAI.features.chatbot.jarvis_ai_neural_engine import neural_engine
    # from JarvisAI.features.utilities import utilities


class JarvisAssistant:
    def __init__(self, sync=True, token=None, disable_msg=False, load_chatbot_model=True,
                 high_accuracy_chatbot_model=False,
                 high_accuracy_chatbot_model_with_neural_engine=False,
                 chatbot_large=False, backend_tts_api='pyttsx3'):

        # Check TTS Backend
        backends = ['pyttsx3', 'gtts']
        if backend_tts_api not in backends:
            raise ValueError("Invalid backend_tts_api type. Expected one of: %s" % backends)
        self.backend_tts_api = backend_tts_api

        # Check Chatbot Model
        if load_chatbot_model:
            self.chatbot_model = load_ch_model(high_accuracy_chatbot_model, chatbot_large)
        self.load_chatbot_model = load_chatbot_model

        # high_accuracy_chatbot_model_with_neural_engine
        self.high_accuracy_chatbot_model_with_neural_engine = high_accuracy_chatbot_model_with_neural_engine
        if high_accuracy_chatbot_model_with_neural_engine:
            self.jarvisai_neural_engine_obj = neural_engine.JarvisAINeuralEngine()
        else:
            self.jarvisai_neural_engine_obj = None

        # Check Sync Token
        if token is None or not sync:
            if not disable_msg:
                print("\n")
                cprint(
                    "Note: This library is no longer in development. "
                    "Check Out Lightweight (More Powerful) Version of JarvisAI- \n"
                    "AdonisAI: https://pypi.org/project/AdonisAI \n\n", color='red')
                cprint("Set 'obj = JarvisAI.JarvisAssistant(sync=False)' if you do not want to use API",
                       color='green')
                cprint("Obtain your token from: http://jarvis-ai-api.herokuapp.com/", color='green')
                cprint("Its free to use. Even API services is also free. \n"
                       "Well, JarvisAI need support of your to keep this project and it's API alive.\n"
                       "So, your contribution/donation will be appreciated. \n"
                       , color='blue')
                cprint("DONATE: https://www.buymeacoffee.com/dipeshpal", color='red')
                cprint(
                    "Set 'obj = JarvisAI.JarvisAssistant(disable_msg=True)' if you do not want to display this message",
                    color='green')
                cprint("Initializing JarvisAI...", color='yellow')

        self.sync = sync
        self.token = token
        self.speech_recognition_ai = SpeechRecognitionAI()
        self.jarvisai_api = JarvisAIAPI()
        self.obj_detection = Detections()

    def setup(self):
        """
        Method to define configuration related to assistant
        :return: Bool
            True if setup done
            False if setup cancel or interrupt
        """
        obj_setup = setup_assistant.Setup()
        response = obj_setup.setup_assistant()
        del obj_setup
        return response

    def hot_word_detect(self, lang='en'):
        """
        Hot word (wake word / background listen) detection
        :param lang: str
            default 'en'
        :return: Bool, str
            status, command
        """
        return wake_word.hot_word_detection(lang=lang)

    def mic_input(self, lang='en'):
        """
        Fetch input from mic
        Note: mic_input usages Google's Speech Recognition
        Limitation: After multiple hits API may not work so use mic_input_ai() instead of mic_input
        :param lang: str
            default 'en'
        :return: str/Bool
            user's voice input as text if true/ false if fail
        """
        if not self.sync:
            config = configparser.ConfigParser()
            config.read('configs/config.ini')
            user_name = config['default']['user_name']
        else:
            if self.token is None:
                cprint("TOKEN NOT FOUND",
                       color='yellow')
                cprint("Set 'obj = JarvisAI.JarvisAssistant(sync=true, token='xyz')' if you want to use this API",
                       color='red')
                cprint("Obtain your token from: http://jarvis-ai-api.herokuapp.com/", color='green')
                print("Currently using local config from 'configs/config.ini' . . .")
                config = configparser.ConfigParser()
                config.read('configs/config.ini')
                user_name = config['default']['user_name']
            else:
                status, res = self.jarvisai_api.get_user_data(self.token)
                if not res['status']:
                    if res['message'] == 'Invalid Token':
                        cprint('Invalid Token',
                               color='red')
                        cprint("Obtain your token from: http://jarvis-ai-api.herokuapp.com/", color='green')
                        raise Exception(f'Invalid Token: {self.token}')
                    else:
                        cprint(res['message'],
                               color='red')
                        raise Exception(res['message'])
                else:
                    user_name = res['data']['name_']

        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                greeting = random.choice(["Hello", "Hi"])
                msg = greeting + ' ' + user_name + ',' + ' How may I help you?'
                print(msg)
                self.text2speech(msg)
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language=lang).lower()
                print('You said: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return False

    def mic_input_ai(self, record_seconds=5, debug=False):
        """
        Fetch input from mic and recognition using Transformers
        Note: This will download pretrained ML model for the first time only
        :param record_seconds: int
            Default 5
        :param debug: bool
            Print recording status if True
        :return: str
            User's voice input as text
        """
        transcription = self.speech_recognition_ai.start_speech_recognition(record_seconds=record_seconds, debug=debug)
        return transcription

    def text2speech(self, text, lang='en'):
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
        if self.backend_tts_api == 'gtts':
            # for gtts Backend
            try:
                myobj = gTTS(text=text, lang=lang, slow=False)
                myobj.save("tmp.mp3")
                playsound("tmp.mp3")
                os.remove("tmp.mp3")
                return True
            except Exception as e:
                # mytext = "Sorry I couldn't understand, or not implemented to handle this input"
                # print(mytext)
                # myobj = gTTS(text=mytext, lang=lang, slow=False)
                # myobj.save("tmp.mp3")
                # playsound("tmp.mp3")
                # os.remove("tmp.mp3")
                print(e)
                print("or You may reached free limit of 'gtts' API. Use 'pyttsx3' as backend for unlimited use.")
                return False
        else:
            # for pyttsx3 Backend
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            try:
                voice_file_name = "configs/JarvisAI-Voice.txt"
                if not os.path.exists(voice_file_name):
                    cprint("You can try different voices. This is one time setup. You can reset your voice by deleting"
                           "'configs/JarvisAI-Voice.txt' file in your working directory.",
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

    def shutdown(self):
        """
        Shutdown the Jarvis API, exit from program
        :return: None/bool
            if no error then exit from program, False if Fail
        """
        try:
            self.text2speech('Good bye. Have a nice day')
            sys.exit()
        except Exception as e:
            print(e)
            return False

    def website_opener(self, domain):
        """
        This will open website according to domain
        :param domain: str
            any domain, example "youtube.com"
        :return: Bool
            True if success, False if fail
        """
        return website_open.website_opener(domain)

    def send_mail(self, sender_email=None, sender_password=None, receiver_email=None, msg="Hello"):
        """
        This function will send mail to user according to input params
        Currently on =ly support Gmail
        :param sender_email: str
            Email id of sender
        :param sender_password: str
            Password
        :param receiver_email: str
            Email id of receiver
        :param msg: str
            Message or mail you want to send
        :return: Bool
            True if success, False if fail
        """
        return send_mail.send_mail(sender_email, sender_password, receiver_email, msg)

    def tell_me_date(self):
        """
        Just return date as string
        :return: str/Bool
            date if success, False if fail
        """
        return date_time.date()

    def tell_me_time(self):
        """
        This function will return time
        :return: str/Bool
            Time if success, False if fail
        """
        return date_time.time()

    def launch_any_app(self, path_of_app='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):
        """
        Launch any windows application according to application path
        :param path_of_app: str
            path of exe
        :return: Bool
            True if success and open the application, False if fail
        """
        return launch_app.launch_app(path_of_app)

    def weather(self, city='Indore'):
        """
        Return weather
        :param city: str
            Any city of this world
        :return: str/bool
            weather info as string if True, or False
        """
        try:
            res = wea.weather_app(city)
        except Exception as e:
            print(e)
            res = False
        return res

    def get_weather(self, text):
        """
        Return weather by auto-detecting city just pass text.
        Example: "Tell me weather in Indore" or "Tell me weather"
        :param text: str
            Any city of this world
        :return: str/bool
            weather info as string if True, or False
        """
        try:
            res = wea.weather_app(text)
        except Exception as e:
            print(e)
            res = False
        return res

    def news(self):
        """
        Fetch top news of the day from news.google.com/news/rss
        :return: list/bool
            news list of string if True, False if fail
        """
        return nw.news()

    def tell_me(self, topic='tell me about Taj Mahal'):
        """
        Tells about anything from wikipedia
        :param topic: str
            any string is valid options
        :return: list/bool
            First 500 character from wikipedia if True, False if fail
        """
        return tma.tell_me_about(topic)

    def datasetcreate(self, dataset_path='datasets', class_name='Demo',
                      haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',
                      eyecascade_path='haarcascade/haarcascade_eye.xml', eye_detect=False,
                      save_face_only=True, no_of_samples=100,
                      width=128, height=128, color_mode=False):
        """
        Dataset Create by face detection
        :param dataset_path: str (example: 'folder_of_dataset')
        :param class_name: str (example: 'folder_of_dataset')
        :param haarcascade_path: str (example: 'haarcascade_frontalface_default.xml)
        :param eyecascade_path: str (example: 'haarcascade_eye.xml)
        :param eye_detect: bool (example:True)
        :param save_face_only: bool (example:True)
        :param no_of_samples: int (example: 100)
        :param width: int (example: 128)
        :param height: int (example: 128)
        :param color_mode: bool (example:False)
        :return: None
        """

        obj = fr.DatasetCreate(dataset_path=dataset_path, class_name=class_name,
                               haarcascade_path=haarcascade_path,
                               eyecascade_path=eyecascade_path, eye_detect=eye_detect,
                               save_face_only=save_face_only, no_of_samples=no_of_samples,
                               width=width, height=height, color_mode=color_mode)
        obj.datasetcreate()

    def face_recognition_train(self, data_dir='datasets', batch_size=32, img_height=128, img_width=128, epochs=10,
                               model_path='model', pretrained=None, base_model_trainable=False):
        """
        Train TF Keras model according to dataset path
        :param data_dir: str (example: 'folder_of_dataset')
        :param batch_size: int (example:32)
        :param img_height: int (example:128)
        :param img_width: int (example:128)
        :param epochs: int (example:10)
        :param model_path: str (example: 'model')
        :param pretrained: str (example: None, 'VGG16', 'ResNet50', 'InceptionV3')
        :param base_model_trainable: bool (example: False (Enable if you want to train the pretrained model's layer))
        :return: None
        """
        obj = fr.FaceRecognizerTrain(data_dir=data_dir, batch_size=batch_size, img_height=img_height,
                                     img_width=img_width, epochs=epochs, model_path=model_path, pretrained=pretrained,
                                     base_model_trainable=base_model_trainable)
        obj.train()

    def predict_faces(self, class_name=None, img_height=128, img_width=128,
                      haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',
                      eyecascade_path='haarcascade/haarcascade_eye.xml', model_path='model',
                      color_mode=False):
        """
        Predict Face
        :param class_name: Type-List (example: ['class1', 'class2'] )
        :param img_height: int (example:128)
        :param img_width: int (example:128)
        :param haarcascade_path: str (example: 'haarcascade_frontalface_default.xml)
        :param eyecascade_path: str (example: 'haarcascade_eye.xml)
        :param model_path: str (example: 'model')
        :param color_mode: bool (example: False)
        :return: None
        """
        obj = fr.Predict(class_name=class_name, img_height=img_height, img_width=img_width,
                         haarcascade_path=haarcascade_path,
                         eyecascade_path=eyecascade_path, model_path=model_path,
                         color_mode=color_mode)
        obj.predictfaces()

    def show_me_my_images(self):
        """
        This function will show images from local directory. Make sure to run setup() first to setup local directory.
        :return: Bool
        """
        return my_photos.show_me_my_images()

    def show_google_photos(self):
        """
        This function will open "https://photos.google.com/" in your browser.
        :return: Bool
        """
        return gp.google_photos()

    def tell_me_joke(self, language='en', category='neutral'):
        """
        Function to tell a joke
        Read https://pyjok.es/api/ for more details
        :param language: str
            default "en"
        :param category: str
            default "neutral"
        :return: str
            "Joke:
        """
        return joke.tell_me_joke(lang=language, cat=category)

    def get_user_data(self):
        """
        Function to fetch user data
        More info: https://jarvis-ai-api.herokuapp.com/api_docs/
        :return: status, response
        """
        if self.token is None:
            cprint("TOKEN NOT FOUND",
                   color='yellow')
            cprint("Set 'obj = JarvisAI.JarvisAssistant(sync=true, token='xyz')' if you want to use this API",
                   color='red')
            cprint("Obtain your token from: http://jarvis-ai-api.herokuapp.com/", color='green')

        status, res = self.jarvisai_api.get_user_data(self.token)
        return status, res

    def set_user_data(self):
        """
        Function to set user data
        :return: None
        """
        self.jarvisai_api.set_user_data()

    def jarvisai_configure_hand_detector(self, camera=0, detectionCon=0.7, maxHands=2, cam_display=True, cam_height=480,
                                         cam_width=888):
        """
        This function is for hand detection configuration.
        Before using 'jarvisai_detect_hands' you need to call this function to setup things.
        @param camera: int (example:0)
            Your device camera number
        @param detectionCon: int (example:0.5)
            The accuracy of hand detection
        @param maxHands: int (example:2)
            Maximum number of hands you want to detect in single frame
        @param cam_display: Bool (example:True)
            Set 'False' if you do not want to display camera window
        @param cam_height: int (Example: 480)
            Resolution of camera window height
        @param cam_width: int (Example: 888)
            Resolution of camera window width
        """
        self.obj_detection.configure_hand_detector(camera, detectionCon, maxHands, cam_display, cam_height, cam_width)

    def jarvisai_detect_hands(self, message=""):
        """
        This function detect the hands and return number of fingers with hand type.
        @param message: str (example: Hello!)
        @return:
            fingers: list (Number of fingers up),
            hand_type: string ('Left' or 'Right' Hand),
            cv2: cv2 object for advance usages,
            img: image array from your camera for advance usages,
            cap: The cap is from VideoCapture object ('cap = cv2.VideoCapture(camera) ) for advance usages.'
            For ADVANCE USAGES REFER: https://docs.opencv.org/master/index.html
        """
        fingers, hand_type, cv2, img, cap = self.obj_detection.detect_hands(message)
        return fingers, hand_type, cv2, img, cap

    # def load_chatbot_model(self, high_accuracy=False, chatbot_large=False):
    #     """
    #     @param high_accuracy: bool (example: False)
    #     @param chatbot_large: bool (example: False)
    #     if you are using chatbot_large then set 'chatbot_large=True', It will required more memory
    #     @return:
    #         fingers: list (Number of fingers up),
    #     """
    #     chatbot_model = load_ch_model(high_accuracy, chatbot_large)
    #     return chatbot_model

    def chatbot_base(self, input_text):
        """
        Conversational Chatbot without using wikipedia/google search
        Note:
            1. Use 'chatbot_base' if you have low memory (low accuracy) otherwise use 'chatbot_large' (high accuracy)
            2. Set 'JarvisAI.JarvisAssistant(high_accuracy_chatbot_model=False)' for low memory system (It gives low accuracy)
        @param input_text: str (example: Hello!)
        @return: str
        """
        if not self.load_chatbot_model:
            print("You need to Set 'JarvisAI.JarvisAssistant(load_chatbot_model=True)' first")
            print("Exiting now, try again...")
        return chatbot_sml(input_text, self.chatbot_model)

    def chatbot_large(self, input_text):
        """
        If chatbot can't answer then it will do wikipedia/google search
        Note:
           1. Use 'chatbot_large' if you have high memory
           2. Set 'JarvisAI.JarvisAssistant(high_accuracy_chatbot_model=True)' for high memory system (It gives high accuracy)
        @param input_text: str (example: Hello!)
        @return: str
        """
        if not self.load_chatbot_model:
            print("You need to Set 'JarvisAI.JarvisAssistant(load_chatbot_model=True)' first")
            print("Exiting now, try again...")
        return chatbot_lrg(input_text, self.chatbot_model)

    def chatbot_advance(self, input_text, enable_google=False, enable_youtube=False):
        """
        If chatbot can't answer then it will do wikipedia/google search
        Note:
            1. Set 'JarvisAI.JarvisAssistant(load_chatbot_model=False)'
            2. Set 'JarvisAI.JarvisAssistant(high_accuracy_chatbot_model=False)'
            3. Set 'JarvisAI.JarvisAssistant(chatbot_large=False)'
            4. Set 'JarvisAI.JarvisAssistant(high_accuracy_chatbot_model_with_neural_engine=True)'
            It is recommended to use 'high_accuracy_chatbot_model_with_neural_engine' or 'chatbot_large'
        @param input_text: str (example: Hello!)
        @param enable_google: bool (example: True)
        @param enable_youtube: bool (example: True)
        @return response: dict
        @return status: bool
        """
        if not self.high_accuracy_chatbot_model_with_neural_engine:
            print(
                "You need to Set 'JarvisAI.JarvisAssistant(high_accuracy_chatbot_model_with_neural_engine=True)'"
                " first to use 'chatbot_advance'")
            return None, False
        else:
            response = self.jarvisai_neural_engine_obj.predict_outcome(text=input_text, enable_google=enable_google,
                                                                       enable_youtube=enable_youtube)
        return response, True

    def show_me_my_list(self):
        """
        Shows your current list data in dictionary if exist
        parameter:
        return:
            data: dictionary containing user list data
        """
        data = read_notes_if_exist()
        return data

    def create_new_list(self, input_text: str = 'add milk in my shopping list'):
        """
        It create new list by identifying list name and list data from user input
        parameter:
            input_text: str (Example: 'add milk in my shopping list')
        return:
            status: boolean (True for success)
        """
        status = make_todo(input_text, question_answering_model=self.chatbot_model[
            'intent_model'].question_answering)
        return status

    def delete_particular_list(self, input_text: str = 'delete my shopping list'):
        """
        It delete particular list by identifying list name from user input
        parameter:
            input_text: str (Example: 'delete my shopping list')
        return:
            status: boolean (True for success)
            msg: str (General Message)
        """
        status, msg = delete_todo(input_text, question_answering_model=self.chatbot_model[
            'intent_model'].question_answering)
        return status, msg

    def show_me_some_tech_news(self):
        nw.show_me_some_tech_news()

    def show_me_some_tech_videos(self):
        nw.show_me_some_tech_videos()


if __name__ == '__main__':
    obj = JarvisAssistant(sync=True, token='adc0a911a43f8b5edce4b44f4c65f7', disable_msg=False,
                          load_chatbot_model=True, high_accuracy_chatbot_model=False,
                          chatbot_large=True)
    print(obj.get_user_data())
    print(obj.show_me_my_list())
    print(obj.create_new_list())
    print(obj.create_new_list('add medicine in my market list'))
    print(obj.show_me_my_list())
    print(obj.delete_particular_list())
    print(obj.show_me_my_list())
    # obj.jarvisai_detect_hands()
    # print(obj.mic_input_ai())
    # print(obj.text2speech_male())
    # res = obj.tell_me_joke()
    # print(res)
    # obj.text2speech("hello")
    # res = obj.website_opener("facebook.com")
    # res = obj.send_mail()
    # res = obj.launch_app("edge")
    # res = obj.weather("mumbai")
    # res = obj.news()
    # res = obj.tell_me()
    # res = obj.tell_me_time()
    # res = obj.tell_me_date()
    # res = obj.shutdown()
    # obj.datasetcreate()
