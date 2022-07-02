import json
import requests
import shutup
try:
    from CONSTANT import Constant
except:
    from JarvisAI.CONSTANT import Constant


CONSTANT = Constant()
shutup.please()


def verify_user(method):
    def inner(ref):
        with open(CONSTANT.API_KEY_PATH, 'r') as f:
            api_key = f.read()
        response = requests.get(f'{CONSTANT.API_AUTH_URL}{api_key}')
        if response.status_code == 200:
            status = json.loads(response.content)
            if status:
                print("Authentication Successful")
                return method(ref)
            else:
                print("Authentication Failed. Please check your API key.")
                exit()
        else:
            print(f'Error: {response.status_code}')
            return False

    return inner


if __name__ == '__main__':
    print(verify_user(print))
    print('Done')
