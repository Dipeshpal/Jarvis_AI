import wikipedia
import re


def tell_me_about(topic):
    try:
        ny = wikipedia.page(topic)
        res = str(ny.content[:500].encode('utf-8'))
        res = re.sub('[^a-zA-Z.\d\s]', '', res)[1:]
        return res
    except Exception as e:
        print(e)
        return False