import json

import requests
import webbrowser


class JarvisAIAPI:
    def __init__(self):
        pass

    def get_user_data(self, token):
        # https://jarvis-ai-api.herokuapp.com/get_user_data_by_token_api/?token=5ec64be7ff718ac25917c198f3d7a4
        url = f'https://jarvis-ai-api.herokuapp.com/get_user_data_by_token_api/?token={token}'
        x = requests.get(url)
        return x.status_code, x.json()

    def set_user_data(self):
        url = 'https://jarvis-ai-api.herokuapp.com/login/'
        webbrowser.open(url, new=2)

    def add_user_raw_data(self, token: str, data: dict):
        url = f'https://jarvis-ai-api.herokuapp.com/update_user_json_data_by_token_api/?token={token}&raw_data={data}'
        x = requests.get(url)
        metadata = x.json()
        return x.status_code, metadata

    def get_user_raw_data(self, token: str):
        url = f'https://jarvis-ai-api.herokuapp.com/get_user_raw_data_by_token_api/?token={token}'
        x = requests.get(url)
        try:
            metadata = x.json()
            status = x.status_code
            x = x.json()['data']['raw_data'].strip()
            ans = x.replace("'", '"')
            data = json.loads(ans)
            return status, metadata, data
        except Exception as e:
            print(e, "\n", "Error/Warning in jarvisai_api.py in 'get_user_raw_data()' ")
            print("You can ignore if you are using JarvisAI for the first time, it's one time warning")
            return False, {}, {}

    def update_user_data(self, token: str, new_data: dict):
        status, metadata, data = self.get_user_raw_data(token)
        data.update(new_data)
        status_code, metadata = self.add_user_raw_data(token, data)
        return status_code, metadata

    def delete_all_user_raw_data(self, token: str):
        data = {}
        url = f'https://jarvis-ai-api.herokuapp.com/update_user_json_data_by_token_api/?token={token}&raw_data={data}'
        x = requests.get(url)
        metadata = x.json()
        return x.status_code, metadata


if __name__ == '__main__':
    obj = JarvisAIAPI()
    data = {'new2': 'hi', 's': ['d']}
    status, res = obj.update_user_data("adc0a911a43f8b5edce4b44f4c65f7", data)
    status, metadata, data = obj.get_user_raw_data("adc0a911a43f8b5edce4b44f4c65f7")
    print(data)
    # obj.update_user_data("adc0a911a43f8b5edce4b44f4c65f7", {'new3': 2})
    # status, metadata, data = obj.get_user_raw_data("adc0a911a43f8b5edce4b44f4c65f7")
    # print(data)
    # obj.delete_all_user_raw_data("adc0a911a43f8b5edce4b44f4c65f7")
    # status, metadata, data = obj.get_user_raw_data("adc0a911a43f8b5edce4b44f4c65f7")
    # print(data)
