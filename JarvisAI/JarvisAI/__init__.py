import sys

try:
    from services.authenticate import verify_user
    from services.speech_to_text.speech_to_text import speech_to_text_google
    from services.text_to_speech.text_to_speech import text_to_speech
    from services.brain.decision_maker_api import make_decision_nlp, make_decision_ai, make_decision_jarvisai, \
        make_decision_jarvisai_string_matching
    from services.api_management_service.dist.manager import management as management_service
    from CONSTANT import Constant
    from features_default import dict_of_features, what_can_i_do
except:
    from JarvisAI.services.authenticate import verify_user
    from JarvisAI.services.speech_to_text.speech_to_text import speech_to_text_google
    from JarvisAI.services.text_to_speech.text_to_speech import text_to_speech
    from JarvisAI.services.brain.decision_maker_api import make_decision_nlp, make_decision_ai, make_decision_jarvisai, \
        make_decision_jarvisai_string_matching
    from JarvisAI.services.api_management_service.dist.manager import management as management_service
    from JarvisAI.CONSTANT import Constant
    from JarvisAI.features_default import dict_of_features, what_can_i_do

import os
import phonetics
from fuzzywuzzy import fuzz
from playsound import playsound
from download import download

CONSTANT = Constant()


class OutputMethods:
    def __init__(self, backend_tts_api):
        """
        Initialize OutputMethods class
        :param backend_tts_api: str
            backend_tts_api (String) <allowed values: ['pyttsx3', 'gtts']>
        """
        self.backend_tts_api = backend_tts_api

    @staticmethod
    def text_output(*args, **kwargs):
        """
        Print text to console
        """
        text = kwargs.get('text')
        print(text)

    @staticmethod
    def voice_output(*args, **kwargs):
        """
        Play text to speech
        """
        text = kwargs.get('text')
        text_to_speech(text=text, lang='en')


# create a class for inputs methods
class InputsMethods(OutputMethods):
    def __init__(self, backend_tts_api):
        """
        Initialize InputsMethods class
        :param backend_tts_api: str
            backend_tts_api (String) <allowed values: ['pyttsx3', 'gtts']>
        """
        super().__init__(backend_tts_api)

    @staticmethod
    def text_input(*args, **kwargs):
        """
        Get text from user
        """
        input_text = input("Say Something: ")
        return input_text

    @staticmethod
    def voice_input_google_api(*args, **kwargs):
        """
        Get voice input from Google Speech API
        read more about Google Speech API (Pricing and Key) at: https://cloud.google.com/speech-to-text
        """
        google_speech_recognition_input_lang = kwargs.get('google_speech_recognition_input_lang')
        google_speech_recognition_key = kwargs.get('google_speech_recognition_key')
        google_speech_recognition_duration_listening = kwargs.get('google_speech_recognition_duration_listening')
        command, status = speech_to_text_google(input_lang=google_speech_recognition_input_lang,
                                                key=google_speech_recognition_key,
                                                duration=google_speech_recognition_duration_listening)
        if status:
            return command
        else:
            return None

    @staticmethod
    def voice_input_deepspeech_streaming(*args, **kwargs):
        greeting = kwargs.get('greeting', None)
        deepspeech_listen_obj = kwargs.get('deepspeech_listen_obj', None)
        if greeting is not None:
            OutputMethods.voice_output(text=greeting)
        asr_deepspeech_stream = next(deepspeech_listen_obj)
        return asr_deepspeech_stream


