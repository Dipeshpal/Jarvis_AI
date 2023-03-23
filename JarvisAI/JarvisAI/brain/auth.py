import shutup
import requests
import json

shutup.please()


def verify_user(func):
    def inner(self, *args, **kwargs):
        with open('api_key.txt', 'r') as f:
            api_key = f.read()
        url = f'https://jarvisai.in/check_secret_key?secret_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            status = json.loads(response.content)
            if status:
                print("Authentication Successful")
                return func(self, *args, **kwargs)  # Return the result of calling func
            else:
                print("Authentication Failed. Please check your API key.")
                exit()
        else:
            print(f'Error: {response.status_code}')
            exit()

    return inner


if __name__ == "__main__":
    data = verify_user("527557f2-0b67-4500-8ca0-03766ade589a")
    print(data, type(data))
