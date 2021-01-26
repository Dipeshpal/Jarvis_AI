import wikipedia
import string


def tell_me_about(topic, sentences):
    try:
        res = wikipedia.summary(title=string.capwords(topic), sentences=sentences, auto_suggest=False)
        return res
    except Exception as e:
        print(e)
        return False
