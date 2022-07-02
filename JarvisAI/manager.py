import sys

import requests


def management(inp, out, task, secret_key, debug=False):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'secret_key': secret_key,
    }

    json_data = {
        'inp': inp,
        'out': out,
        'task': task,
        'secret_key': secret_key,
    }

    response = requests.post('https://jarvis-ai-api.herokuapp.com/log_inp_out', params=params, headers=headers, json=json_data)
    status = response.json().get('status', None)
    if status:
        if debug:
            print("Working...")
        return True
    else:
        print("WARNING: Do not change JarvisAI's code, or it will break and you will be banned from using it.")
        sys.exit()
