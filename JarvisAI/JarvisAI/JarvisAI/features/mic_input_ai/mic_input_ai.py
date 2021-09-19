# Voice Recognition using https://huggingface.co/facebook/wav2vec2-base-960h
import pyaudio
import wave
import os
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from lazyme.string import color_print as cprint

try:
    import torch
except ImportError:
    cprint("No Pytorch Found, Please install if manually from below link", color='yellow', underline=True, bold=True)
    cprint("https://pytorch.org/get-started/locally/", color='blue', underline=True, bold=True)


class MicRecord:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.WAVE_OUTPUT_FILENAME = "temp_record.wav"
        if os.path.exists(self.WAVE_OUTPUT_FILENAME):
            os.remove(self.WAVE_OUTPUT_FILENAME)

    def start_recording(self, record_seconds=5, debug=False):
        audio = pyaudio.PyAudio()
        # start Recording
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)
        print(f"Listening for {record_seconds} Seconds")
        if debug:
            print("recording...")
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * record_seconds)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        if debug:
            print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()


class SpeechRecognition(MicRecord):
    def __init__(self):
        super().__init__()
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
        self.model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    def start_speech_recognition(self, record_seconds=5, debug=False):
        self.start_recording(record_seconds=record_seconds, debug=debug)
        print("Recognizing...")
        input_audio, _ = librosa.load(self.WAVE_OUTPUT_FILENAME, sr=16000)
        input_values = self.tokenizer(input_audio, return_tensors="pt").input_values
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.batch_decode(predicted_ids)[0]
        os.remove(self.WAVE_OUTPUT_FILENAME)
        return transcription.lower()


if __name__ == '__main__':
    obj = SpeechRecognition()
    transcription = obj.start_speech_recognition()
    print(transcription)
