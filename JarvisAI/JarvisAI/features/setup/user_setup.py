import string
import os
from gtts import gTTS
from playsound import playsound


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


def setup_mode(data=None, model=None):
    print("You are in Setup mode, let's setup few things")
    txt2speech("You are in Setup mode, let's setup few things")
    user_name = input("Enter your name: ")
    country = input("Enter your country: ")
    country = string.capwords(country)
    age = ''
    not_int = False
    while not not_int:
        try:
            user_age = int(input("Enter your age: "))
            age = user_age
            not_int = True
        except Exception as e:
            user_age = 0
            age = user_age
            print("Enter only numbers")

    city = input("Enter your city: ")
    city = string.capwords(city)
    email = None
    while True:
        print("Would you like to provide Email, for Gmail mail send only")
        print("This will only use to send email. I am not asking for password.")
        ch = input("Type y/Y to YES or anything else to NO: ")
        if ch.lower() == 'y':
            email_id = input("Enter your Email ID: ")
            if email_id != None:
                email = email_id
                break
        else:
            break
    data['jarvis_obj'].update_user_config(user_name, country, city, age, email)
    print("New Configurations- \n", data['jarvis_obj'].user_config)
    return "Setup Completed"