class JarvisAI(InputsMethods, OutputMethods):
    def __init__(self, input_method: object, output_method: object, backend_tts_api='pyttsx3', api_key: str = "",
                 detect_wake_word: bool = True, wake_word_detection_method: object = None, bot_name: str = "Jarvis",
                 display_intent: bool = True, google_speech_recognition_input_lang='en',
                 google_speech_recognition_key=None, google_speech_recognition_duration_listening=5):
        """
        :param input_method: (object) method to get input from user <allowed values: [InputsMethods.text_input, InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming]>
        :param output_method: (object) method to give output to user <allowed values: [OutputMethods.text_output, OutputMethods.voice_output]
        :param backend_tts_api: (str) [Default 'pyttsx3'] backend tts api to use <allowed values: ['pyttsx3', 'gtts']>
        :param api_key: (str) [Default ''] api key to use JarvisAI get it from http://jarvis-ai-api.herokuapp.com
        :param detect_wake_word: (bool) [Default True] detect wake word or not <allowed values: [True, False]>
        :param wake_word_detection_method: (object) [Default None] method to detect wake word <allowed values: [InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming]
        :param bot_name: (str) [Default 'Jarvis'] name of the bot
        :param display_intent: (bool) [Default True] display intent or not <allowed values: [True, False]>
        :param google_speech_recognition_input_lang: (str) [Default 'en'] language of the input Check supported languages here: https://cloud.google.com/speech-to-text/docs/languages
        :param google_speech_recognition_key: (str) [Default None] api key to use Google Speech API
        :param google_speech_recognition_duration_listening: (int) [Default 5] duration of the listening

        READ MORE: Google Speech API (Pricing and Key) at: https://cloud.google.com/speech-to-text
        """
        self.deepspeech_listen_obj = None
        self.model = None
        self.vad_audio = None
        self.ARGS = None
        self.api_key = api_key
        self.input_method = input_method
        self.output_method = output_method
        self.backend_tts_api = backend_tts_api
        self.detect_wake_word = detect_wake_word
        self.wake_word_detection_method = wake_word_detection_method
        self.bot_name = bot_name
        self.display_intent = display_intent
        self.google_speech_recognition_input_lang = google_speech_recognition_input_lang
        self.google_speech_recognition_key = google_speech_recognition_key
        self.google_speech_recognition_duration_listening = google_speech_recognition_duration_listening
        self.custom_features = {}
        OutputMethods.__init__(self, backend_tts_api=backend_tts_api)

        self.validate_input_output_option()

    def register_feature(self, feature_obj: object, feature_command: str):
        """
        Register a feature to JarvisAI
        :param feature_obj: (object) function that will be called when the feature_command is detected
        :param feature_command: (str) command to activate the function
        """
        if feature_command in list(dict_of_features.keys()):
            raise ValueError(f"Feature command '{feature_command}' already registered. Change the command name.")
        dict_temp = {
            feature_command.lower(): feature_obj
        }
        self.custom_features.update(dict_temp)
        dict_of_features.update(self.custom_features)

    def play_wake_up_sound(self, lock=False):
        if lock:
            if not os.path.exists('ai-off.wav'):
                path = download('https://github.com/Dipeshpal/AdonisAI/raw/main/AdonisAI/utils/ai-off.wav',
                                'ai-off.wav', progressbar=True)
            playsound('ai-off.wav')
        else:
            if not os.path.exists('wake_up.wav'):
                path = download('https://github.com/Dipeshpal/AdonisAI/raw/main/AdonisAI/utils/wake_up.wav',
                                'wake_up.wav', progressbar=True)
            playsound('wake_up.wav')

    def validate_input_output_option(self):
        if self.backend_tts_api not in ['pyttsx3', 'gtts']:
            raise ValueError("Invalid backend_tts_api type. Expected one of: %s" % ['pyttsx3', 'gtts'])
        else:
            if not os.path.exists(CONSTANT.USER_CONFIG_FOLDER):
                os.mkdir(CONSTANT.USER_CONFIG_FOLDER)
            if not os.path.exists(CONSTANT.SPEECH_ENGINE_PATH):
                with open(CONSTANT.SPEECH_ENGINE_PATH, 'w') as f:
                    f.write(self.backend_tts_api)
            else:
                with open(CONSTANT.SPEECH_ENGINE_PATH, 'r') as f:
                    backend_tts_api_tmp = f.read()
                if backend_tts_api_tmp != self.backend_tts_api:
                    with open(CONSTANT.SPEECH_ENGINE_PATH, 'w') as f:
                        f.write(self.backend_tts_api)

        if self.input_method not in [InputsMethods.text_input, InputsMethods.voice_input_google_api,
                                     InputsMethods.voice_input_deepspeech_streaming]:
            raise ValueError("Invalid input_method type. Expected one of: %s" % [InputsMethods.text_input,
                                                                                 InputsMethods.voice_input_google_api,
                                                                                 InputsMethods.voice_input_deepspeech_streaming])
        elif self.input_method in [InputsMethods.voice_input_deepspeech_streaming]:
            try:
                from services.asr_deepspeech_streaming.streaming import listen as deepspeech_listen, ARGS, vad_audio, \
                    model
            except ImportError:
                from JarvisAI.JarvisAI.services.asr_deepspeech_streaming.streaming import listen as deepspeech_listen, \
                    ARGS, \
                    vad_audio, model

            self.ARGS = ARGS
            self.vad_audio = vad_audio
            self.model = model
            self.deepspeech_listen_obj = deepspeech_listen(ARGS, vad_audio, model)

        if self.output_method not in [OutputMethods.text_output, OutputMethods.voice_output]:
            raise ValueError("Invalid output_method type. Expected one of: %s" % [OutputMethods.text_output,
                                                                                  OutputMethods.voice_output])

        if self.api_key is None or self.api_key == "":
            raise ValueError(
                "Invalid api_key. Expected a valid api_key. Get one from https://jarvis-ai-api.herokuapp.com")
        else:
            if not os.path.exists(CONSTANT.USER_CONFIG_FOLDER):
                os.mkdir(CONSTANT.USER_CONFIG_FOLDER)
            if not os.path.exists(CONSTANT.API_KEY_PATH):
                with open(CONSTANT.API_KEY_PATH, 'w') as f:
                    f.write(self.api_key)
            else:
                with open(CONSTANT.API_KEY_PATH, 'r') as f:
                    api_key_tmp = f.read()
                if api_key_tmp != self.api_key:
                    with open(CONSTANT.API_KEY_PATH, 'w') as f:
                        f.write(self.api_key)

        if self.detect_wake_word:
            if self.wake_word_detection_method is None:
                raise ValueError("Invalid wake_word_engine. Expected a valid wake_word_engine. Expected one of: %s" % [
                    InputsMethods.voice_input_google_api,
                    InputsMethods.voice_input_deepspeech_streaming])
            elif self.wake_word_detection_method not in [InputsMethods.voice_input_google_api,
                                                         InputsMethods.voice_input_deepspeech_streaming]:
                raise ValueError(
                    "Invalid wake_word_engine. Expected one of: %s" % [InputsMethods.voice_input_google_api,
                                                                       InputsMethods.voice_input_deepspeech_streaming])
            elif self.wake_word_detection_method in [InputsMethods.voice_input_deepspeech_streaming]:
                if self.deepspeech_listen_obj is None:
                    print("Loading deepspeech model...")
                    try:
                        from services.asr_deepspeech_streaming.streaming import listen as deepspeech_listen, ARGS, \
                            vad_audio, \
                            model
                    except ImportError:
                        from JarvisAI.JarvisAI.services.asr_deepspeech_streaming.streaming import \
                            listen as deepspeech_listen, \
                            ARGS, \
                            vad_audio, model
                    self.ARGS = ARGS
                    self.vad_audio = vad_audio
                    self.model = model
                    self.deepspeech_listen_obj = deepspeech_listen(ARGS, vad_audio, model)

    def manage_tasks(self):
        if not self.detect_wake_word and (self.input_method == InputsMethods.voice_input_google_api or
                                          self.input_method == InputsMethods.voice_input_deepspeech_streaming):
            print("Waiting for your command...")
            # self.play_wake_up_sound()
        inp = self.input_method(
            deepspeech_listen_obj=self.deepspeech_listen_obj,
            google_speech_recognition_input_lang=self.google_speech_recognition_input_lang,
            google_speech_recognition_key=self.google_speech_recognition_key,
            google_speech_recognition_duration_listening=self.google_speech_recognition_duration_listening, )
        if inp is None:
            return
        inp = inp.lower()
        print("You said: " + inp)
        if inp == "stop" or inp == "exit":
            return "stop"

        if inp in list(self.custom_features.keys()):
            accuracy_ = 100
            task = inp
        else:
            task, accuracy_ = make_decision_jarvisai(self.api_key, inp)
        if self.display_intent:
            print("===========>", task.upper(), "with accuracy", accuracy_, "<===========")
        if accuracy_ > 0.5:
            fun = dict_of_features[task]
        else:
            classes = list(dict_of_features.keys())
            task = make_decision_jarvisai_string_matching(classes, inp)
            fun = dict_of_features[task]
            print("===========>", task.upper(), "<===========")
        #     fun = dict_of_features["conversation"]
        # perform action
        if fun is not None:
            call_out = fun(inp)
        else:
            call_out = "Sorry, I don't understand your command."
        if not call_out:
            call_out = "Sorry, I don't understand your command."

        if not self.output_method == OutputMethods.text_output:
            print(call_out)
        self.output_method(text=call_out)
        if inp not in list(self.custom_features.keys()):
            management_service(inp=inp, out=call_out, task=task, secret_key=self.api_key, debug=False)

    @verify_user
    def start(self):
        while True:
            if self.detect_wake_word:
                print("Listening for wake word...")
                wake_word = self.wake_word_detection_method(deepspeech_listen_obj=self.deepspeech_listen_obj)
                if wake_word is None:
                    continue
                if wake_word == "shutdown":
                    print("Shutting down...")
                    sys.exit()
                code1 = phonetics.metaphone(wake_word)
                code2 = phonetics.metaphone(self.bot_name)
                accuracy = fuzz.ratio(code1, code2)
                if len(wake_word) > 0 and accuracy > 50:
                    print("You Said: %s" % self.bot_name)
                    print("Wake word detected...")
                    print("Waiting for your command...")
                    self.play_wake_up_sound()
                    while True:
                        signal = self.manage_tasks()
                        if signal == "stop" or signal == "exit" or signal is None:
                            self.play_wake_up_sound(lock=True)
                            break
                        elif signal == "shutdown":
                            print("Shutting down...")
                            sys.exit()
            else:
                self.manage_tasks()


if __name__ == "__main__":
    # create your own function
    # It must contain parameter 'feature_command' which is the command you want to execute
    # Return is optional
    # If you want to provide return value it should only return text (str)
    # Your return value will be displayed or call out by the choice of OutputMethods of JarvisAI

    def custom_function(
            feature_command="custom command (which is the command you want to execute)"):
        # write your code here to do something with the command
        # perform some tasks
        # return is optional
        return feature_command + ' Executed'


    obj = JarvisAI(input_method=InputsMethods.text_input,
                   output_method=OutputMethods.text_output,
                   backend_tts_api='pyttsx3',
                   api_key="e91bb0bf7feafa0ecf6bb384e867cb98",
                   detect_wake_word=False,
                   wake_word_detection_method=InputsMethods.voice_input_google_api,
                   bot_name="Jarvis",
                   display_intent=True,
                   google_speech_recognition_input_lang='en',
                   google_speech_recognition_key=None,
                   google_speech_recognition_duration_listening=5
                   )

    obj.register_feature(feature_obj=custom_function, feature_command='custom feature')

    obj.start()
