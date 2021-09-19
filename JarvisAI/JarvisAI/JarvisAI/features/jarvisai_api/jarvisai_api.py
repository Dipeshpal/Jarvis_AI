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


if __name__ == '__main__':
    obj = JarvisAIAPI()
    status, res = obj.get_user_data("xxxxx")
    print(status)
    print(res)
    print(type(res))
