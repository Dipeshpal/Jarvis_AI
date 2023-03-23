import wikipedia
import re


def tell_me_about(*args, **kwargs):
    # topic = kwargs.get("query")
    entities = kwargs.get("entities")
    li = ['EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG',
          'PERCENT', 'PERSON', 'PRODUCT', 'TIME', 'WORK_OF_ART']
    topic = [entity[0] for entity in entities if entity[1] in li][0]
    try:
        ny = wikipedia.page(topic)
        res = str(ny.content[:500].encode('utf-8'))
        res = re.sub('[^a-zA-Z.\d\s]', '', res)[1:]
        return res
    except Exception as e:
        print(e)
        return False
