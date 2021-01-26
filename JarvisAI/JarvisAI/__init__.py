import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import sys
import configparser
import random

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


class JarvisAssistant:
    def __init__(self):
        pass

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
        try:
            status, command = wake_word.hot_word_detection(lang=lang)
            print(status, command)
        except wake_word.DefaultFileNotFound as e:
            print("Unable to locate configuraton file 'config/config.ini'. Creating NOW...")
            self.setup()
        except Exception as e:
            status = command = False
        return status, command

    def mic_input(self, lang='en'):
        """
        Fetch input from mic
        :param lang: str
            default 'en'
        :return: str/Bool
            user's voice input as text if true/ false if fail
        """
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        user_name = config['default']['user_name']

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

    def text2speech(self, text, lang='en'):
        """
        Convert any text to speech
        :param text: str
            text (String)
        :param lang: str
            default 'en'
        :return: Bool
            True / False (Play sound if True otherwise write exception to log and return False)
        """
        try:
            myobj = gTTS(text=text, lang=lang, slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            return True
        except Exception as e:
            mytext = "Sorry I couldn't understand, or not implemented to handle this input"
            print(mytext)
            myobj = gTTS(text=mytext, lang=lang, slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            print(e)
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
        return send_mail(sender_email, sender_password, receiver_email, msg)

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

    def news(self):
        """
        Fetch top news of the day from news.google.com/news/rss
        :return: list/bool
            news list of string if True, False if fail
        """
        return nw.news()

    def tell_me(self, topic='India', sentences=1):
        """
        TIt tells about anything from wikipedia in summary
        :param topic: str
            any string is valid options
        :param sentences: int
            number of sentence
        :return: str
            Summary of topic
        """
        return tma.tell_me_about(topic, sentences)

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


if __name__ == '__main__':
    obj = JarvisAssistant()
    # print(obj.text2speech_male())
    res = obj.tell_me_joke()
    print(res)
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
