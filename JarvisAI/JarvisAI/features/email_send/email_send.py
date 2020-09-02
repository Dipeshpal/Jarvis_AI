import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import smtplib


def voice_to_text():
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
        command = voice_to_text();
    return command


def txt2speech(mytext):
    try:
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("tmp.mp3")
        playsound("tmp.mp3")
        os.remove("tmp.mp3")
    except Exception:
        mytext = "Sorry I couldn't understand, or not implemented to handle this input"
        print(mytext)
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("tmp2.mp3")
        playsound("tmp2.mp3")
        os.remove("tmp2.mp3")


def send_mail(data, models):
    print("To use this features make sure you have enabled less secure apps: \
     https://myaccount.google.com/lesssecureapps")
    print('Who is the recipient?')
    txt2speech('Who is the recipient?')
    recipient = input("Enter Email ID: ")
    print('What should I say to him?')
    txt2speech('What should I say to him?')
    msg = voice_to_text()

    user_config = data['user_config']
    email = user_config['email']
    if email == None:
        print("No email found in Database, please setup first")
        return "Please run 'setup' command to set your email id first."
    print("Is this your email ID?: " + email)
    txt2speech("Is this your email ID?: " + email)
    txt2speech("Confirm by typing y/Y for yes or anything else for NO")
    ch = input("Confirm by typing y/Y for yes or anything else for NO: ")
    if ch.lower() == 'y':
        txt2speech("Please enter your password-")
        pw = input("Password (we never save or share password): ")
        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(email, pw)
            mail.sendmail(email, recipient, msg)
            mail.close()
            return 'Email has been sent successfully. You can check your inbox.'
        except Exception as e:
            return "Unable to send mail, please check your credentials. Or there may be some technical error"
    else:
        return "Please run 'setup' command to set your email id first."
