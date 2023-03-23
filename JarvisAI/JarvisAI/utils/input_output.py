try:
    from utils.speech_to_text.speech_to_text import speech_to_text_google
    from utils.text_to_speech.text_to_speech import text_to_speech
    from utils.speech_to_text.speech_to_text_whisper import speech_to_text_whisper
except:
    from JarvisAI.utils.speech_to_text.speech_to_text import speech_to_text_google
    from JarvisAI.utils.text_to_speech.text_to_speech import text_to_speech
    from JarvisAI.utils.speech_to_text.speech_to_text_whisper import speech_to_text_whisper


class JarvisInputOutput:
    def __init__(self, input_mechanism='text', output_mechanism='text', logging=None,
                 google_speech_api_key=None, google_speech_recognition_input_lang='en',
                 duration_listening=5, backend_tts_api='pyttsx3',
                 use_whisper_asr=False, display_logs=False,
                 api_key=None):
        self.input_mechanism = input_mechanism
        self.output_mechanism = output_mechanism
        self.google_speech_api_key = google_speech_api_key
        self.google_speech_recognition_input_lang = google_speech_recognition_input_lang
        self.duration_listening = duration_listening
        self.backend_tts_api = backend_tts_api
        self.logging = logging
        self.use_whisper_asr = use_whisper_asr
        self.display_logs = display_logs
        self.api_key = api_key
        with open('api_key.txt', 'w') as f:
            f.write(api_key)
        # print("JarvisInputOutput initialized")
        # print(f"Input mechanism: {self.input_mechanism}")
        # print(f"Output mechanism: {self.output_mechanism}")
        # print(f"Google Speech API Key: {self.google_speech_api_key}")
        # print(f"Backend TTS API: {self.backend_tts_api}")

    def text_input(self):
        if self.input_mechanism == 'text':
            return input("Enter your query: ")
        else:
            self.logging.exception("Invalid input mechanism")
            raise ValueError("Invalid input mechanism")

    def text_output(self, text):
        if self.output_mechanism == 'text' or self.output_mechanism == 'both':
            print(text)
        else:
            self.logging.exception("Invalid output mechanism")
            raise ValueError("Invalid output mechanism")

    def voice_input(self, *args, **kwargs):
        if self.input_mechanism == 'voice':
            if self.use_whisper_asr:
                if self.display_logs:
                    print("Using Whisper ASR")
                command, status = speech_to_text_whisper(duration=self.duration_listening)
            else:
                if self.display_logs:
                    print("Using Google ASR")
                command, status = speech_to_text_google(input_lang=self.google_speech_recognition_input_lang,
                                                        key=self.google_speech_api_key,
                                                        duration=self.duration_listening)
            print(f"You Said: {command}")
            if status:
                return command
            else:
                return None
        else:
            self.logging.exception("Invalid input mechanism")
            raise ValueError("Invalid input mechanism")

    def voice_output(self, *args, **kwargs):
        if self.output_mechanism == 'voice' or self.output_mechanism == 'both':
            text = kwargs.get('text', None)
            text_to_speech(text=text, lang='en', backend_tts_api=self.backend_tts_api)
        else:
            self.logging.exception("Invalid output mechanism")
            raise ValueError("Invalid output mechanism")
