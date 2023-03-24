import requests


def premium_chat(*args, **kwargs):
    try:
        api_key = kwargs.get("api_key")
        query = kwargs.get('query')
        url = f"https://jarvisai.in/chatbot_premium_api?secret_key={api_key}&text={query}"
        response = requests.get(url)
        return response.json().get("message",  "Error Code=1. Server is facing some issues. Please try again later.")
    except Exception as e:
        return f"An error occurred while performing premium_chat, connect with developer. Error: {e}"


if __name__ == "__main__":
    print(premium_chat("hi"))
