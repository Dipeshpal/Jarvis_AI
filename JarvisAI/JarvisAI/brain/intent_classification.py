import os
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from element_manager import *
import time
import requests


def check_local_intent(text):
    """Check if the intent of a text string is available locally.

    Args:
        text (str): The text string to check.

    Returns:
        str: The intent of the text string.
    """
    try:
        if not os.path.exists('actions.json'):
            return None
        else:
            with open('actions.json', 'r') as f:
                actions = json.load(f)
            # Below is sample actions.json file
            # [
            #   {
            #     "intent": "greet and hello hi kind of things",
            #     "example": []
            #   },
            #   {
            #     "intent": "goodbye",
            #     "example": ['bye', 'goodbye', 'see you later']
            #   }
            # ]
            # if text in example then return intent
            for action in actions:
                if text in action['example']:
                    return action['intent']
                if action['intent'] in text:
                    return action['intent']
                if action['example'] == "":
                    continue
    except Exception as e:
        return None


def try_to_classify_intent(secret_key, text):
    """Classify the intent of a text string using the JarvisAI API.

       Args:
           text (str): The text string to classify.

       Returns:
           str: The intent of the text string.
       """
    try:
        intent = check_local_intent(text)
        if intent is not None:
            return intent, 1.0
    except Exception as e:
        pass

    try:
        url = f'https://jarvisai.in/intent_classifier?secret_key={secret_key}&text={text}'
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            return data['data'][0], data['data'][1]
    except Exception as e:
        raise Exception('Something went wrong while classifying the intent.')


def restart_server():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get('https://huggingface.co/spaces/dipesh/dipesh-Intent-Classification-large')

        time.sleep(4)
        # to click on the element(Restart this Space) found
        driver.find_element(By.XPATH, get_xpath(driver, 'd7n5Js111lAwV_U')).click()
        return True, 'Server restarted successfully'
    except Exception as e:
        print(e)
        print("Make sure chromedriver.exe is in the same folder as your script")
        return False, 'Server restart failed'


def classify_intent(secret_key, text):
    for i in range(3):
        try:
            return try_to_classify_intent(secret_key, text)
        except Exception as e:
            restart_server()
            return try_to_classify_intent(secret_key, text)


if __name__ == "__main__":
    intent, _ = classify_intent('99f605ce-5bf9-4e80-93a3-f367df65aa27', "custom function")
    print(intent, _)
