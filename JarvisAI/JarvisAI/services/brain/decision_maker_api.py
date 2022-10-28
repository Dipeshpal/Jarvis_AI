from pprint import pprint
import textdistance
import requests
try:
    from CONSTANT import Constant
except:
    from JarvisAI.CONSTANT import Constant


CONSTANT = Constant()


def make_decision_nlp(string, classes, secret_key=None):
    try:
        answer = []
        answer_ = {}
        answer_li = []
        for clas in classes.split(","):
            acc = textdistance.jaccard(string, clas)
            answer_li.append({'label': clas, 'confidence': acc})
            answer.append({'label': clas.strip(), 'confidence': acc})
            answer_[clas] = acc
        response = dict()
        response["data"] = [{'label': max(answer_, key=answer_.get).strip(),
                             'confidences': answer}]
        best = response["data"][0]["label"]
        return best
    except Exception as e:
        print(e)
        return None


def make_decision_ai(secret_key, string, classes):
    try:
        url = f'{CONSTANT.BASE_URL}make_decision_ktrain_api?secret_key={secret_key}'
        r = requests.post(url, json={'string': string,
                                     'classes': classes})
        res = r.json()
        res = res['action'], None
    except Exception as e:
        print(e)
        res = None
    return res


def make_decision_jarvisai(secret_key, string):
    try:
        url = f'{CONSTANT.BASE_URL}make_decision_intent_classifier?secret_key={secret_key}&string={string}'
        r = requests.get(url)
        res = r.json()
        res = res['action']['data'][0]['class'], res['action']['data'][0]['accuracy']
    except Exception as e:
        print(e)
        res = None
    return res


def make_decision_jarvisai_string_matching(classes_list, input_string):
    try:
        answer = []
        answer_ = {}
        answer_li = []
        for clas in classes_list:
            acc = textdistance.jaccard(input_string, clas)
            answer_li.append({'label': clas, 'confidence': acc})
            answer.append({'label': clas.strip(), 'confidence': acc})
            answer_[clas] = acc
        response = dict()
        response["data"] = [{'label': max(answer_, key=answer_.get).strip(),
                             'confidences': answer}]
        best = response["data"][0]["label"]
        return best
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    inp = "date"
    clss = "asking date, asking time, tell me joke, tell me news, tell me weather, tell me about, open website, play on youtube, send whatsapp message, send email"
    # pprint(make_decision_nlp(inp, clss))
    # pprint(make_decision_ai(inp, clss))
    pprint(make_decision_ai('5ba317a681c5d42361cda5b9f9ba7d0e', inp, clss))
    pprint(make_decision_jarvisai('5ba317a681c5d42361cda5b9f9ba7d0e', inp))
