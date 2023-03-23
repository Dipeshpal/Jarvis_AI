import whisper
import sounddevice
from scipy.io.wavfile import write
import time

model = whisper.load_model("base")


def recorder(second=5):
    fs = 16000
    print("Recording.....")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    write("./recording.wav", fs, record_voice)
    print("Finished.....")
    time.sleep(1)


def speech_to_text_whisper(duration=5):
    try:
        recorder(second=duration)
        result = model.transcribe("./recording.wav")
        return result.get("text"), True
    except Exception as e:
        print(e)
        return e, False


if __name__ == "__main__":
    speech_to_text_whisper()
