import requests


def premium_chat(*args, **kwargs):
    # TODO: add this upcoming feature
    try:
        return "This feature is not available right now. We are working on it."
        with open('api_key.txt', 'r') as f:
            api_key = f.read()
        query = kwargs.get('query')
        url = f"https://jarvisai.in/premium_chatbot_api?query={query}&secret_key={api_key}"
        response = requests.get(url)
        return response.json().get("response", "Sorry, I don't know how to handle this intent.")
    except Exception as e:
        return f"An error occurred while performing premium_chat, connect with developer. Error: {e}"


if __name__ == "__main__":
    print(premium_chat("hi"))
