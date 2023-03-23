import speech_recognition as sr
import pyaudio
import wave


def record_audio(duration=5):
    filename = "recording.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = duration
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    # print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()


def speech_to_text_google(input_lang='en', key=None, duration=5):
    try:
        print("Listening for next 5 seconds...")
        record_audio(duration=duration)
        r = sr.Recognizer()
        with sr.AudioFile("recording.wav") as source:
            audio = r.record(source)
            command = r.recognize_google(audio, language=input_lang, key=key)
        # TODO: Translate command to target language
        # if input_lang != 'en':
        #     translator = googletrans.Translator()
        #     command = translator.translate("command", dest='hi').text
        return command, True
    except Exception as e:
        print(e)
        return e, False


if __name__ == "__main__":
    print(speech_to_text_google())
