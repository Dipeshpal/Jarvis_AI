import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import sys

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


class JarvisAssistant:
    def __init__(self):
        pass

    def mic_input(self):
        """
        Fetch input from mic
        :return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Say something...')
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio).lower()
                print('You said: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return False

    def text2speech(self, text):
        """
        Convert any text to speech
        :param text: text (String)
        :return: True / False (Play sound if True otherwise write exception to log and return False)
        """
        try:
            myobj = gTTS(text=text, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            return True
        except Exception as e:
            mytext = "Sorry I couldn't understand, or not implemented to handle this input"
            print(mytext)
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("tmp.mp3")
            playsound("tmp.mp3")
            os.remove("tmp.mp3")
            print(e)
            return False

    def shutdown(self):
        """
        Shutdown the Jarvis API, exit from program
        :return: if no error then exit from program, False if Fail
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
        :param domain: any domain, example "youtube.com"
        :return: True if success, False if fail
        """
        return website_open.website_opener(domain)

    def send_mail(self, sender_email=None, sender_password=None, receiver_email=None, msg="Hello"):
        """
        This function will send mail to user according to input params
        Currently on =ly support Gmail
        :param sender_email: Email id of sender
        :param sender_password: Password
        :param receiver_email: Email id of receiver
        :param msg: Message or mail you want to send
        :return: True if success, False if fail
        """
        return send_mail(sender_email, sender_password, receiver_email, msg)

    def tell_me_date(self):
        """
        Just return date as string
        :return: date if success, False if fail
        """
        return date_time.date()

    def tell_me_time(self):
        """
        This function will return time
        :return: Time if success, False if fail
        """
        return date_time.time()

    def launch_any_app(self, path_of_app='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):
        """
        Launch any windows application according to application path
        :param path_of_app: path of exe
        :return: True if success and open the application, False if fail
        """
        return launch_app.launch_app(path_of_app)

    def weather(self, city='Indore'):
        """
        Return weather
        :param city: Any city of this world
        :return: weather info as string if True, or False
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
        :return: news list of string if True, False if fail
        """
        return nw.news()

    def tell_me(self, topic='tell me about Taj Mahal'):
        """
        Tells about anything from wikipedia
        :param topic: any string is valid options
        :return: First 500 character from wikipedia if True, False if fail
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
        obj = dc.DatasetCreate(dataset_path=dataset_path, class_name=class_name,
                               haarcascade_path=haarcascade_path,
                               eyecascade_path=eyecascade_path, eye_detect=eye_detect,
                               save_face_only=save_face_only, no_of_samples=no_of_samples,
                               width=width, height=height, color_mode=color_mode)
        obj.create()

    def face_recognition_train(self, data_dir='datasets', batch_size=32, img_height=128, img_width=128, epochs=10,
                               model_path='model'):
        """
        Train TF Keras model according to dataset path
        :param data_dir: str (example: 'folder_of_dataset')
        :param batch_size: int (example:32)
        :param img_height: int (example:128)
        :param img_width: int (example:128)
        :param epochs: int (example:10)
        :param model_path: str (example: 'model')
        :return: None
        """
        obj = train.Classifier(data_dir=data_dir, batch_size=batch_size, img_height=img_height,
                               img_width=img_width, epochs=epochs, model_path=model_path)
        obj.start()

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
        obj = predict.Predict(class_name=class_name, img_height=img_height, img_width=img_width,
                              haarcascade_path=haarcascade_path,
                              eyecascade_path=eyecascade_path, model_path=model_path,
                              color_mode=color_mode)
        obj.cap_and_predict()


if __name__ == '__main__':
    obj = JarvisAssistant()
    # res = obj.mic_input()
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
    # print(res)
    # obj.text2speech(res[0])
    # obj.text2speech(res[1])
    obj.datasetcreate()
