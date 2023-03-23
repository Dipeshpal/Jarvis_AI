import os
import requests
import json


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
            for action in actions:
                if text in action['example']:
                    return action['intent']
    except Exception as e:
        return e


def classify_intent(secret_key, text):
    """Classify the intent of a text string using the Wit.ai API.

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
        return e, None


if __name__ == "__main__":
    intent, _ = classify_intent('527557f2-0b67-4500-8ca0-03766ade589a', "what is the time")
    print(intent, _)
