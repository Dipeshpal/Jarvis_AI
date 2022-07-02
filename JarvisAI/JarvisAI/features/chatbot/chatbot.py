from pprint import pprint

import requests
import numpy as np
import os

try:
    from CONSTANT import Constant
except:
    from JarvisAI.CONSTANT import Constant

CONSTANT = Constant()


def chatbot_only_chat(message):
    if not os.path.exists(CONSTANT.API_KEY_PATH):
        return f"""Please create a {CONSTANT.API_KEY_PATH} file with your secret key in it.
        It's used for security purpose.
        Get your free key from "{CONSTANT.BASE_URL}"
        """
    else:
        with open(CONSTANT.API_KEY_PATH, "r") as f:
            secret_key = f.read()

    if os.path.exists('step.npy'):
        step = str(np.load('step.npy'))
    else:
        step = '0'
    url = f"{CONSTANT.BASE_URL}chatbot_api_only_chat?secret_key={secret_key}&message={message}&step={step}"
    response = requests.get(url)
    res = response.json()
    status = res['status']

    if status:
        step = int(res['response']['data'][0]['step'])
        np.save('step.npy', step)
        return res['response']['data'][0]['res']
    else:
        return res['response'] + '\n' + f"Get a new secret key from {CONSTANT.BASE_URL}"


def chatbot_general_purpose(message: str, google_result: bool = False, youtube_result: bool = False, *args, **kwargs):
    if not os.path.exists(CONSTANT.API_KEY_PATH):
        return f"""Please create a {CONSTANT.API_KEY_PATH} file with your secret key in it.
        It's used for security purpose.
        Get your free key from "{CONSTANT.BASE_URL}"
        """
    else:
        with open(CONSTANT.API_KEY_PATH, "r") as f:
            secret_key = f.read()

    if os.path.exists('step.npy'):
        step = str(np.load('step.npy'))
    else:
        step = '0'

    url = f"{CONSTANT.BASE_URL}chatbot_api_general_purpose?secret_key={secret_key}&query={message}&google_result={google_result}&youtube_result={youtube_result}"
    response = requests.get(url)
    try:
        res = response.json()
        if res['status']:
            step = int(res['response']['response']['data'][0][0]['weights_of_all_models']['conversation'][-1]['step'])
            np.save('step.npy', step)
            conversation = res['response']['response']['data'][0][0]['weights_of_all_models']['conversation'][0]

            suggested_answer = res['response']['response']['data'][0][0]['suggested_answer']['answer']

            return suggested_answer
        else:
            return "Something went wrong with chatbot_api_general_purpose server"
    except Exception as e:
        return f"Something went wrong with chatbot_api_general_purpose server {e}"


if __name__ == "__main__":
    # for i in range(7):
    pprint(chatbot_general_purpose("weather in Madhya Pradesh"))
